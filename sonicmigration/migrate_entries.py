#!/usr/bin/env python3
"""Migrate Jekyll `entry` markdown files into the SonicJS "entries" collection.

Run next to utils.py (needs `pip install pyyaml`):

    python3 migrate_entries.py path/to/_entries --dry-run --limit 5   # preview, no writes
    python3 migrate_entries.py path/to/_entries --limit 5             # try a few for real
    python3 migrate_entries.py path/to/_entries                       # everything

What it does per file
  * front matter -> SonicJS fields. A front-matter field with no matching SonicJS field is
    ignored; all ignored fields are listed in a warning summary at the end.
  * body: Liquid gallery includes become [gallery] shortcodes; `page_images` becomes a grid gallery
  * `links_references` is appended to the END of the body
  * references (attributes, zone, habitats) are swapped for the referenced item's id
  * entries whose slug already exists in SonicJS are skipped, so reruns are safe
"""
import argparse
import http.client
import json
import os
import re
import sys
import threading
import time
from urllib.parse import urlsplit
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import yaml

from utils import login, load_dotenv

# ----------------------------------------------------------------------------------------------
# CONFIG – adjust to your SonicJS collections
# ----------------------------------------------------------------------------------------------
COLLECTION = "entries"
CONTENT_FIELD = "content"  # SonicJS field that receives the markdown body

# Jekyll front-matter field -> (SonicJS collection to look in, what the Jekyll value is matched against)
REFERENCES = {
    "attributes": ("attributes", "slug"),   # [155]  -> attribute whose slug is "155"
    "zone": ("zones", "title"),             # [intertidal, marine]
    "habitats": ("habitats", "title"),      # [mangrove, rocky shore]
}

# If the Jekyll name isn't a SonicJS field, try these names before giving up.
ALIASES = {
    "zone": ["zones"],
    "habitats": ["habitat"],
    "attributes": ["attribute"],
    "inat_id": ["inaturalist_id", "inat"],
    "coverimg": ["cover_image", "coverImage"],
    "rdb": ["rdb3"],
}

REQUIRED_BY_COLLECTION = {}  # collection name -> set of required field names, filled from each schema

# Consumed by the converter itself, never copied as fields.
CONSUMED = {"layout", "galleries", "links_references", "page_images"}
# ----------------------------------------------------------------------------------------------


# ---- HTTP -----------------------------------------------------------------------------------
# One persistent (keep-alive) connection per worker thread: against a deployed Worker this saves a
# TCP + TLS handshake on every request. 429/503 responses are retried with backoff.
_local = threading.local()


def _connection(base):
    conn = getattr(_local, "conn", None)
    if conn is None:
        cls = http.client.HTTPSConnection if base.scheme == "https" else http.client.HTTPConnection
        conn = _local.conn = cls(base.netloc, timeout=30)
    return conn


def api(method, path, token, body=None):
    base = urlsplit(os.environ.get("SONICJS_URL", "http://localhost:8787"))
    headers = {"Authorization": f"Bearer {token}"}
    data = None
    if body is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(body).encode()
    reconnected = False
    for attempt in range(6):
        reused = getattr(_local, "conn", None) is not None
        try:
            conn = _connection(base)
            conn.request(method, base.path.rstrip("/") + path, body=data, headers=headers)
            resp = conn.getresponse()
            text = resp.read().decode("utf-8", "replace")
        except (http.client.RemoteDisconnected, ConnectionResetError, BrokenPipeError, http.client.CannotSendRequest):
            _local.conn = None  # stale keep-alive connection: open a fresh one
            if reused and not reconnected:
                reconnected = True
                continue
            raise
        if resp.status in (429, 503) and attempt < 5:
            time.sleep(float(resp.getheader("Retry-After") or 0) or min(2 ** attempt, 20))
            continue
        return resp.status, text
    return resp.status, text


