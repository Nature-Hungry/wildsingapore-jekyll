import json
import os
import sys
from utils import login, post, load_dotenv

from concurrent.futures import ThreadPoolExecutor

habitats = [
 "mangrove"
, "mudflat"
, "coastal forest"
, "rocky shore"
, "sandy shore"
, "seagrass meadow"
, "coral rubble"
, "coral reef"
, "native forest"
, "exotic forest"
, "grassland"
, "scrubland"
, "urban park"
, "built-up"
, "freshwater swamp"
, "freshwater marsh"
]
zones = [
    "terrestrial"
,"freshwater"
,"intertidal"
, "marine"
]

load_dotenv()

token = login()
for h in habitats:
    status, text = post("/api/habitats",{"title":h},token=token)
    if status == 404:
        continue
    if not 200 <= status < 300:
        print(text, file=sys.stderr)
        sys.exit("first item failed; fix the payload/auth before continuing")
        break

    print(f"insert {h} ok")

for z in zones:
    status, text = post("/api/zones", {"title":z},token=token)
    if status == 404:
        continue
    if not 200 <= status < 300:
        print(text, file=sys.stderr)
        sys.exit("first item failed; fix the payload/auth before continuing")
        break

    print(f"insert {z} ok")