#!/usr/bin/env python3
"""Automated Seedance Video Generator for Episode 01 (Zouzou & The Bouncy Ice Cream)."""
import base64, json, os, re, sys, time, urllib.request, urllib.error

MEMO_PATH = "/home/user/WORKSPACE_MEMO_PRIVATE.md"
with open(MEMO_PATH, encoding="utf-8") as f:
    m = re.search(r"`ARK_API_KEY`:\s*`([^`]+)`", f.read())
    if not m:
        raise RuntimeError("ARK_API_KEY not found in WORKSPACE_MEMO_PRIVATE.md")
    ARK_KEY = m.group(1).strip()

BASE_URL = "https://ark.ap-southeast.bytepluses.com/api/v3/contents/generations/tasks"
EP_DIR = "/home/user/ABSURD_3D_CARTOON_SHORTS/EPISODE_01_ZOUZOU_RUBBER_ICECREAM"
OUT_DIR = os.path.join(EP_DIR, "05_GENERATED_VIDEOS_MP4")
os.makedirs(OUT_DIR, exist_ok=True)

CANDIDATE_MODELS = [
    "seedance-1-5-pro-251215",
    "seedance-1-0-pro-250528",
    "dreamina-seedance-2-0-260128",
    "dreamina-seedance-2-0-fast-260128",
    "seedance-1-0-pro-fast-251015",
]

def to_data_uri(path):
    with open(path, "rb") as fp:
        return "data:image/png;base64," + base64.b64encode(fp.read()).decode("ascii")

def pick_active_model():
    for mid in CANDIDATE_MODELS:
        payload = json.dumps({
            "model": mid,
            "content": [{"type": "text", "text": "test"}],
            "duration": 999
        }).encode("utf-8")
        req = urllib.request.Request(
            BASE_URL, data=payload,
            headers={"Authorization": f"Bearer {ARK_KEY}", "Content-Type": "application/json"},
            method="POST"
        )
        try:
            urllib.request.urlopen(req, timeout=15)
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="replace")
            if "ModelNotOpen" not in body and "InvalidEndpointOrModel.NotFound" not in body:
                print(f"Active Seedance model detected: {mid}")
                return mid
    return None

if __name__ == "__main__":
    active = pick_active_model()
    if not active:
        print("NO_ACTIVE_MODEL_YET")
        sys.exit(2)
    print(f"Ready to generate with: {active}")