def items_of(payload):
    if isinstance(payload, list):
        return payload
    return payload.get("data", payload.get("items", []))


def fv(item, key):
    """Field value: top level first, then nested under "data"."""
    if key in item and item[key] is not None:
        return item[key]
    return (item.get("data") or {}).get(key)


def fetch_all(collection, token, page_size=100):
    out, seen, offset = [], set(), 0
    while True:
        status, text = api("GET", f"/api/{collection}?limit={page_size}&offset={offset}", token)
        if not 200 <= status < 300:
            sys.exit(f"GET /api/{collection} failed: {status} {text}")
        items = [i for i in items_of(json.loads(text)) if i["id"] not in seen]
        if not items:
            break
        seen.update(i["id"] for i in items)
        out.extend(items)
        offset += len(items)
    return out


def discover_schema(token, collection=None):
    """Return {field name: type} for a collection (default COLLECTION) from GET /api/collections."""
    collection = collection or COLLECTION
    status, text = api("GET", "/api/collections", token)
    if not 200 <= status < 300:
        sys.exit(f"GET /api/collections failed: {status} {text}")
    for c in items_of(json.loads(text)):
        if collection in (c.get("name"), c.get("slug")):
            schema = c.get("schema") or {}
            if isinstance(schema, str):
                schema = json.loads(schema)
            if isinstance(schema.get("fields"), list):
                return {f["name"]: f.get("type", "string") for f in schema["fields"]}
            if isinstance(schema.get("properties"), dict):
                req = REQUIRED_BY_COLLECTION.setdefault(collection, set())
                req.update(schema.get("required") or [])
                req.update(k for k, v in schema["properties"].items() if (v or {}).get("required") is True)
                types = {}
                for k, v in schema["properties"].items():
                    v = v or {}
                    t = v.get("type", "string")
                    item_t = (v.get("items") or {}).get("type")
                    types[k] = f"array<{item_t}>" if t == "array" and item_t in ("number", "integer") else t
                return types
    sys.exit(f'collection "{collection}" not found in /api/collections (or its schema has an unknown shape); '
             "pass --fields title,slug,content,... to set the field list by hand")


def schema_for(collection, token, args):
    try:
        return discover_schema(token, collection)
    except SystemExit:
        print(f'warning: could not read the "{collection}" schema; sending only its known fields', file=sys.stderr)
        return {"name": "string", "link": "string"}


# ---- parsing --------------------------------------------------------------------------------
FRONT_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?(.*)\Z", re.S)


def parse_file(path):
    m = FRONT_RE.match(path.read_text(encoding="utf-8"))
    if not m:
        return None, None
    return yaml.safe_load(m.group(1)) or {}, m.group(2)


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def clean_caption(c):
    c = re.sub(r"\s+", " ", str(c or "")).strip()
    return c.replace("|", "/")  # "|" is the field separator in the shortcode


def shortcode(items, style="wrap", cols=None, height=None, warn=None):
    lines = []
    for it in items or []:
        url = str(it.get("url", "")).strip()
        if not url:
            continue
        if not re.match(r"^(https?://|/)", url):
            if warn:
                warn(f"relative image url {url!r} made site-relative")
            url = "/" + url.lstrip("./")
        caption = clean_caption(it.get("caption"))
        cs, rs = it.get("col_span"), it.get("row_span")
        span = f"{cs or 1}x{rs or 1}" if (cs or rs) else ""
        lines.append(" | ".join([url, caption] + ([span] if span else [])) if (caption or span) else url)
    if not lines:
        return ""
    attrs = ""
    if style != "wrap":
        attrs += f' style="{style}"'
    if cols:
        attrs += f' cols="{cols}"'
    if height:
        attrs += f' height="{height}"'
    return f"[gallery{attrs}]\n" + "\n".join(lines) + "\n[/gallery]"


