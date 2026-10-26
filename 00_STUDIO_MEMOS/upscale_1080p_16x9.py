#!/usr/bin/env python3
"""Lossless-proportion 16:9 Horizontal Full HD (1920x1080) upscaler for LATCHI-SHORT-FILMS."""
import sys
from PIL import Image, ImageFilter

TARGET_W, TARGET_H = 1920, 1080
TARGET_RATIO = TARGET_W / TARGET_H  # 1.7777778


def upscale_to_1080p_16x9(in_path: str, out_path: str):
    im = Image.open(in_path).convert("RGB")
    w, h = im.size
    cur_ratio = w / h

    # Center-crop minimally (<0.8% if 1376x768 -> 1.7917 vs 1.7778) so ZERO stretching ever occurs
    if abs(cur_ratio - TARGET_RATIO) > 1e-4:
        if cur_ratio > TARGET_RATIO:
            new_w = int(round(h * TARGET_RATIO))
            x0 = (w - new_w) // 2
            im = im.crop((x0, 0, x0 + new_w, h))
        else:
            new_h = int(round(w / TARGET_RATIO))
            y0 = (h - new_h) // 2
            im = im.crop((0, y0, w, y0 + new_h))

    if im.size != (TARGET_W, TARGET_H):
        im = im.resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
        im = im.filter(ImageFilter.UnsharpMask(radius=0.9, percent=70, threshold=3))

    im.save(out_path, format="PNG", compress_level=1)
    return im.size


if __name__ == "__main__":
    for p in sys.argv[1:]:
        sz = upscale_to_1080p_16x9(p, p)
        print(f"1080p 16:9 ready: {p} -> {sz}")
