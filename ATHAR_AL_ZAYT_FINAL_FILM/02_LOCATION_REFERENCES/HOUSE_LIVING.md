# مرجع الموقع 5 — غرفة جلوس بيت ياسين (HOUSE LIVING ROOM)

## الوصف المقفل
- غرفة جلوس صغيرة **نظيفة ومتواضعة محدودة الإمكانيات** (ليست قصراً وليست مهجورة).
- كنبة بسيطة بأغطية كروشيهية + كرسيان بسيطان + **طاولة صغيرة واطئة** في الوسط.
- سجادة بنقوش هادئة، ستارة بسيطة على نافذة، مدخل مطبخ صغير في الخلفية.
- **الإضاءة المسائية الثابتة:** مصباح سقفي دافئ + إضاءة جانبية — متسقة في كل مشاهد الزيارة (SC12–SC21).
- تفاصيل إنسانية: طقم شاي صغير على الطاولة، صور عائلية صغيرة **بلا نص مقروء**، لعبة الطفلة على السجادة.

## PROMPT — 16:9 (نسخ جاهز)
```
Photorealistic film still, wide shot of a small modest but clean Algerian home living room at evening. A simple sofa with crocheted covers, two simple chairs, a small low wooden table in the middle with a small tea set, a patterned modest rug, simple curtained window, a small kitchen doorway in the background, tiny framed family photos on the wall without readable text, a small child's cloth toy on the rug. Warm ceiling lamp and warm side lamp lighting, cozy realistic modest atmosphere, no people. Natural depth of field. Photorealistic live-action film still, no cartoon, no illustration, no watermark, no readable text.
FORMAT: Horizontal landscape 16:9 only, cinematic widescreen framing. Never vertical 9:16, never portrait, never square. Do not crop the image into a vertical frame.
```

## قفل الاستمرارية
- مواضع الأثاث ثابتة: الكنبة خلفية رئيسية، الطاولة وسط، مدخل المطبخ خلفية يسار.
- **مكان تسليم المال (SC17):** قرب الطاولة الصغيرة — ياسين واقف أمام الحاج الجالس، الأم على الكنبة.
- لعبة الطفلة على السجادة قرب الكنبة في كل مشاهد المساء.

## 📍 خريطة التثبيت المقفلة (SC16 → SC27) — مطلب العميل 17 أكتوبر
**القاعدة: زاوية الكاميرا تتغير (يمين/يسار/فوق/تحت) لكن مواضع الشخصيات والأثاث لا تتغير أبداً.**
- **الحاج:** جالس الجهة اليسرى من الكنبة — لا يتحرك (ينهض فقط للانصراف SC26-27).
- **الأم:** جالسة الطرف الأيمن من الكنبة — لا تتحرك (الأخت تلعب على السجادة قربها SC19/SC25).
- **أمين:** جالس على الكرسي البسيط يمين الكنبة — لا يتحرك (ينهض للمصافحة SC26).
- **ياسين:** واقف وسط الغرفة خلف طاولة الشاي، مواجه للكنبة — لا يتحرك (خطوة أمامية واحدة فقط لتسليم المال SC21، ويجلس بجوار أمه في SC25).
- **طريقة التنفيذ:** `SC16_IMAGE_A_WIDE.png` هي **اللقطة الأم** — تُمرَّر ضمن `images` في كل توليد جديد لغرفة الجلوس + يُكتب نص المواضع صراحة في كل برومبت.

## ⭐ مرجع الصالون بالتثبيت — `HOUSE_LIVING_BLOCKING.png` (مطلب العميل)
صورة مرجعية واحدة تجمع **الغرفة + الشخصيات الأربع في مواضعها المقفلة** بوضعية محايدة هادئة (مرجع للعميل يرفعه في Flow مع كل مشاهد غرفة الجلوس SC16-SC27): الحاج جالس يسار الكنبة • الأم يمين الكنبة • أمين على الكرسي يمين • ياسين واقف وسط خلف طاولة الشاي. مبنية على اللقطة الأم SC16_A — نفس الأثاث والإضاءة والمواضع.
