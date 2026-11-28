#!/usr/bin/env python3
"""Delete EVERY item in one SonicJS collection (default: entries). This cannot be undone.

Run next to utils.py and migrate_entries.py:

    python3 delete_entries.py --dry-run          # list what would be deleted, delete nothing
    python3 delete_entries.py                    # asks you to type the collection name first
    python3 delete_entries.py --yes              # no prompt (scripts)
    python3 delete_entries.py --collection authors

Uses GET /api/<collection> to list ids and DELETE /api/<collection>/<id> for each item.
"""
import argparse
import sys
import time
from concurrent.futures import ThreadPoolExecutor

from migrate_entries import api, fetch_all, fv  # keep-alive connections + 429 retry live there
from utils import load_dotenv, login


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--collection", default="entries")
    ap.add_argument("--dry-run", action="store_true", help="only list, delete nothing")
    ap.add_argument("--yes", action="store_true", help="skip the confirmation prompt")
    ap.add_argument("--concurrency", type=int, default=8)
    args = ap.parse_args()

    load_dotenv()
    token = login()

    items = fetch_all(args.collection, token)
    print(f'"{args.collection}" has {len(items)} items.')
    if not items:
        return
    for it in items[:5]:
        print(f"  e.g. {it['id']}  {fv(it, 'slug') or ''}  {fv(it, 'title') or fv(it, 'name') or ''}")
    if args.dry_run:
        print("dry run: nothing deleted")
        return

    if not args.yes:
        base = __import__("os").environ.get("SONICJS_URL", "http://localhost:8787")
        print(f"\nThis will permanently delete all {len(items)} items from {base}")
        if input(f'Type the collection name ("{args.collection}") to continue: ').strip() != args.collection:
            sys.exit("cancelled")

    def delete(it):
        status, text = api("DELETE", f"/api/{args.collection}/{it['id']}", token)
        # 404 = already gone, which is fine on a rerun
        return None if 200 <= status < 300 or status == 404 else {"id": it["id"], "status": status, "body": text[:200]}

    failed, done, t0 = [], 0, time.time()
    with ThreadPoolExecutor(max_workers=args.concurrency) as pool:
        for res in pool.map(delete, items):
            done += 1
            if res:
                failed.append(res)
            if done % 100 == 0 or done == len(items):
                print(f"  {done}/{len(items)} processed, {len(failed)} failed", flush=True)

    print(f"deleted {len(items) - len(failed)}/{len(items)} in {time.time() - t0:.0f}s")
    if failed:
        print(failed[:5], file=sys.stderr)
        sys.exit(1)

    left = fetch_all(args.collection, token)
    print(f'check: "{args.collection}" now lists {len(left)} items' + ("" if not left else " (soft-deleted items may still be listed; look at the admin)"))


if __name__ == "__main__":
    main()