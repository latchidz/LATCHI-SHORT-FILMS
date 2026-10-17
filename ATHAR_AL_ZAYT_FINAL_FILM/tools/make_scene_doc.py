# -*- coding: utf-8 -*-
"""مولّد مستند المشهد (HTML) — نفس محتوى SCxx_FLOW_PROMPT.md لكن بصيغة تعرض الصور المدمجة مضمونة.
يقرأ قالب الـ md (بعلامات {{IMAGE:مسار|اسم|وصف}}) وينتج SCxx_FLOW_PROMPT.html
الاستعمال: python3 tools/make_scene_doc.py <رقم المشهد>
"""
import re, base64, io, os, sys
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
n = int(sys.argv[1])
md_path = os.path.join(ROOT, "04_FLOW_VIDEO_PROMPTS", f"SC{n:02d}_FLOW_PROMPT.md")
md = open(md_path, encoding="utf-8").read()

title = re.search(rf"# SCENE {n:02d} — (.+)", md).group(1).strip()
subtitle = re.search(r"\*\*(فيلم[^*]+)\*\*", md)
subtitle = subtitle.group(1) if subtitle else ""

# ملاحظات قسم اللقطات (أسطر >)
shots_note = "<br>".join(l.strip("> ").strip() for l in md.splitlines()
                         if l.startswith("> ") and "**طريقة التحميل**" not in l and l.strip("> ").strip())

# اللقطات
shot_marks = re.findall(r"\{\{IMAGE:([^|]+)\|([^|]+)\|([^}]+)\}\}", md)

def img_data(path):
    im = Image.open(os.path.join(ROOT, path.strip())).convert("RGB")
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=92)
    return base64.b64encode(buf.getvalue()).decode()

shots_html = ""
for i, (path, name, caption) in enumerate(shot_marks, 1):
    b64 = img_data(path)
    fname = name.strip() + ".jpg"
    shots_html += f'''
<div class="shot">
  <div class="shot-head"><span class="num">{i}</span><div class="cap"><b>{caption.strip()}</b><code>{name.strip()}.png</code></div>
  <a class="dl" download="{fname}" href="data:image/jpeg;base64,{b64}">⬇ تحميل الصورة</a></div>
  <img src="data:image/jpeg;base64,{b64}" alt="{caption.strip()}">
</div>'''

# البرومبت الرئيسي (أول كتلة كود بعد 📋)
m = re.search(r"## 📋[^\n]*\n(.*?)```(?:\w*)\n(.*?)\n```", md, re.S)
prompt_lead = m.group(1).strip()
prompt = m.group(2).strip()

# النيجاتيف (كتلة الكود بعد 🚫)
m2 = re.search(r"## 🚫[^\n]*\n(.*?)```(?:\w*)\n(.*?)\n```", md, re.S)
neg_lead = m2.group(1).strip().strip("*()")
negative = m2.group(2).strip() if m2 else ""

# آخر إطار
m3 = re.search(r"## 🔗[^\n]*\n(.+?)(?=\n## |\n---|\Z)", md, re.S)
lastframe = m3.group(1).strip() if m3 else ""

