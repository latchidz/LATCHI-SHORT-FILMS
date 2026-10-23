# 🔒 CHAR_AMIN (V3 OFFICIAL) — القفل الرسمي الدائم لشخصية «أمين»

> **اسم الشخصية:** أمين  
> **صاحب الوجه الحقيقي:** **إسكندر خنتوش** (العميل نفسه)  
> **الدور:** 🎬 **البطل الدائم** في جميع الأفلام القصيرة والمسلسلات القادمة (`SOCIAL_DRAMA`)  
> **الإصدار المعتمد رسمياً:** **V3 — النظارة الأولى الزمردية الذهبية بدون إطار (`Rimless Emerald-Gold Signature`)**  
> **حالة الاعتماد:** 🔒 **مقفول نهائياً بنسبة 100% (بأمر العميل — هو المرجع الأساسي الوحيد المعتمد من الآن فصاعداً)**

---

## ⚡ القاعدة الذهبية الأولى (من الآن فصاعداً)

1. **نخدم دائماً وبالأصل بهذا المرجع الجديد (V3 النظارة الأولى الزمردية الذهبية)** الموجود في جذر `00_CHARACTERS/AMIN/` وفي بطاقات القفل الجاهزة داخل `01_SCENE_LOCK_CARDS_9x16/`.
2. **المراجع القديمة (بدون نظارات V1/V2) + النظارة الثانية السوداء المستطيلة (`90%`)** مخبّأة ومحفوظة بالكامل في مكان واحد منفصل داخل **`99_RESERVE_BACKUP/`** كاحتياط فقط — **ممنوع استعمالها تلقائياً** إلا إذا طلب العميل ذلك صراحةً بالاسم.
3. **ممنوع منعاً باتاً:** توليد أجساد بدون رأس أو قصّ ولصق الرؤوس بالـ Python، وممنوع أي تنعيم أو فلترة تجميلية للبشرة (`Zero Beautification / Raw 35mm Skin Texture`).

---

## 📁 هيكل مجلد `00_CHARACTERS/AMIN/`

| المسار | الوظيفة |
|---|---|
| **`CHAR_AMIN_MASTER_SHEET.png`** | **ورقة المرجع الرئيسية المعتمدة (`16:9` · 8 لوحات)** لأمين بالنظارة الأولى الزمردية الذهبية بدون إطار |
| `CHAR_AMIN_MASTER_SHEET.jpg` / `_preview.jpg` | نسخ خفيفة للرفع السريع والمعاينة على الهاتف وGoogle Flow |
| **`PROP_GLASSES_01_EMERALD_GOLD.jpg`** | مرجع الماكرو الدقيق للنظارة الرسمية (لقفل شكل العدسة الزمردية المتدرجة بدون إطار والمفصل الذهبي والذراع الأسود اللامع) |
| **`01_SCENE_LOCK_CARDS_9x16/`** | **سرّ تطابق الـ 100% في المشاهد العمودية (`9:16`):** بطاقتا القفل الجاهزتان (`768×1376`) بنفس الطريقة التي أنتجت المشهد التجريبي 1 و2 |
| `02_APPROVED_BENCHMARKS_100PCT/` | المشهدان التجريبيان المعتمدان من العميل (`BENCHMARK_01_CAFE_TERRACE_100PCT.png` و`BENCHMARK_02_LUXURY_CAR_SMILE.png`) كمعيار بصري قياسي |
| **`99_RESERVE_BACKUP/`** | **خزنة الاحتياط المنفصلة:** تضم `01_OLD_REFERENCES_NO_GLASSES/` (كل مراجع V1 وV2 القديمة) + `02_SECOND_GLASSES_MATTE_BLACK_90PCT/` (النظارة الثانية السوداء المستطيلة ومشاهديها) |

---

## 🏆 السرّ التقني المحفوظ: كيفاش تخدمت المشاهد التجريبية 1 و2 بنسبة تطابق 100%؟

لتوليد أي مشهد عمودي `9:16` يظهر فيه أمين مطابقاً لوجه إسكندر الحقيقي بنسبة **100%** (مثل `BENCHMARK_01_CAFE_TERRACE_100PCT.png` و`BENCHMARK_02_LUXURY_CAR_SMILE.png`)، اتبع هذه الخطوات حرفياً دون تغيير:

