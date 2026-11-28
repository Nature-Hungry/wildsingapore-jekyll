#!/usr/bin/env python3
"""Find out which request shape SonicJS actually stores. Creates 3 throw-away test entries,
reads each back, reports where the extra fields ended up, then deletes the test entries.

    python3 probe_create.py            (run next to utils.py and migrate_entries.py)
"""
import json
import time

from migrate_entries import api, extract_id, fetch_all, fv
from utils import load_dotenv, login

load_dotenv()
token = login()
stamp = int(time.time())

authors = fetch_all("authors", token)[:1]
extra = {"kingdom": "Animalia", "family": "ProbeFamily", "genus": "Probegenus", "coverimg": "https://example.com/probe.jpg"}
if authors:
    extra["authors"] = [authors[0]["id"]]
core = {"content": "probe body"}

variants = [
    ("A  flat body        -> POST /api/entries", "/api/entries", {"title": f"Probe A {stamp}", "slug": f"zz-probe-a-{stamp}", **core, **extra}),
    ("B  data wrapper     -> POST /api/entries", "/api/entries",
     {"title": f"Probe B {stamp}", "slug": f"zz-probe-b-{stamp}", "data": {**core, **extra}}),
    ("C  flat body        -> POST /api/collections/entries/content", "/api/collections/entries/content",
     {"title": f"Probe C {stamp}", "slug": f"zz-probe-c-{stamp}", **core, **extra}),
]


def where(item):
    top = item if isinstance(item, dict) else {}
    data = top.get("data") if isinstance(top.get("data"), dict) else {}
    found = {k: ("top-level" if top.get(k) not in (None, "", []) else "in data" if data.get(k) not in (None, "", []) else "MISSING") for k in extra}
    return found


created = []
for label, path, body in variants:
    status, text = api("POST", path, token, body)
    print(f"\n{label}\n  POST status: {status}")
    if not 200 <= status < 300:
        print("  response:", text[:300])
        continue
    item_id = extract_id(text)
    if not item_id:  # fall back to finding it by slug
        for it in fetch_all("entries", token):
            if fv(it, "slug") == body["slug"]:
                item_id = it["id"]
    if not item_id:
        print("  could not find the created item")
        continue
    created.append((path, item_id))
    gstatus, gtext = api("GET", f"/api/entries/{item_id}", token)
    try:
        got = json.loads(gtext)
        got = got.get("data", got) if isinstance(got, dict) and isinstance(got.get("data"), dict) and "title" in got["data"] else got
    except ValueError:
        got = {}
    print("  stored fields:", json.dumps(where(got)))

print("\ncleaning up test entries...")
for _path, item_id in created:
    api("DELETE", f"/api/entries/{item_id}", token)
print("done. Use the shape whose fields are not MISSING (migrate_entries.py --shape flat|data, --endpoint PATH).")