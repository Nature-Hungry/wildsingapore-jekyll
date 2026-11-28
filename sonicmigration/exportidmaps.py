"""Write habitats.json, zones.json and attributes.json, each mapping {id: title}.

Reads what is already in SonicJS (GET /api/<collection>), so it does not insert anything
and is safe to rerun. Put it next to utils.py and run:  python3 exportIdMaps.py
"""
import json
import os
import sys
import urllib.error
import urllib.request

from utils import login, load_dotenv


def get(path, token=None):
    base = os.environ.get("SONICJS_URL", "http://localhost:8787").rstrip("/")
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    req = urllib.request.Request(base + path, headers=headers, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, r.read().decode()
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()


def items_of(payload):
    """List responses are expected as {"data": [...]}; also accept a bare list."""
    if isinstance(payload, list):
        return payload
    return payload.get("data", payload.get("items", []))


def title_of(item):
    # title may be top level or nested inside "data" depending on the response shape
    return item.get("title") or (item.get("data") or {}).get("title")


def fetch_id_to_title(collection, token, page_size=100):
    result, offset = {}, 0
    while True:
        status, text = get(f"/api/{collection}?limit={page_size}&offset={offset}", token)
        if not 200 <= status < 300:
            sys.exit(f"GET /api/{collection} failed: {status} {text}")
        items = items_of(json.loads(text))
        new = {it["id"]: title_of(it) for it in items if it["id"] not in result}
        if not new:  # empty page, or the server ignored offset and repeated itself
            break
        result.update(new)
        offset += len(items)
        if len(items) < page_size:
            break
    missing = [i for i, t in result.items() if not t]
    if missing:
        print(f"warning: {len(missing)} item(s) in {collection} have no title: {missing[:5]}", file=sys.stderr)
    return result


load_dotenv()
token = login()

for collection in ("habitats", "zones", "attributes"):
    mapping = fetch_id_to_title(collection, token)
    out = f"{collection}.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(mapping, f, indent=2, ensure_ascii=False)
    print(f"wrote {out}: {len(mapping)} entries")