### 1️⃣ اختيار بطاقة الإدخال العمودية (`images[0]` مقاس `768×1376` نسبة `9:16`)
لا تمرر ورقة `16:9` أفقية مباشرة كـ `images[0]` عند توليد مشهد عمودي `9:16` (لأن الموديل يورث النسبة الأفقية أو يصغّر ملامح الوجه). بدلاً من ذلك، مرّر إحدى البطاقتين الجاهزتين في `01_SCENE_LOCK_CARDS_9x16/` كـ **`images[0]`** دائماً:
- **للمشاهد الجادة / الهادئة / الدرامية / الحوارية (طريقة المشهد التجريبي 1 — الأقوى 100%):**
  مرّر `01_SCENE_LOCK_CARDS_9x16/AMIN_9x16_LOCK_CARD_01_SERIOUS_NEUTRAL.png` كـ `images[0]`.
- **لمشاهد الابتسامة / الفرح / النجاح (طريقة المشهد التجريبي 2):**
  مرّر `01_SCENE_LOCK_CARDS_9x16/AMIN_9x16_LOCK_CARD_02_SMILING_WARM.png` كـ `images[0]`.
- **إذا ظهر مع أمين ممثل ثانٍ في نفس الكادر (مثل يوسف):**
  اجعل بطاقة أمين `9:16` هي `images[0]` (لقفل مقاس الكادر `768×1376` وقفل وجه أمين 100%)، ومرّر ورقة الشخصية الثانية كـ `images[1]`.

### 2️⃣ بصمة الهوية والنظارة الإلزامية في البرومبت (`IDENTITY + EYEWEAR LOCK`)
انسخ هذا القفل النصي حرفياً في بداية برومبت `generate_image` (`offer_options: false`):

```text
Vertical 9:16 raw 35mm live-action cinematic film still, shot on ARRI Alexa Mini LF with Cooke S4 50mm prime lens, natural film grain, zero AI skin smoothing, zero beauty filters.

CHARACTER LOCK (100% EXACT SAME REAL MAN AS IMAGE 1 — AMIN):
Preserve the exact unfiltered North African / Algerian facial bone structure, skin pores, slight cheek moles, straight nose with slightly rounded tip, full natural lips, short ~1cm neatly trimmed black beard connected to mustache (lighter on cheeks, denser on chin), and clean high skin-fade haircut with short textured dark hair on top from Image 1.

SIGNATURE EYEWEAR LOCK (EXACT RIMLESS SUNGLASSES FROM IMAGE 1):
He wears the exact rimless octagonal-rectangular sunglasses shown in Image 1: frameless emerald-teal dark gradient lenses (darker deep green-charcoal at top fading slightly lighter toward bottom), delicate polished gold nose bridge, ornate gold spear-point temple hinges mounted directly into the lens edges, and sleek glossy black temple arms resting naturally over his ears. Zero thick rims, zero aviator wireframes.
```

### 3️⃣ قاعدة التعبير والابتسامة والنظرة (`EXPRESSION & GAZE LOCK`)
- **في المشاهد الهادئة / الجادة (أسلوب المشهد الأول 100%):**
  اطلب زاوية `3/4` أو أمامية طبيعية مع نظرة خارج عدسة الكاميرا (`looking slightly off-camera, zero direct lens eye-contact`) وفم مسترخٍ مغلق أو شبه مغلق بهدوء ووقار (`calm, composed, confident neutral expression, relaxed lips`).
- **في مشاهد الابتسامة (أسلوب المشهد الثاني):**
  اطلب ابتسامة طبيعية حقيقية غير مبالغ فيها (`warm, natural, relaxed authentic smile matching the top smiling portraits in Image 1 — upper teeth gently visible, relaxed lower lip, NEVER an exaggerated wide-open mouth grin`).

---

## 📋 سجل التحديثات الرسمية

| التاريخ | الحدث |
|---|---|
| 21/10/2026 | إنشاء المرجع الأول V1 بدون نظارات (محفوظ الآن في `99_RESERVE_BACKUP/01_OLD_REFERENCES_NO_GLASSES/`) |
| 22/10/2026 | إضافة مراجع V2 وتعابير الوجه الحقيقية لفيلم «الشدة تبيّن الرجال» (محفوظة في `99_RESERVE_BACKUP/01_OLD_REFERENCES_NO_GLASSES/`) |
| 23/10/2026 | **اختبار النظارتين V3 واعتماد العميل الرسمي للنظارة الأولى الزمردية الذهبية (`CHAR_AMIN_MASTER_SHEET.png`) + تثبيت طريقة المشهد التجريبي 1 و2 (100%) كمعيار دائم، ونقل المراجع القديمة والنظارة الثانية إلى `99_RESERVE_BACKUP/`** |