INCLUDE_RE = re.compile(r"\{%-?\s*include\s+(img-wrap-group|img-grid|justifiedgallery)\.html\s+(.*?)\s*-?%\}", re.S)
STYLE_OF = {"img-wrap-group": "wrap", "img-grid": "grid", "justifiedgallery": "justified"}


def convert_includes(body, fm, warn):
    def repl(m):
        kind, argstr = m.group(1), m.group(2)
        args = {k: v.strip("\"'") for k, v in re.findall(r"(\w+)\s*=\s*(\"[^\"]*\"|'[^']*'|\S+)", argstr)}
        node = {"page": fm}
        for part in args.get("items", "").split("."):
            node = node.get(part) if isinstance(node, dict) else None
            if node is None:
                break
        if not isinstance(node, list):
            warn(f"could not resolve gallery items {args.get('items')!r}; include left in place")
            return m.group(0)
        code = shortcode(node, STYLE_OF[kind], cols=args.get("cols"), height=args.get("height"), warn=warn)
        # Blank lines on both sides: the shortcode must be its own markdown block, otherwise a
        # preceding text line would swallow it into the same paragraph.
        return f"\n\n{code}\n\n" if code else ""

    return INCLUDE_RE.sub(repl, body)


# ---- authors --------------------------------------------------------------------------------
AUTHORS_COLLECTION = "authors"  # fields: name (string), link (string)


def parse_author(raw):
    """'[Ria Tan](https://…)' -> ('Ria Tan', 'https://…');  'John' -> ('John', '')."""
    raw = str(raw).strip()
    m = re.search(r"\[([^\]]+)\]\(([^)\s]+)\)", raw)
    if m:
        name = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", raw)
        return re.sub(r"[*_]", "", name).strip(), m.group(2).strip()
    return re.sub(r"[*_]", "", raw).strip(), ""


def extract_id(text):
    try:
        d = json.loads(text)
    except ValueError:
        return None
    if not isinstance(d, dict):
        return None
    inner = d.get("data")
    return d.get("id") or (inner.get("id") if isinstance(inner, dict) else None)


# ---- field conversion -----------------------------------------------------------------------
def to_number(x):
    try:
        return float(str(x).strip())
    except ValueError:
        return None


def coerce(value, ftype, name, warn):
    if hasattr(value, "isoformat"):
        return value.isoformat()
    if ftype == "array<number>":
        out = []
        for v in (value if isinstance(value, list) else [value]):
            for piece in str(v).split(","):  # entry.html also split comma-separated sizes
                if not piece.strip():
                    continue
                n = to_number(piece)
                if n is None:
                    warn(f"{name}: {piece.strip()!r} is not a number; dropped")
                else:
                    out.append(n)
        return out
    if ftype in ("number", "integer"):
        if isinstance(value, list):
            if len(value) > 1:
                warn(f"{name}: number field got {len(value)} values; kept the first")
            value = value[0] if value else None
        return int(value) if ftype == "integer" and value is not None else value
    if ftype == "array":
        return value if isinstance(value, list) else [value]
    if ftype in ("string", "textarea", "slug") and isinstance(value, list):
        return ", ".join(str(v) for v in value)
    if ftype in ("string", "textarea", "slug") and not isinstance(value, str):
        return str(value)  # e.g. inat_id 119047 -> "119047"
    return value


