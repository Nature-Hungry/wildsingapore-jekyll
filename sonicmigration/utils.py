import json
import os
import sys
import urllib.error
import urllib.request


def post(path, body, token=None):
    """POST JSON; returns (status, response_text). Never raises on HTTP errors."""
    base = os.environ.get("SONICJS_URL", "http://localhost:8787").rstrip("/")
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    print(base + path)
    req = urllib.request.Request(
        base + path, data=json.dumps(body).encode(), headers=headers, method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, r.read().decode()
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()


def login():
    if os.environ.get("SONICJS_TOKEN"):
        return os.environ["SONICJS_TOKEN"]
    status, text = post(
        "/auth/login",
        {"email": os.environ.get("SONICJS_EMAIL"), "password": os.environ.get("SONICJS_PASSWORD")},
    )
    if status != 200:
        sys.exit(f"login failed: {status} {text}")
    token = json.loads(text).get("token")
    if not token:
        sys.exit("login response had no token")
    return token

def load_dotenv(path=".env"):
    """Minimal .env reader: KEY=VALUE lines; real environment variables win."""
    if not os.path.isfile(path):
        return
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            key = key.removeprefix("export ").strip()
            value = value.strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
                value = value[1:-1]
            os.environ.setdefault(key, value)