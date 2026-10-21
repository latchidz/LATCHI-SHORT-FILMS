# -*- coding: utf-8 -*-
"""يدمج الصور داخل ملفات Markdown: يستبدل {{IMAGE:مسار|وصف}} بصورة مدمجة بالحجم الكامل.
الاستعمال: python3 tools/embed_md.py <ملف.md>"""
import re, base64, io, sys, os
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = sys.argv[1] if len(sys.argv) > 1 else None
if not path or not os.path.isfile(os.path.join(ROOT, path)):
    sys.exit("الملف غير موجود")

src = open(os.path.join(ROOT, path), encoding="utf-8").read()

def embed(m):
    img_path, caption = m.group(1).strip(), m.group(2).strip()
    im = Image.open(os.path.join(ROOT, img_path)).convert("RGB")
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=92)  # الحجم الكامل 1376×768 بجودة عالية
    b64 = base64.b64encode(buf.getvalue()).decode()
    return f"**{caption}**\n\n![{caption}](data:image/jpeg;base64,{b64})"

out, n = re.subn(r"\{\{IMAGE:([^|]+)\|([^}]+)\}\}", embed, src)
open(os.path.join(ROOT, path), "w", encoding="utf-8").write(out)
print(f"✓ {path}: دُمجت {n} صورة — الحجم النهائي {os.path.getsize(os.path.join(ROOT,path))//1024} KB")