def build_payload(path, fm, body, schema, ref_maps, warn, ignored, author_refs):
    """author_refs collects (field, [(key, name, link), ...]) so authors can be created before posting."""
    payload = {}
    fm = dict(fm)

    # body: gallery includes, page_images grid, then links_references at the very end
    body = convert_includes(body, fm, warn).rstrip()
    if fm.get("page_images"):
        grid = shortcode(fm["page_images"], "grid", warn=warn)
        if grid:
            body += "\n\n" + grid
    if fm.get("links_references"):
        body += "\n\n" + str(fm["links_references"]).strip()
    body = re.sub(r"\n{3,}", "\n\n", body)
    leftover = re.findall(r"\{%.*?%\}|\{\{.*?\}\}", body, re.S)
    if leftover:
        warn(f"Liquid left in body: {leftover[0][:60]!r}" + (f" (+{len(leftover) - 1} more)" if len(leftover) > 1 else ""))
    payload[CONTENT_FIELD] = body + "\n"

    for key, value in fm.items():
        if key in CONSUMED or value in (None, "", [], {}):
            continue
        target = key if key in schema else next((a for a in ALIASES.get(key, []) if a in schema), None)
        if target is None:
            ignored[key].append(path.name)
            continue
        if key == "permalink":
            link = str(value).strip()
            if ":" in link:
                warn(f"permalink {link!r} has placeholders; not stored")
                continue
            payload[target] = "/" + re.sub(r"/{2,}", "/", link).lstrip("/")
            continue
        if key == "authors":
            people = []
            for raw in (value if isinstance(value, list) else [value]):
                name, link = parse_author(raw)
                if name:
                    people.append((name.lower(), name, link))
            if people:
                author_refs.append((target, people))
            continue
        if key in REFERENCES:
            values = value if isinstance(value, list) else [value]
            ids = []
            for v in values:
                rid = ref_maps[key].get(str(v).strip().lower())
                if rid:
                    ids.append(rid)
                else:
                    warn(f"{key}: no {REFERENCES[key][0]} item matches {v!r}; dropped")
            if ids:
                payload[target] = ids
            continue
        payload[target] = coerce(value, schema[target], key, warn)
    return payload


def shape_body(payload, shape):
    if shape == "flat":
        return payload
    top = {k: payload[k] for k in ("title", "slug", "status") if k in payload}
    return {**top, "data": {k: v for k, v in payload.items() if k not in top}}


