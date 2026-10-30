# 🎯 دليل بطاقات القفل العمودية (`9:16`) وطريقة إنتاج المشهد التجريبي 1 و2 بنسبة 100%

يحتوي هذا المجلد على البطاقتين العموديتين (`768×1376` — نسبة `9:16` أصلية) المصممتين بـ `PIL.ImageOps.contain` (صفر مطّ أو تشويه للأبعاد) واللتين أعطتا تطابقاً بنسبة **100%** مع وجه إسكندر خنتوش (أمين) في الاختبار المعتمد:

1. **`AMIN_9x16_LOCK_CARD_01_SERIOUS_NEUTRAL.png`** (`768×1376`)
   - **الاستعمال:** جميع اللقطات الهادئة، الجادة، الدرامية، ولقطات الحوار والهيبة (مطابقة تماماً لطريقة **المشهد التجريبي الأول** `BENCHMARK_01_CAFE_TERRACE_100PCT.png` الذي اعتبره العميل الأقوى بنسبة **100%**).
   - **المحتوى:** بورتريه أمامي قريب + بورتريه جانبي يسار + بورتريه جانبي يمين + صورة ماكرو للنظارة الزمردية الذهبية بدون إطار + 4 زوايا كاملة للجسم (`Front, 3/4, Side, Back`).

2. **`AMIN_9x16_LOCK_CARD_02_SMILING_WARM.png`** (`768×1376`)
   - **الاستعمال:** جميع لقطات الابتسامة، الفرح، الترحيب، والنجاح (مطابقة تماماً لطريقة **المشهد التجريبي الثاني** `BENCHMARK_02_LUXURY_CAR_SMILE.png`).
   - **المحتوى:** بورتريه مبتسم بالنظارة الزمردية الذهبية (`3/4`) + صورة ابتسامة أمين الحقيقية الكاملة لقفل شكل الأسنان والخدود والذقن + بورتريه أمامي وجانبي + جسم أمامي و`3/4` + ماكرو النظارة الرسمية.

---

## 🧪 البرومبت المرجعي الكامل للمشهد التجريبي الأول (`100% Gold Standard`)

عند التوليد بـ `generate_image` (`offer_options: false`) مع تمرير `AMIN_9x16_LOCK_CARD_01_SERIOUS_NEUTRAL.png` في `images`:

```text
Vertical 9:16 raw 35mm live-action cinematic film still, shot on ARRI Alexa Mini LF with 50mm prime lens, shallow depth of field, natural film grain, zero AI skin smoothing, zero beauty filters.

CHARACTER LOCK (100% EXACT SAME REAL MAN AS IMAGE 1 — AMIN):
Medium close-up (chest-up, slight 3/4 angle) of the exact same Algerian man in his late twenties from Image 1, preserving 100% his authentic facial bone structure, natural skin pores, straight nose with slightly rounded tip, full natural lips, short ~1cm neatly trimmed black beard connected to mustache, and clean high skin-fade haircut with short textured dark hair on top.

SIGNATURE EYEWEAR LOCK (EXACT RIMLESS SUNGLASSES FROM IMAGE 1):
He wears the exact rimless octagonal-rectangular sunglasses from Image 1: frameless emerald-teal dark gradient lenses, delicate polished gold nose bridge, ornate gold spear-point temple hinges mounted directly into the lens edges, and sleek glossy black temple arms.

SCENE & ACTION:
[اكتب هنا وصف المكان واللباس والإضاءة والوضعية المطلوبة في المشهد الجديد — مع الحفاظ على نظرة خارج عدسة الكاميرا looking off-camera, zero direct lens eye-contact].
```

---

## 🧪 البرومبت المرجعي الكامل للمشهد التجريبي الثاني (`Smiling Gold Standard`)

عند التوليد بـ `generate_image` (`offer_options: false`) مع تمرير `AMIN_9x16_LOCK_CARD_02_SMILING_WARM.png` في `images`:

```text
Vertical 9:16 raw 35mm live-action cinematic film still, shot on ARRI Alexa Mini LF with 50mm prime lens, natural daylight, authentic skin pores, zero AI retouching.

CHARACTER & SMILE LOCK (100% EXACT SAME REAL MAN AS IMAGE 1 — AMIN):
Medium shot (waist-up, slight 3/4 turn) of the exact same Algerian man from Image 1 with his warm, natural, relaxed authentic smile matching the top smiling portraits in Image 1 (upper teeth gently visible, natural relaxed lower lip, authentic cheek lines, NEVER an exaggerated wide-open grin), preserving 100% his short ~1cm trimmed black beard, high skin-fade haircut, and exact rimless emerald-teal gradient sunglasses with polished gold bridge, gold spear hinges, and glossy black arms.

SCENE & ACTION:
[اكتب هنا وصف المكان واللباس والإضاءة والوضعية المطلوبة في المشهد الجديد — looking slightly off-camera toward another person, zero direct lens eye-contact].
```
