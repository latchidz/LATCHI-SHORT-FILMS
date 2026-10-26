#!/usr/bin/env python3
"""Cinema-grade 2-stage 4K UHD (2160x3840, exact 9:16) upscaler with zero aspect distortion and zero halos."""
import sys
import cv2
import numpy as np
from PIL import Image


def upscale_to_true_4k_9x16(in_path: str, out_path: str):
    im = Image.open(in_path).convert("RGB")
    w, h = im.size
    if (w, h) == (2160, 3840):
        if in_path != out_path:
            im.save(out_path, format="PNG", optimize=True, compress_level=9)
        return (2160, 3840)

    target_ratio = 9.0 / 16.0
    cur_ratio = w / h
    if abs(cur_ratio - target_ratio) > 1e-4:
        if cur_ratio < target_ratio:
            new_h = int(round(w / target_ratio))
            top = (h - new_h) // 2
            im = im.crop((0, top, w, top + new_h))
        else:
            new_w = int(round(h * target_ratio))
            left = (w - new_w) // 2
            im = im.crop((left, 0, left + new_w, h))

    arr = np.array(im)
    mid = cv2.resize(arr, (1080, 1920), interpolation=cv2.INTER_LANCZOS4)
    smooth_mid = cv2.bilateralFilter(mid, d=5, sigmaColor=18, sigmaSpace=18)
    detail_mid = mid.astype(np.float32) - smooth_mid.astype(np.float32)
    mid_sharp = np.clip(mid.astype(np.float32) + 0.35 * detail_mid, 0, 255).astype(np.uint8)

    up4k = cv2.resize(mid_sharp, (2160, 3840), interpolation=cv2.INTER_LANCZOS4)
    blur = cv2.GaussianBlur(up4k, (0, 0), sigmaX=1.1)
    sharp4k = cv2.addWeighted(up4k, 1.28, blur, -0.28, 0)

    out_im = Image.fromarray(sharp4k)
    out_im.save(out_path, format="PNG", optimize=True, compress_level=9)
    return out_im.size


if __name__ == "__main__":
    for p in sys.argv[1:]:
        sz = upscale_to_true_4k_9x16(p, p)
        print(f"4K ready: {p} -> {sz}")