# ---- main -----------------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src", help="folder containing the Jekyll entry .md files")
    ap.add_argument("--dry-run", action="store_true", help="build payloads, write preview.json, POST nothing")
    ap.add_argument("--limit", type=int, help="only process the first N files")
    ap.add_argument("--fields", help="comma-separated SonicJS field names (skips schema discovery)")
    ap.add_argument("--concurrency", type=int, default=4)
    ap.add_argument("--shape", choices=["flat", "data"], default="flat",
                    help='request body: "flat" = every field at top level; "data" = title/slug/status at top level, '
                         "everything else inside a data object (use probe_create.py to see which one your server keeps)")
    ap.add_argument("--endpoint", help="create endpoint path (default /api/<collection>); e.g. /api/collections/entries/content")
    ap.add_argument("--status", help='optional top-level status to send, e.g. "published" (unverified: check the entry in the admin)')
    args = ap.parse_args()

    load_dotenv()
    token = login()

    if args.fields:
        schema = {f.strip(): "string" for f in args.fields.split(",")}
    else:
        schema = discover_schema(token)
    for needed in ("title", "slug", CONTENT_FIELD):
        if needed not in schema:
            sys.exit(f'SonicJS "{COLLECTION}" has no field named {needed!r}; found: {sorted(schema)}')
    print(f"SonicJS fields: {', '.join(sorted(schema))}")
    if schema[CONTENT_FIELD] == "lexical":
        print(
            f'\nWARNING: "{CONTENT_FIELD}" is a lexical field, which stores editor JSON, but this script sends Jekyll '
            "markdown text.\n  Either change the field to type 'markdown' (keeps the markdown and [gallery] shortcodes as-is) "
            "or add a markdown -> Lexical converter.\n",
            file=sys.stderr,
        )

    # lookup maps for reference fields (only those the collection can actually hold)
    ref_maps = {}
    for key, (coll, match_on) in REFERENCES.items():
        if key in schema or any(a in schema for a in ALIASES.get(key, [])):
            ref_maps[key] = {str(fv(i, match_on)).strip().lower(): i["id"] for i in fetch_all(coll, token) if fv(i, match_on) is not None}
            print(f"loaded {len(ref_maps[key])} {coll} for {key}")
        else:
            ref_maps[key] = {}

    author_schema, author_ids = {}, {}
    if "authors" in schema or any(a in schema for a in ALIASES.get("authors", [])):
        author_schema = schema_for(AUTHORS_COLLECTION, token, args)
        author_ids = {str(fv(i, "name")).strip().lower(): i["id"] for i in fetch_all(AUTHORS_COLLECTION, token) if fv(i, "name")}
        print(f"loaded {len(author_ids)} authors")

    existing = {str(fv(i, "slug")) for i in fetch_all(COLLECTION, token)}
    print(f"{len(existing)} entries already in SonicJS")

    files = sorted(Path(args.src).rglob("*.md"))
    if args.limit:
        files = files[: args.limit]

    # slug: the last segment of the front-matter `permalink` if there is one, otherwise the slugified
    # title. Titles of "-" (the site shows the scientific name for those) use genus + species, and
    # anything still empty falls back to the file name.
    def base_slug(p, fm, warn):
        permalink = fm.get("permalink")
        if permalink:
            if ":" in str(permalink):
                warn(f"permalink {permalink!r} has placeholders; slug taken from the title instead")
            else:
                segs = [x for x in str(permalink).split("/") if x]
                if segs:
                    return slugify(re.sub(r"\.(html?|php)$", "", segs[-1])), True
        slug = slugify(str(fm.get("title", "")))
        if not slug:
            slug = slugify(f"{fm.get('genus') or ''} {fm.get('species') or ''}")
        if not slug:
            slug = slugify(p.parent.name if p.stem.lower() == "index" else p.stem)
            warn(f"title {fm.get('title')!r} gives no slug; used the file name")
        return slug, False

    parsed, ignored, problems = [], defaultdict(list), []
    for p in files:
        fm, body = parse_file(p)
        warnings = []
        if fm is None or not fm.get("title"):
            problems.append((p.name, "no front matter or no title; skipped"))
            continue
        slug, explicit = base_slug(p, fm, warnings.append)
        parsed.append((p, fm, body, slug, explicit, warnings))
    counts = Counter(x[3] for x in parsed)
    explicit_counts = Counter(x[3] for x in parsed if x[4])  # slugs that come from a permalink

    jobs, final_counts = [], Counter()
    for p, fm, body, slug, explicit, warnings in parsed:
        warn = warnings.append
        if not slug:
            problems.append((p.name, "empty slug; skipped"))
            continue
        # on a clash, an entry whose slug comes from its permalink keeps it (unless another permalink
        # produced the same slug); title-based slugs get the folder name prefixed
        if counts[slug] > 1 and not (explicit and explicit_counts[slug] == 1):
            slug = slugify(f"{p.parent.name}-{slug}")
            warn(f"slug clash, using {slug!r}")
        final_counts[slug] += 1
        if final_counts[slug] > 1:  # still not unique (same title in the same folder)
            slug = f"{slug}-{final_counts[slug]}"
            warn(f"slug still clashes, using {slug!r}")
        author_refs = []
        payload = build_payload(p, fm, body, schema, ref_maps, warn, ignored, author_refs)
        payload["title"] = str(fm["title"])
        payload["slug"] = slug
        if args.status:
            payload["status"] = args.status
        for req in sorted(REQUIRED_BY_COLLECTION.get(COLLECTION, set())):
            if req not in payload and not (req == "authors" and author_refs):
                warn(f"required field {req!r} is empty; SonicJS will probably reject this entry")
        jobs.append((p, slug, payload, author_refs))
        for w in warnings:
            problems.append((p.name, w))

    todo = [j for j in jobs if j[1] not in existing]
    print(f"{len(jobs)} parsed, {len(jobs) - len(todo)} already exist, {len(todo)} to create")

    # authors: create the ones that don't exist yet (first spelling/link wins), then fill in ids
    wanted = {}
    for _p, _slug, _payload, refs in todo:
        for _field, people in refs:
            for key, name, link in people:
                if key in wanted and link and wanted[key][1] and link != wanted[key][1]:
                    problems.append((_p.name, f"author {name!r} appears with a different link; kept {wanted[key][1]!r}"))
                wanted.setdefault(key, (name, link))
    missing = {k: v for k, v in wanted.items() if k not in author_ids}
    if missing:
        print(f"{len(missing)} new authors to create" + (" (dry run: not created)" if args.dry_run else ""))
    for key, (name, link) in missing.items():
        for req in sorted(REQUIRED_BY_COLLECTION.get(AUTHORS_COLLECTION, set())):
            if req == "link" and not link:
                problems.append(("authors", f"{name!r} has no link but {req!r} is required in the authors schema; creation will probably fail"))
        if args.dry_run:
            author_ids[key] = f"NEW-AUTHOR:{name}"
            continue
        body_a = {"name": name}
        if link:
            body_a["link"] = link
        if "title" in author_schema:
            body_a["title"] = name
        if "slug" in author_schema:
            body_a["slug"] = slugify(name)
        status, text = api("POST", f"/api/{AUTHORS_COLLECTION}", token, body_a)
        if not 200 <= status < 300:
            problems.append(("authors", f"could not create {name!r}: {status} {text[:200]}"))
            continue
        author_ids[key] = extract_id(text) or next(
            (i["id"] for i in fetch_all(AUTHORS_COLLECTION, token) if str(fv(i, "name")).strip().lower() == key), None)
    for _p, _slug, payload, refs in todo:
        for field, people in refs:
            ids = [author_ids[k] for k, _n, _l in people if author_ids.get(k)]
            if ids:
                payload[field] = ids

    created, failed = 0, []
    if args.dry_run:
        Path("preview.json").write_text(json.dumps([shape_body(j[2], args.shape) for j in todo], indent=2, ensure_ascii=False), encoding="utf-8")
        print("dry run: wrote preview.json, nothing sent")
    else:
        def send(job):
            p, slug, payload, _refs = job
            status, text = api("POST", args.endpoint or f"/api/{COLLECTION}", token, shape_body(payload, args.shape))
            return None if 200 <= status < 300 else {"file": str(p), "slug": slug, "status": status, "body": text[:300]}

        t0, done = time.time(), 0
        with ThreadPoolExecutor(max_workers=args.concurrency) as pool:
            for res in pool.map(send, todo):
                done += 1
                if res:
                    failed.append(res)
                else:
                    created += 1
                if done % 100 == 0 or done == len(todo):
                    rate = done / max(time.time() - t0, 0.001)
                    print(f"  {done}/{len(todo)}  {rate:.1f}/s  ~{(len(todo) - done) / rate / 60:.1f} min left", flush=True)
        print(f"created {created}/{len(todo)}, failed {len(failed)}, {time.time() - t0:.0f}s total")

    # ---- warnings summary ----
    if ignored:
        print("\nWARNING: front-matter fields with no matching SonicJS field (ignored):")
        for key, names in sorted(ignored.items(), key=lambda kv: -len(kv[1])):
            print(f"  {key}: {len(names)} entries (e.g. {names[0]})")
    if problems:
        print(f"\nWARNING: {len(problems)} per-file issue(s):")
        for name, msg in problems[:40]:
            print(f"  {name}: {msg}")
        if len(problems) > 40:
            print(f"  ... and {len(problems) - 40} more (see migration-report.json)")
    Path("migration-report.json").write_text(
        json.dumps({"ignored_fields": {k: len(v) for k, v in ignored.items()}, "issues": problems, "failed": failed}, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    if failed:
        print(json.dumps(failed[:5], indent=2), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()