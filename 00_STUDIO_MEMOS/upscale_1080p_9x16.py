#!/usr/bin/env python3
"""Center-crop to exact 9:16 aspect ratio and Lanczos-upscale/resize to 1080x1920."""
import sys
from PIL import Image

TARGET_W, TARGET_H = 1080, 1920
TARGET_RATIO = TARGET_W / TARGET_H  # 0.5625

for path in sys.argv[1:]:
    im = Image.open(path).convert("RGB")
    w, h = im.size
    ratio = w / h
    if abs(ratio - TARGET_RATIO) > 0.005:
        if ratio > TARGET_RATIO:
            new_w = int(round(h * TARGET_RATIO))
            left = (w - new_w) // 2
            im = im.crop((left, 0, left + new_w, h))
        else:
            new_h = int(round(w / TARGET_RATIO))
            top = (h - new_h) // 2
            im = im.crop((0, top, w, top + new_h))
    if im.size != (TARGET_W, TARGET_H):
        im = im.resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
    im.save(path, format="PNG", optimize=True, compress_level=9)
    print(f"1080x1920 9:16 ready: {path} -> {im.size}")