# فحص سريع
m4 = re.search(r"## ✅[^\n]*\n(.+?)(?=\n## |\n---|\Z)", md, re.S)
check = m4.group(1).strip() if m4 else ""

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>المشهد {n:02d} — {esc(title)} | آثار الزيت</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#f6f7f9;color:#1f2937;font-family:"Segoe UI",Tahoma,"Noto Naskh Arabic",sans-serif;line-height:1.85}}
.page{{max-width:900px;margin:0 auto;background:#fff;min-height:100vh;box-shadow:0 0 40px rgba(0,0,0,.08)}}
.inner{{padding:36px 46px 60px}}
h1{{font-size:1.6rem;color:#111827;border-bottom:3px solid #4f7cff;padding-bottom:12px}}
h1 small{{color:#6b7280;font-size:.85rem;font-weight:400;display:block;margin-top:4px}}
h2{{font-size:1.2rem;margin:38px 0 14px;color:#1e40af}}
.note{{background:#eef4ff;border:1px solid #c7d7fe;border-radius:10px;padding:12px 18px;font-size:.88rem;color:#374151;margin-bottom:18px}}
.shot{{border:1px solid #e5e7eb;border-radius:14px;overflow:hidden;margin-bottom:24px}}
.shot-head{{display:flex;align-items:center;gap:12px;padding:12px 16px;background:#f9fafb;border-bottom:1px solid #e5e7eb;flex-wrap:wrap}}
.num{{width:30px;height:30px;border-radius:9px;background:linear-gradient(135deg,#4f7cff,#8b5cf6);color:#fff;display:grid;place-items:center;font-weight:800;flex-shrink:0}}
.cap b{{font-size:.95rem}} .cap code{{color:#6b7280;font-size:.78rem;direction:ltr;display:block}}
.dl{{margin-inline-start:auto;background:linear-gradient(135deg,#059669,#10b981);color:#fff;text-decoration:none;font-weight:700;font-size:.85rem;padding:8px 18px;border-radius:9px}}
.dl:hover{{filter:brightness(1.1)}}
.shot img{{width:100%;display:block}}
.pbox{{position:relative;background:#0f172a;border-radius:12px;overflow:hidden}}
.copy{{position:absolute;top:10px;inset-inline-end:10px;z-index:2;background:linear-gradient(135deg,#4f7cff,#8b5cf6);color:#fff;border:0;font-weight:700;font-family:inherit;font-size:.83rem;padding:8px 18px;border-radius:9px;cursor:pointer}}
.copy:hover{{filter:brightness(1.12)}}
pre{{padding:22px 20px;font-family:Consolas,"Courier New",monospace;font-size:.85rem;line-height:1.9;white-space:pre-wrap;word-break:break-word;color:#dbeafe;direction:ltr;text-align:left}}
.lead{{font-size:.85rem;color:#6b7280;margin:-6px 0 10px}}
.sect{{background:#f9fafb;border:1px solid #e5e7eb;border-radius:12px;padding:14px 20px;font-size:.93rem;color:#374151}}
.hr{{border:0;border-top:1px solid #e5e7eb;margin:34px 0}}
.tip{{margin-top:34px;background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:12px 18px;font-size:.85rem;color:#92400e}}
@media (max-width:640px){{.inner{{padding:22px 18px 40px}}}}
@media print{{.copy{{display:none}} .dl{{display:none}} body{{background:#fff}}}}
</style></head><body><div class="page"><div class="inner">

<h1>المشهد {n:02d} — {esc(title)}<small>{esc(subtitle)}</small></h1>

<h2>🎬 لقطات المشهد</h2>
<div class="note">{shots_note}</div>
{shots_html}
<hr class="hr">

<h2>📋 برومبت Google Flow — جاهز للنسخ</h2>
<div class="pbox"><button class="copy" onclick="copyText('pr',this)">📋 نسخ البرومبت</button>
<pre id="pr">{esc(prompt)}</pre></div>

<h2>🚫 Negative Prompt</h2>
<p class="lead">{esc(neg_lead)}</p>
<div class="pbox"><button class="copy" onclick="copyText('ng',this)">📋 نسخ</button>
<pre id="ng">{esc(negative)}</pre></div>
<hr class="hr">

<h2>🔗 آخر إطار — للربط بالمشهد التالي</h2>
<div class="sect">{esc(lastframe)}</div>

<h2>✅ فحص سريع قبل التوليد</h2>
<div class="sect">{esc(check)}</div>

<div class="tip">💡 الصور مدمجة بدقتها الكاملة (1376×768) — حمّلها بأزرار «تحميل الصورة» أو كليك يمين ← حفظ الصورة باسم، ثم ارفعها في Google Flow بترتيب أرقامها (1 = إطار البداية) والصق البرومبت.</div>

</div></div>
<script>
function copyText(id, btn) {{
  var txt = document.getElementById(id).textContent;
  function ok() {{ btn.textContent = "✓ تم النسخ"; setTimeout(function() {{ btn.textContent = "📋 نسخ البرومبت"; }}, 2000); }}
  function fb() {{
    var ta = document.createElement("textarea");
    ta.value = txt; document.body.appendChild(ta); ta.select();
    try {{ document.execCommand("copy"); ok(); }} catch (e) {{ alert("حدد النص يدوياً وانسخه"); }}
    document.body.removeChild(ta);
  }}
  if (navigator.clipboard && navigator.clipboard.writeText) {{ navigator.clipboard.writeText(txt).then(ok, fb); }} else fb();
}}
</script>
</body></html>'''

out = os.path.join(ROOT, "04_FLOW_VIDEO_PROMPTS", f"SC{n:02d}_FLOW_PROMPT.html")
open(out, "w", encoding="utf-8").write(html)
print(f"✓ 04_FLOW_VIDEO_PROMPTS/SC{n:02d}_FLOW_PROMPT.html ({os.path.getsize(out)//1024} KB) — لقطات: {len(shot_marks)}")
