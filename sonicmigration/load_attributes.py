#!/usr/bin/env python3
"""Bulk-create entries in the "attributes" collection, one POST per item.

Usage:
  SONICJS_URL=https://your-worker.example.com \
  SONICJS_EMAIL=you@example.com SONICJS_PASSWORD=... \
  python3 load_attributes.py attributes.json

  DRY_RUN=1 python3 load_attributes.py attributes.json   # print only

Optional env: COLLECTION (default "attributes"), CONCURRENCY (default 4),
              SONICJS_TOKEN (skip login), ENDPOINT (override path)
Standard library only.
"""
import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor
from utils import login, post, load_dotenv




load_dotenv()

BASE = os.environ.get("SONICJS_URL", "http://localhost:8787").rstrip("/")
COLLECTION = os.environ.get("COLLECTION", "attributes")
CONCURRENCY = int(os.environ.get("CONCURRENCY", "4"))
DRY = bool(os.environ.get("DRY_RUN"))

if len(sys.argv) < 2:
    sys.exit("usage: python3 load_attributes.py attributes.json")
with open(sys.argv[1], encoding="utf-8") as f:
    rows = json.load(f)

# Both URL styles appear in the SonicJS docs, so probe them in order.
candidates = (
    [os.environ["ENDPOINT"]]
    if os.environ.get("ENDPOINT")
    else [f"/api/{COLLECTION}/content", f"/api/{COLLECTION}"]
)


if DRY:
    print(f"DRY RUN: would POST {len(rows)} items to {BASE}{candidates[0]}")
    print("first body:", json.dumps(rows[0]))
    sys.exit(0)

token = login()

# Find the working endpoint using the first item.
path = None
for c in candidates:
    status, text = post(c, rows[0], token)
    if status == 404:
        continue
    path = c
    print(f"endpoint: {c} -> first item {status}")
    if not 200 <= status < 300:
        print(text, file=sys.stderr)
        sys.exit("first item failed; fix the payload/auth before continuing")
    break
if path is None:
    sys.exit(f"no endpoint found, tried: {', '.join(candidates)}")


def create(row):
    try:
        status, text = post(path, row, token)
    except Exception as e:  # network error
        return {"slug": row["slug"], "error": str(e)}
    if 200 <= status < 300:
        return None
    return {"slug": row["slug"], "status": status, "body": text}


with ThreadPoolExecutor(max_workers=CONCURRENCY) as pool:
    results = list(pool.map(create, rows[1:]))

failed = [r for r in results if r]
ok = len(rows) - len(failed)
print(f"created {ok}/{len(rows)}, failed {len(failed)}")
if failed:
    print(json.dumps(failed, indent=2), file=sys.stderr)
    sys.exit(1)