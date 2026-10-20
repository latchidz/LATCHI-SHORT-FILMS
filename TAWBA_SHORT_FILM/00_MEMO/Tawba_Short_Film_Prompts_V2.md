# وثيقة إنتاج «التوبة وحسن الخاتمة» — النسخة المعدّلة V2
**الصيغة:** 9:16 عمودي (1080×1920) • **المدة:** 10 مشاهد × 10 ثواني = 100 ثانية • **الواقعية:** لايف أكشن 100% (لا 3D ولا رسوم)
**الأدوات:** صور المراجع والمشاهد: وكيل Arena • الفيديو: Google Flow (إطار بداية + إطار نهاية)

> هذه النسخة تحل محل مذكرة Gemini. صحّحت الأخطاء البصرية والدينية والمنطقية، وأعدت بناء كل مشهد ليتناسب مع طريقة العمل الفعلية: **مراجع مرفوعة بالاسم، صور مفتاحية دقيقة، وفيديو من 10 ثواني بكاميرا ثابتة**. كل صورة فيها **شرح عربي مفصل** لشكلها، ثم **برومبت إنجليزي جاهز للنسخ**.

---

## 0) الأخطاء اللي لقيتها وكيفاش صلحتها

### أ) أخطاء تقنية (هي سبب فشل Arena)

| # | الخطأ في المذكرة القديمة | التصحيح |
|---|---|---|
| 1 | برومبتات الصور فيها `--ar 9:16 --v 6.1 --style raw` (صيغة Midjourney). وكيل Arena ما يفهمهاش ويكتبها كنص أو يتجاهلها | **حذفتها**. المقاس عمودي مكتوب بالكلمات |
| 2 | المراجع بمعرّفات مثل `[REF-CHAR-01]` داخل البرومبت. الوكيل ما يقدرش يربطها بصورة | المراجع الآن **أسماء ملفات** (`REF_AMIN` …) ترفعها مع كل توليد، وكل صورة تذكر مراجعها بالترتيب |
| 3 | بطاقات الشخصيات بنسبة 9:16 لصورة «كل الزوايا». النتيجة صورة واحدة بلا زوايا | بطاقات الشخصيات **16:9 أفقية** بأربع زوايا ووجهين. والمراجع البيئية فقط عمودية |
| 4 | كلمات مثل `Hasselblad` و`Anamorphic` و`Kodak 5219` و`8k hyper-detailed`. تعطي مظهر CGI مصقولًا بلا واقعية | استبدلتها بعدسة 35mm وحبيبات فيلم طبيعية وبشرة بمسام وبلا ريتوش |
| 5 | في برومبت الفيديو: سطور `Phonetic:` و`Translation:` بالإنجليزية داخل البرومبت. تخلي Veo ينطق الترجمة أو يكتب نصوصًا | **حذفتها من البرومبتات** وحطيت الترجمة في جدول خارجها |
| 6 | المشهد 5 فيه حركة كاميرا (`tilt-up tracking`) وإطار البداية لقطة أرض والنهاية لقطة من الخلف. مستحيل مع إطارين أول وآخر | كاميرا **ثابتة** وكادر واحد بثلاثة أرباع، من الجانب، والقارورة في الإطار الأول والأخير |
| 7 | إطارات البداية لا تطابق الحركة: المشهد 4 يبدأ بـ«ينزل ويضع يده» والصورة فيها اليد موضوعة. المشهد 9 يبدأ بـ«يوسف ينهض من السجود» والصورة فيها جالس | إطار البداية صار **قبل** الحركة، وإطار النهاية **بعدها** |
| 8 | إطار نهاية المشهد 8 (الأيدي مرفوعة) يناقض آخر الفيديو (الأيدي على الصدر) | إطار النهاية الآن اليدان على الصدر |
| 9 | كل مشهد صورة أو اثنتين بلا مراعاة الاستمرارية. ومعرّفات «الأيمن والأيسر» غير موحدة | قفل «اتجاه الكاميرا» لكل مكان، وتمرير الصورة السابقة كأم للصور المتتابعة |
| 10 | القارورة: في المشهد 1 في اليد، وفي المشهد 2 «بجانبه» | القارورة **في يده اليمنى** حتى لحظة سقوطها في المشهد 5، وبلا ملصق |
| 11 | في المشهد 4 الصورة: يد يوسف اليسرى. الفيديو: اليمنى. وكتفان مختلفان | موحدة: **اليد اليمنى على كتف أمين الأيسر** |
| 12 | جمل «STRICTLY FORBIDDEN» تتضمن حتى «no smiling». وقوائم سلبية مخلوطة بالإيجابية | فصلتها في سطر `NEGATIVE` واحد في آخر كل برومبت |
| 13 | عدد ثابت للصور لكل مشهد غير مدروس | عدد الصور **حسب حاجة المشهد: 19 صورة** (مشهدان بصورة واحدة، سبعة باثنتين، ومشهد بثلاث) |
| 14 | ذكر أدوات غير مستعملة (Kling, Veo 2, Midjourney, Flux) | حذفته. الصور بوكيل Arena والفيديو بـ Google Flow |

### ب) أخطاء منطقية في القصة

| # | الخطأ | التصحيح |
|---|---|---|
| 15 | أمين يقول «يا خويا يوسف» وهو ما سمع اسمه قط. ويوسف يناديه «يا أمين» دون تعارف | أمين يقدّم نفسه في المشهد 3 («أنا أمين»)، ويوسف يسأله عن المسجد من خلف الكتف |
| 16 | أمين في المشهد 3 «يسحب يده» وهو ما مدّها أصلًا | حذفت الحركة، وصار يخفض رأسه ويبتعد بنظره |
| 17 | أمين يقول «ما نصلحش ندخل لبيت ربي» لكن ما أحد دعاه للمسجد | يوسف يدعوه في بداية المشهد 3: «الفجر قرّب… تجي معايا للمسجد؟» |
| 18 | الزمن: الشارع «الساعة 2:00 فجرًا» ثم ضوء الفجر الذهبي في المسجد، والمسجد مغلق في 2:00 | الزمن الآن **آخر ساعة قبل الفجر**، ثم **ضوء الفجر الأزرق الناعم** في المسجد |
| 19 | لا مرجع لباب المسجد، والمشهد 5 ينتهي نحو «قوس المسجد» غير الموجود | قوس مضيء **بعيد جدًا** على يمين الزقاق داخل مرجع الشارع نفسه |
| 20 | جمل الحوار أطول من 10 ثواني (المشهد 4 و8 و10 بحوالي 3 كلمات في الثانية) | قصّرتها وأعدت توزيع التوقيت |
| 21 | المشهد 10: «فرّجت الصلاة» (لا تُقال هكذا في الدارجة)، و«مات ساجدًا سبحان ربي الرحيم» طويلة | «خلصت الصلاة يا خويا»، وعند الوفاة: «إنا لله وإنا إليه راجعون… هنيئًا ليك» |

### ج) أخطاء في الدقة الدينية

| # | الخطأ | التصحيح |
|---|---|---|
| 22 | في الوضوء يبدأ بغسل الوجه، والترتيب النبوي يبدأ **بغسل اليدين ثلاثًا** | المشهد 6: غسل اليدين ثلاثًا، المشهد 7: الوجه ثم الساعدان (مختصر سينمائي) |
| 23 | «كل عضو اغسلو ثلاث مرات» فيه تعميم (مسح الرأس مرة واحدة) | «نبداو باليدين، تلات مرات. هاذي سنة النبي ﷺ» |
| 24 | ذكر بعد الوضوء ناقص: نصف الشهادة فقط | الشهادة كاملة بالفصحى |
| 25 | «تحية المسجد» تُصلى فرادى عادة، لا جماعة بإمام | «نصلّو ركعتين» (نافلة بالجماعة، وهي الصورة الصحيحة لوقوف المأموم عن يمين الإمام كما في حديث ابن عباس) |
| 26 | في المشهد 9 الصورة تضع يوسف «في العمق» وأمين «في المقدمة»، وهو يخالف وقوفهما كتفًا بكتف | الاثنان على نفس الخط، وكاميرا أمامية منخفضة ثابتة للمشهدين 9 و10 |

### د) أخطاء في النشر
- هاشتاقات `#Veo2 #KlingAI #Midjourney` تفضح الأدوات وتضر بالجمهور المستهدف.
- «الملايين يبكون» و«أبكى الجميع» ادعاءات غير صحيحة.
- ما فيه تذكير بإقرار المحتوى المولّد بالذكاء الاصطناعي. (تفاصيل في القسم 7.)

---

## 1) القواعد العامة

### 🎥 الكاميرا والمقاس
- 9:16 عمودي فقط، 10 ثواني بالضبط لكل مقطع، 30 FPS.
- كاميرا ثابتة (trépied)، بدفع خفيف جدًا (حوالي 3%) على الأكثر. بلا حركة يدوية ولا pan ولا قطع داخل المقطع.

### 🔊 الصوت
- **بلا موسيقى نهائيًا.** فقط أصوات الواقع (ريح، قطرات ماء، خطوات، همس).
- الحوار فقط في أماكنه المحددة، والتلاوة بالفصحى.

### 🗣️ اللهجة
جزائرية طبيعية. وكل الكلمات مشكولة لتسهيل النطق (راجع جدول الحوار في القسم 5).

### 💰 الرصيد
10 فيديوهات × 15 كريدت = **150 كريدت = 4 حسابات** (3 مقاطع لكل حساب، والرابع للمشهد 10).

### 🧭 قفل اتجاه الكاميرا (الأهم للاستمرارية)
**الزقاق (المشاهد 1 → 5):** الكاميرا عبر الزقاق بمستوى العين (إلا المشهد 1 منخفضة وقريبة)، الجدار والدكان المغلق والرصيف على اليسار، وعمود الإنارة فوق الرصيف، ومدخل المسجد القوس المضيء **بعيد جدًا على اليمين**. يوسف يدخل من **اليسار** ماشيًا نحو **اليمين**.

**الميضأة (6 → 7):** صف من 4 حنفيات، يوسف عند اليسرى وأمين على يمينه. الكاميرا عند طرف الصف الأيسر.

**قاعة الصلاة (8 → 10):**

```text
                 جدار القبلة (المحراب)
        ─────────────────────────────────
              ┌─────────┐ ┌─────────┐
              │ يوسف    │ │ أمين    │    ← من وجهة نظر المصلّين (يواجهون القبلة)
              │ (إمام)  │ │ (مأموم) │      أمين على يمين الإمام، كتفًا بكتف
              └─────────┘ └─────────┘
   كاميرا المشهد 8 = من الخلف: يوسف يسار الكادر، أمين يمينه
   كاميرا المشهدين 9 و10 = من الأمام (منخفضة): أمين يسار الكادر، يوسف يمينه (انقلاب طبيعي)
```

---

## 2) المراجع (ارفع هذه الصور مع كل توليد)

الأسماء إلزامية: `REF_AMIN`، `REF_YOUCEF`، `REF_ENV_STREET`، `REF_ENV_ABLUTION`، `REF_ENV_PRAYER`.

**انسخ هذا البلوك للوكيل مرة واحدة لتوليد المراجع الخمسة:**


```text
Generate FIVE separate reference images in this order, each labeled exactly with its name: REF_AMIN, REF_YOUCEF, REF_ENV_STREET, REF_ENV_ABLUTION, REF_ENV_PRAYER. All are photorealistic live-action cinematic photography with natural skin texture and realistic hands, no 3D render, no cartoon, no illustration, no readable text, no logos, no watermark.

=== REF_AMIN === (landscape 16:9 character reference sheet, plain light-grey studio background, ONE person only)
A 24-year-old Algerian young man. Pale olive skin, slightly gaunt cheeks, dark messy wavy hair falling slightly over the forehead, patchy five-day stubble, dark circles under sorrowful brown eyes showing deep exhaustion and guilt. He wears an oversized faded black hoodie (hood DOWN) over a dark grey T-shirt, dark charcoal washed jeans and worn scuffed sneakers. Show the same man in full-body front, three-quarter, side and back views, plus two close-up faces: broken and exhausted, and calm with a faint peace. Add one extra panel of the same man barefoot with the hoodie sleeves pushed above the elbows. Identical face, clothes and proportions in every view. Soft natural lighting.

=== REF_YOUCEF === (landscape 16:9 character reference sheet, plain light-grey studio background, ONE person only)
A 27-year-old Algerian young man. Warm medium-olive skin, full neatly trimmed black beard, short neat black hair, gentle compassionate brown eyes, calm dignified posture. He wears a clean cream-beige Algerian cotton qamis (long, light embroidery at the collar) over simple trousers and simple leather sandals. Show the same man in full-body front, three-quarter, side and back views, plus two close-up faces: warm gentle smile, and serious calm. Add one extra panel barefoot with the qamis sleeves pushed above the elbows. Identical face, clothes and proportions in every view. Soft natural lighting.

=== REF_ENV_STREET === (VERTICAL 9:16, no people)
A narrow old alley in a working-class Algiers quarter in the last hour before dawn, still dark with a faint deep-blue glow at the top of the sky. Seen from across the alley at eye level: on the LEFT-center a tall old building wall with peeling plaster and a closed rolled-down metal shop shutter, with a raised concrete curb along its base; a tall pole with ONE dim warm sodium streetlamp above the curb at the center-left; damp cracked asphalt with small puddles reflecting the lamp; the alley continues to the RIGHT with a slight bend and, far away on the right, a small arched doorway glows warm yellow-green (the mosque entrance), tiny and distant. Chilly air, very faint mist. Nothing else in the alley.

=== REF_ENV_ABLUTION === (VERTICAL 9:16, no people)
A clean traditional Algerian mosque ablution room. A long wall tiled in turquoise-and-white zellige with a row of four polished chrome faucets about 70 cm above a long low smooth stone bench that runs along the wall; a narrow marble drain trough on the damp grey stone floor in front of the bench; soft white ceiling light plus warm wall lamps; faint steam. Camera at the left end of the row, eye level, angled slightly into the room, the whole row of four faucets visible. Calm, clean, tranquil.

=== REF_ENV_PRAYER === (VERTICAL 9:16, no people)
A modest Algerian mosque prayer hall seen from the back of the hall at eye level toward the qibla wall. The qibla wall with a white plaster horseshoe mihrab in its center and a wooden minbar to the right of the mihrab; a green wool prayer carpet with cream stripes running PARALLEL to the qibla wall; two white plaster columns left and right; high arched windows in the right wall letting in soft cool-blue dawn light with a first warm tint; warm pendant lamps. Empty hall, absolute stillness.
```


---

## 3) خطة الصور (19 صورة)

| المشهد | عدد الصور | الصور | لماذا؟ |
|---|---|---|---|
| **SC01** | 1 | SC01_A | حركة خفيفة جدًا (تنفس ودمعة). الإطار الأول يكفي |
| **SC02** | 2 | SC02_A، SC02_B | دخول يوسف ثم وقوفه ومد يده، تغيّر واضح |
| **SC03** | 1 | SC03_A | الحوار على وجه واحد في لقطة ثابتة. إطار البداية يكفي ويحفظ تزامن الشفاه |
| **SC04** | 2 | SC04_A، SC04_B | النزول على الركبة ووضع اليد |
| **SC05** | 2 | SC05_A، SC05_B | سقوط القارورة ثم الوقوف والخطوة الأولى |
| **SC06** | 2 | SC06_A، SC06_B | غسل اليدين ثم شرح السنة، وبدء رفع أكمام أمين |
| **SC07** | 2 | SC07_A، SC07_B | قبل غسل الوجه وبعده |
| **SC08** | 2 | SC08_A، SC08_B | الهمس ثم التكبير ووضع اليدين على الصدر |
| **SC09** | 2 | SC09_A، SC09_B | سجودان ثم جلوس يوسف وبقاء أمين |
| **SC10** | 3 | SC10_A، SC10_B، SC10_C | أهم مشهد، والصورة الوسطى (B) مرجع إضافي لحركة الاستسلام الهادئة |

### جدول Flow (أي صورتين لكل فيديو)

| المشهد | الإطار الأول | الإطار الأخير | مرجع إضافي | الحساب |
|---|---|---|---|---|
| 1 | SC01_A | — (إطار أول فقط) | — | 1 |
| 2 | SC02_A | SC02_B | — | 1 |
| 3 | SC03_A | — (إطار أول فقط) | — | 1 |
| 4 | SC04_A | SC04_B | — | 2 |
| 5 | SC05_A | SC05_B | — | 2 |
| 6 | SC06_A | SC06_B | — | 2 |
| 7 | SC07_A | SC07_B | — | 3 |
| 8 | SC08_A | SC08_B | — | 3 |
| 9 | SC09_A | SC09_B | — | 3 |
| 10 | SC10_A | SC10_C | SC10_B (اختياري) | 4 |

**ترتيب التوليد:** المراجع الخمسة ← الدفعة 1 (الزقاق، 8 صور) ← الدفعة 2 (الميضأة، 4 صور) ← الدفعة 3 (قاعة الصلاة، 7 صور). كل دفعة في مكان واحد باش تثبت الأضواء والتفاصيل.

---

## 4) تفاصيل الصور والبرومبتات (صورة بصورة)


#### المشهد 01 — الضياع في عتمة الليل


##### 🖼️ SC01_A — إطار البداية (الصورة الوحيدة للمشهد)

**كيفاش راح تكون الصورة:** لقطة قريبة-متوسطة من زاوية منخفضة قليلًا: أمين جالس منهارًا على الرصيف الإسمنتي أمام الدكان المغلق تحت ضوء عمود الإنارة الخافت. يده اليمنى معلقة بين ركبتيه وفيها قارورة زجاج داكنة **بلا ملصق** وقاعدتها تلمس الرصيف، ورأسه منحنٍ بخجل وحسرة، العينان غائرتان والخدان هزيلان واللحية خفيفة، والقلنسوة **مرخاة للخلف**. الضوء العنبري من العمود على جهة واحدة من وجهه وظل عميق على الجهة الأخرى. في أقصى يمين الخلفية ضوء القوس الدافئ البعيد جدًا (المسجد) صغير وغير واضح.

**ارفع معها (بالترتيب):** `REF_ENV_STREET`، `REF_AMIN`

```text
Use the uploaded reference images listed in the scene header, in that order (the FIRST one is the portrait base). Reproduce the exact faces, clothes, location layout and props. AMIN: 24-year-old Algerian young man, pale olive skin, slightly gaunt cheeks, dark messy wavy hair, patchy five-day stubble, dark circles under sorrowful brown eyes, oversized faded black hoodie with the hood DOWN over a dark grey T-shirt, dark charcoal washed jeans, worn scuffed sneakers (street). In the mosque: the same hoodie with the sleeves pushed above the elbows, barefoot. LOCATION LOCK (REF_ENV_STREET, never change): a narrow old alley in a working-class Algiers quarter in the last hour before dawn, still dark with a faint deep-blue glow at the top of the sky. Seen from across the alley at eye level: on the LEFT-center a tall old building wall with peeling plaster and a closed rolled-down metal shop shutter, with a raised concrete curb along its base; a tall pole with ONE dim warm sodium streetlamp above the curb at the center-left; damp cracked asphalt with small puddles reflecting the lamp; the alley continues to the RIGHT with a slight bend, and far away on the right a small arched doorway glows warm yellow-green (the mosque entrance), tiny and distant. Nothing else in the alley. Chilly air, very faint mist. SHOT: Low-angle medium close-up, slightly from below. Amin sits slumped on the raised concrete curb in front of the closed shop shutter under the dim sodium streetlamp. His right hand hangs between his knees holding a dark glass bottle with NO label whose base touches the pavement. His head is bowed in deep shame and regret, sunken eyes, hollow cheeks, hood down. Amber light from the lamp on one side of his face, deep shadow on the other. In the far right background, tiny and out of focus, the warm glow of the distant arched doorway. Photorealistic live-action film still, natural 35mm lens look, soft natural film grain, real skin texture with pores and fine lines, no beauty retouching, believable fabric creases and wet-surface reflections, motivated practical lighting, accurate hands with five fingers each. Vertical 9:16 portrait. NEGATIVE: no 3D render, no CGI look, no illustration, no painting, no plastic or waxy skin, no HDR over-sharpening, no landscape or square format, no identity drift, no face change, no age change, no clothing change, no extra people, no duplicate bodies, no extra fingers, no distorted hands, no floating objects, no mirrored layout, no readable text, no logos, no brand labels, no watermark, no subtitles.
```


#### المشهد 02 — اللقاء غير المتوقع


##### 🖼️ SC02_A — إطار البداية

**كيفاش راح تكون الصورة:** لقطة متوسطة-واسعة من الجهة المقابلة للزقاق بمستوى العين (حوالي 1.3 م). أمين جالس على الرصيف في يمين-وسط الكادر والقارورة في يده اليمنى ورأسه منحنٍ. عند **الحافة اليسرى** للكادر يدخل يوسف ماشيًا نحو اليمين (نحو ضوء المسجد البعيد) في منتصف خطوة، ورأسه ملتفت نحو أمين وفي وجهه اهتمام وشفقة فورية. الاثنان ظاهران كاملان، عمود الإنارة فوق الرصيف والإسفلت مبلل.

**ارفع معها (بالترتيب):** `REF_ENV_STREET`، `REF_AMIN`، `REF_YOUCEF`

```text
Use the uploaded reference images listed in the scene header, in that order (the FIRST one is the portrait base). Reproduce the exact faces, clothes, location layout and props. AMIN: 24-year-old Algerian young man, pale olive skin, slightly gaunt cheeks, dark messy wavy hair, patchy five-day stubble, dark circles under sorrowful brown eyes, oversized faded black hoodie with the hood DOWN over a dark grey T-shirt, dark charcoal washed jeans, worn scuffed sneakers (street). In the mosque: the same hoodie with the sleeves pushed above the elbows, barefoot. YOUCEF: 27-year-old Algerian young man, warm medium-olive skin, full neatly trimmed black beard, short neat black hair, gentle brown eyes, calm compassionate face, a clean cream-beige Algerian cotton qamis (long, light embroidery at the collar) over simple trousers, leather sandals in the street, barefoot in the mosque. LOCATION LOCK (REF_ENV_STREET, never change): a narrow old alley in a working-class Algiers quarter in the last hour before dawn, still dark with a faint deep-blue glow at the top of the sky. Seen from across the alley at eye level: on the LEFT-center a tall old building wall with peeling plaster and a closed rolled-down metal shop shutter, with a raised concrete curb along its base; a tall pole with ONE dim warm sodium streetlamp above the curb at the center-left; damp cracked asphalt with small puddles reflecting the lamp; the alley continues to the RIGHT with a slight bend, and far away on the right a small arched doorway glows warm yellow-green (the mosque entrance), tiny and distant. Nothing else in the alley. Chilly air, very faint mist. SHOT: Medium-wide shot across the alley at eye level (about 1.3 m). Amin sits on the curb in the right-center, bottle in his right hand, head bowed. At the LEFT edge of the frame, Youcef enters walking toward the right (toward the distant mosque glow), caught mid-stride, head turning toward Amin with immediate concern. Both fully visible, streetlamp above the curb, wet asphalt. Photorealistic live-action film still, natural 35mm lens look, soft natural film grain, real skin texture with pores and fine lines, no beauty retouching, believable fabric creases and wet-surface reflections, motivated practical lighting, accurate hands with five fingers each. Vertical 9:16 portrait. NEGATIVE: no 3D render, no CGI look, no illustration, no painting, no plastic or waxy skin, no HDR over-sharpening, no landscape or square format, no identity drift, no face change, no age change, no clothing change, no extra people, no duplicate bodies, no extra fingers, no distorted hands, no floating objects, no mirrored layout, no readable text, no logos, no brand labels, no watermark, no subtitles.
```


##### 🖼️ SC02_B — إطار النهاية

**كيفاش راح تكون الصورة:** نفس الكادر بالضبط. يوسف توقف على بعد 1.2 م أمام أمين، منحنٍ قليلًا من الخصر، يمد يده اليمنى المفتوحة نحوه بابتسامة أخوية هادئة. أمين رفع رأسه ينظر إليه بعينين واسعتين مذهولتين بين الدفاع والانكسار، والقارورة ما زالت في يده اليمنى منخفضة.

**ارفع معها (بالترتيب):** `REF_ENV_STREET`، `REF_AMIN`، `REF_YOUCEF`، + صورة SC02_A كأم

```text
Use the uploaded reference images listed in the scene header, in that order (the FIRST one is the portrait base). Reproduce the exact faces, clothes, location layout and props. AMIN: 24-year-old Algerian young man, pale olive skin, slightly gaunt cheeks, dark messy wavy hair, patchy five-day stubble, dark circles under sorrowful brown eyes, oversized faded black hoodie with the hood DOWN over a dark grey T-shirt, dark charcoal washed jeans, worn scuffed sneakers (street). In the mosque: the same hoodie with the sleeves pushed above the elbows, barefoot. YOUCEF: 27-year-old Algerian young man, warm medium-olive skin, full neatly trimmed black beard, short neat black hair, gentle brown eyes, calm compassionate face, a clean cream-beige Algerian cotton qamis (long, light embroidery at the collar) over simple trousers, leather sandals in the street, barefoot in the mosque. LOCATION LOCK (REF_ENV_STREET, never change): a narrow old alley in a working-class Algiers quarter in the last hour before dawn, still dark with a faint deep-blue glow at the top of the sky. Seen from across the alley at eye level: on the LEFT-center a tall old building wall with peeling plaster and a closed rolled-down metal shop shutter, with a raised concrete curb along its base; a tall pole with ONE dim warm sodium streetlamp above the curb at the center-left; damp cracked asphalt with small puddles reflecting the lamp; the alley continues to the RIGHT with a slight bend, and far away on the right a small arched doorway glows warm yellow-green (the mosque entrance), tiny and distant. Nothing else in the alley. Chilly air, very faint mist. SHOT: Same framing and positions as the previous image (use it as the exact base). Youcef has stopped about 1.2 m in front of Amin, bent slightly at the waist, extending his open right hand toward him with a warm humble brotherly smile. Amin has lifted his head and looks up with wide startled eyes caught between defense and vulnerability, the bottle still held low in his right hand. Photorealistic live-action film still, natural 35mm lens look, soft natural film grain, real skin texture with pores and fine lines, no beauty retouching, believable fabric creases and wet-surface reflections, motivated practical lighting, accurate hands with five fingers each. Vertical 9:16 portrait. NEGATIVE: no 3D render, no CGI look, no illustration, no painting, no plastic or waxy skin, no HDR over-sharpening, no landscape or square format, no identity drift, no face change, no age change, no clothing change, no extra people, no duplicate bodies, no extra fingers, no distorted hands, no floating objects, no mirrored layout, no readable text, no logos, no brand labels, no watermark, no subtitles.
```


#### المشهد 03 — الخجل من بيت الله


##### 🖼️ SC03_A — إطار البداية (الصورة الوحيدة للمشهد)

**كيفاش راح تكون الصورة:** لقطة مقربة من فوق الكتف: الكاميرا خلف **كتف يوسف الأيمن** بمستوى صدره تنظر قليلًا للأسفل. كتف القماص الكريمي وجانب رأس يوسف **ضبابيان** في الحافة اليمنى للكادر. في البؤرة الحادة وسط-يسار الكادر وجه أمين وهو جالس أسفل منه، ينظر للأسفل ويبتعد قليلًا نحو اليسار، شفتاه مفتوحتان قليلًا كأنه يبدأ الكلام، حاجباه معقودان وعيناه لامعتان بدموع محبوسة. يده وقارورته ظاهرتان منخفضتين عند الحافة السفلية. ضوء العمود من أعلى اليسار.

**ارفع معها (بالترتيب):** `REF_ENV_STREET`، `REF_AMIN`، `REF_YOUCEF`

```text
Use the uploaded reference images listed in the scene header, in that order (the FIRST one is the portrait base). Reproduce the exact faces, clothes, location layout and props. AMIN: 24-year-old Algerian young man, pale olive skin, slightly gaunt cheeks, dark messy wavy hair, patchy five-day stubble, dark circles under sorrowful brown eyes, oversized faded black hoodie with the hood DOWN over a dark grey T-shirt, dark charcoal washed jeans, worn scuffed sneakers (street). In the mosque: the same hoodie with the sleeves pushed above the elbows, barefoot. YOUCEF: 27-year-old Algerian young man, warm medium-olive skin, full neatly trimmed black beard, short neat black hair, gentle brown eyes, calm compassionate face, a clean cream-beige Algerian cotton qamis (long, light embroidery at the collar) over simple trousers, leather sandals in the street, barefoot in the mosque. LOCATION LOCK (REF_ENV_STREET, never change): a narrow old alley in a working-class Algiers quarter in the last hour before dawn, still dark with a faint deep-blue glow at the top of the sky. Seen from across the alley at eye level: on the LEFT-center a tall old building wall with peeling plaster and a closed rolled-down metal shop shutter, with a raised concrete curb along its base; a tall pole with ONE dim warm sodium streetlamp above the curb at the center-left; damp cracked asphalt with small puddles reflecting the lamp; the alley continues to the RIGHT with a slight bend, and far away on the right a small arched doorway glows warm yellow-green (the mosque entrance), tiny and distant. Nothing else in the alley. Chilly air, very faint mist. SHOT: Over-the-shoulder medium close-up. The camera is behind Youcef's RIGHT shoulder at chest height, looking slightly down. The blurred cream qamis shoulder and the side of Youcef's head fill the RIGHT edge of the frame (his face is not visible). In sharp focus in the left-center: Amin's face, seated on the curb below, looking down and slightly away to the left, lips slightly parted as if about to speak, brows drawn together, eyes glistening with held-back tears. His right hand and the dark unlabeled bottle are visible low at the bottom edge. Lamp light from the upper left, shallow depth of field. Photorealistic live-action film still, natural 35mm lens look, soft natural film grain, real skin texture with pores and fine lines, no beauty retouching, believable fabric creases and wet-surface reflections, motivated practical lighting, accurate hands with five fingers each. Vertical 9:16 portrait. NEGATIVE: no 3D render, no CGI look, no illustration, no painting, no plastic or waxy skin, no HDR over-sharpening, no landscape or square format, no identity drift, no face change, no age change, no clothing change, no extra people, no duplicate bodies, no extra fingers, no distorted hands, no floating objects, no mirrored layout, no readable text, no logos, no brand labels, no watermark, no subtitles.
```


#### المشهد 04 — الاحتواء وسعة الرحمة


##### 🖼️ SC04_A — إطار البداية

**كيفاش راح تكون الصورة:** لقطة قريبة-متوسطة بمستوى عين أمين: يوسف ينزل بجسده، ركبته اليمنى على وشك لمس الأرض المبللة ووجهه في مستوى وجه أمين، ويده اليمنى ممدودة نحو **كتف أمين الأيسر** دون أن تلمسه بعد، وملامحه رحمة وهدوء. في الحافة اليسرى الأمامية وبشكل ضبابي: رأس أمين المنحني وكتفه المنهار بقلنسوته السوداء. ضوء دافئ من أعلى اليسار وتوهج أزرق خافت خلفهما.

**ارفع معها (بالترتيب):** `REF_ENV_STREET`، `REF_YOUCEF`، `REF_AMIN`

```text
Use the uploaded reference images listed in the scene header, in that order (the FIRST one is the portrait base). Reproduce the exact faces, clothes, location layout and props. AMIN: 24-year-old Algerian young man, pale olive skin, slightly gaunt cheeks, dark messy wavy hair, patchy five-day stubble, dark circles under sorrowful brown eyes, oversized faded black hoodie with the hood DOWN over a dark grey T-shirt, dark charcoal washed jeans, worn scuffed sneakers (street). In the mosque: the same hoodie with the sleeves pushed above the elbows, barefoot. YOUCEF: 27-year-old Algerian young man, warm medium-olive skin, full neatly trimmed black beard, short neat black hair, gentle brown eyes, calm compassionate face, a clean cream-beige Algerian cotton qamis (long, light embroidery at the collar) over simple trousers, leather sandals in the street, barefoot in the mosque. LOCATION LOCK (REF_ENV_STREET, never change): a narrow old alley in a working-class Algiers quarter in the last hour before dawn, still dark with a faint deep-blue glow at the top of the sky. Seen from across the alley at eye level: on the LEFT-center a tall old building wall with peeling plaster and a closed rolled-down metal shop shutter, with a raised concrete curb along its base; a tall pole with ONE dim warm sodium streetlamp above the curb at the center-left; damp cracked asphalt with small puddles reflecting the lamp; the alley continues to the RIGHT with a slight bend, and far away on the right a small arched doorway glows warm yellow-green (the mosque entrance), tiny and distant. Nothing else in the alley. Chilly air, very faint mist. SHOT: Medium close-up at Amin's eye level. Youcef is lowering himself, his right knee about to touch the wet ground, his face level with Amin's, his right hand extended toward Amin's LEFT shoulder but not touching it yet, an expression of calm compassion. At the left foreground edge, out of focus: Amin's bowed head and slumped shoulder in the black hoodie. Warm lamp light from the upper left, a faint cool blue glow behind them. Photorealistic live-action film still, natural 35mm lens look, soft natural film grain, real skin texture with pores and fine lines, no beauty retouching, believable fabric creases and wet-surface reflections, motivated practical lighting, accurate hands with five fingers each. Vertical 9:16 portrait. NEGATIVE: no 3D render, no CGI look, no illustration, no painting, no plastic or waxy skin, no HDR over-sharpening, no landscape or square format, no identity drift, no face change, no age change, no clothing change, no extra people, no duplicate bodies, no extra fingers, no distorted hands, no floating objects, no mirrored layout, no readable text, no logos, no brand labels, no watermark, no subtitles.
```


##### 🖼️ SC04_B — إطار النهاية

**كيفاش راح تكون الصورة:** نفس الكادر. يوسف جاثٍ على ركبة واحدة على الأرض المبللة، يده اليمنى مستقرة على كتف أمين الأيسر، وابتسامة تشجيع مشعة ورحيمة وعيناه تنظران في عيني أمين. أمين في الحافة اليسرى ضبابي ورأسه ما زال منحنيًا.

**ارفع معها (بالترتيب):** `REF_ENV_STREET`، `REF_YOUCEF`، `REF_AMIN`، + صورة SC04_A كأم

```text
Use the uploaded reference images listed in the scene header, in that order (the FIRST one is the portrait base). Reproduce the exact faces, clothes, location layout and props. AMIN: 24-year-old Algerian young man, pale olive skin, slightly gaunt cheeks, dark messy wavy hair, patchy five-day stubble, dark circles under sorrowful brown eyes, oversized faded black hoodie with the hood DOWN over a dark grey T-shirt, dark charcoal washed jeans, worn scuffed sneakers (street). In the mosque: the same hoodie with the sleeves pushed above the elbows, barefoot. YOUCEF: 27-year-old Algerian young man, warm medium-olive skin, full neatly trimmed black beard, short neat black hair, gentle brown eyes, calm compassionate face, a clean cream-beige Algerian cotton qamis (long, light embroidery at the collar) over simple trousers, leather sandals in the street, barefoot in the mosque. LOCATION LOCK (REF_ENV_STREET, never change): a narrow old alley in a working-class Algiers quarter in the last hour before dawn, still dark with a faint deep-blue glow at the top of the sky. Seen from across the alley at eye level: on the LEFT-center a tall old building wall with peeling plaster and a closed rolled-down metal shop shutter, with a raised concrete curb along its base; a tall pole with ONE dim warm sodium streetlamp above the curb at the center-left; damp cracked asphalt with small puddles reflecting the lamp; the alley continues to the RIGHT with a slight bend, and far away on the right a small arched doorway glows warm yellow-green (the mosque entrance), tiny and distant. Nothing else in the alley. Chilly air, very faint mist. SHOT: Same framing as the previous image (use it as the exact base). Youcef kneels on one knee on the damp ground, his right hand resting on Amin's LEFT shoulder, a radiant loving smile of encouragement, his eyes looking into Amin's. Amin stays at the left foreground edge, out of focus, head still bowed. Photorealistic live-action film still, natural 35mm lens look, soft natural film grain, real skin texture with pores and fine lines, no beauty retouching, believable fabric creases and wet-surface reflections, motivated practical lighting, accurate hands with five fingers each. Vertical 9:16 portrait. NEGATIVE: no 3D render, no CGI look, no illustration, no painting, no plastic or waxy skin, no HDR over-sharpening, no landscape or square format, no identity drift, no face change, no age change, no clothing change, no extra people, no duplicate bodies, no extra fingers, no distorted hands, no floating objects, no mirrored layout, no readable text, no logos, no brand labels, no watermark, no subtitles.
```


#### المشهد 05 — القرار وكسر القيد


##### 🖼️ SC05_A — إطار البداية

**كيفاش راح تكون الصورة:** لقطة متوسطة-واسعة بنفس اتجاه المشهد 2. أمين جالس على الرصيف في يمين-وسط الكادر، يده اليمنى انفتحت للتو والقارورة الزجاجية الداكنة (بلا ملصق) تنزلق منها وتميل لتتدحرج نحو المزراب. يوسف واقف بجانبه على **اليسار** منحنٍ قليلًا ويده اليمنى ممدودة للأسفل نحو يد أمين اليسرى. الاثنان ظاهران كاملان والعمود فوقهما.

**ارفع معها (بالترتيب):** `REF_ENV_STREET`، `REF_AMIN`، `REF_YOUCEF`

```text
Use the uploaded reference images listed in the scene header, in that order (the FIRST one is the portrait base). Reproduce the exact faces, clothes, location layout and props. AMIN: 24-year-old Algerian young man, pale olive skin, slightly gaunt cheeks, dark messy wavy hair, patchy five-day stubble, dark circles under sorrowful brown eyes, oversized faded black hoodie with the hood DOWN over a dark grey T-shirt, dark charcoal washed jeans, worn scuffed sneakers (street). In the mosque: the same hoodie with the sleeves pushed above the elbows, barefoot. YOUCEF: 27-year-old Algerian young man, warm medium-olive skin, full neatly trimmed black beard, short neat black hair, gentle brown eyes, calm compassionate face, a clean cream-beige Algerian cotton qamis (long, light embroidery at the collar) over simple trousers, leather sandals in the street, barefoot in the mosque. LOCATION LOCK (REF_ENV_STREET, never change): a narrow old alley in a working-class Algiers quarter in the last hour before dawn, still dark with a faint deep-blue glow at the top of the sky. Seen from across the alley at eye level: on the LEFT-center a tall old building wall with peeling plaster and a closed rolled-down metal shop shutter, with a raised concrete curb along its base; a tall pole with ONE dim warm sodium streetlamp above the curb at the center-left; damp cracked asphalt with small puddles reflecting the lamp; the alley continues to the RIGHT with a slight bend, and far away on the right a small arched doorway glows warm yellow-green (the mosque entrance), tiny and distant. Nothing else in the alley. Chilly air, very faint mist. SHOT: Medium-wide shot across the alley at eye level, same direction as the scene 2 frames. Amin sits on the curb in the right-center; his right hand has just opened and the dark unlabeled glass bottle is slipping from it, tipping, about to roll toward the gutter. Youcef stands beside him on the LEFT, leaning slightly, his right hand extended down toward Amin's left hand. Both fully visible, streetlamp above. Photorealistic live-action film still, natural 35mm lens look, soft natural film grain, real skin texture with pores and fine lines, no beauty retouching, believable fabric creases and wet-surface reflections, motivated practical lighting, accurate hands with five fingers each. Vertical 9:16 portrait. NEGATIVE: no 3D render, no CGI look, no illustration, no painting, no plastic or waxy skin, no HDR over-sharpening, no landscape or square format, no identity drift, no face change, no age change, no clothing change, no extra people, no duplicate bodies, no extra fingers, no distorted hands, no floating objects, no mirrored layout, no readable text, no logos, no brand labels, no watermark, no subtitles.
```


##### 🖼️ SC05_B — إطار النهاية

**كيفاش راح تكون الصورة:** نفس الكادر. الاثنان واقفان جنبًا إلى جنب: أمين ممسك بيد يوسف اليمنى بكلتا يديه بقوة، وذراع يوسف اليسرى تسند ظهر أمين. لقد التفتا نحو **اليمين** (نحو القوس الدافئ البعيد) ويظهران بزاوية ثلاثة أرباع من الخلف وهما يخطوان الخطوة الأولى معًا. القارورة الداكنة ملقاة على جانبها عند الرصيف خلفهما بلا بركة سائل.

**ارفع معها (بالترتيب):** `REF_ENV_STREET`، `REF_AMIN`، `REF_YOUCEF`، + صورة SC05_A كأم

```text
Use the uploaded reference images listed in the scene header, in that order (the FIRST one is the portrait base). Reproduce the exact faces, clothes, location layout and props. AMIN: 24-year-old Algerian young man, pale olive skin, slightly gaunt cheeks, dark messy wavy hair, patchy five-day stubble, dark circles under sorrowful brown eyes, oversized faded black hoodie with the hood DOWN over a dark grey T-shirt, dark charcoal washed jeans, worn scuffed sneakers (street). In the mosque: the same hoodie with the sleeves pushed above the elbows, barefoot. YOUCEF: 27-year-old Algerian young man, warm medium-olive skin, full neatly trimmed black beard, short neat black hair, gentle brown eyes, calm compassionate face, a clean cream-beige Algerian cotton qamis (long, light embroidery at the collar) over simple trousers, leather sandals in the street, barefoot in the mosque. LOCATION LOCK (REF_ENV_STREET, never change): a narrow old alley in a working-class Algiers quarter in the last hour before dawn, still dark with a faint deep-blue glow at the top of the sky. Seen from across the alley at eye level: on the LEFT-center a tall old building wall with peeling plaster and a closed rolled-down metal shop shutter, with a raised concrete curb along its base; a tall pole with ONE dim warm sodium streetlamp above the curb at the center-left; damp cracked asphalt with small puddles reflecting the lamp; the alley continues to the RIGHT with a slight bend, and far away on the right a small arched doorway glows warm yellow-green (the mosque entrance), tiny and distant. Nothing else in the alley. Chilly air, very faint mist. SHOT: Same framing as the previous image (use it as the exact base). Both now stand up side by side: Amin grips Youcef's right hand tightly with both of his hands, Youcef's left arm supports Amin's back. They have turned to the RIGHT toward the distant warm arched doorway, seen in three-quarter back view, taking the first step together. The dark unlabeled bottle lies on its side at the curb behind them, no liquid pool. Photorealistic live-action film still, natural 35mm lens look, soft natural film grain, real skin texture with pores and fine lines, no beauty retouching, believable fabric creases and wet-surface reflections, motivated practical lighting, accurate hands with five fingers each. Vertical 9:16 portrait. NEGATIVE: no 3D render, no CGI look, no illustration, no painting, no plastic or waxy skin, no HDR over-sharpening, no landscape or square format, no identity drift, no face change, no age change, no clothing change, no extra people, no duplicate bodies, no extra fingers, no distorted hands, no floating objects, no mirrored layout, no readable text, no logos, no brand labels, no watermark, no subtitles.
```


#### المشهد 06 — تعلّم الوضوء


##### 🖼️ SC06_A — إطار البداية

**كيفاش راح تكون الصورة:** لقطة ثنائية متوسطة من **طرف الصف الأيسر** وبزاوية خفيفة نحو القاعة: يوسف الأقرب للكاميرا جالس أمام الحنفية اليسرى وأكمام قماصه مرفوعة فوق المرفقين، يغسل يديه تحت الماء الجاري وقطرات الماء على يديه. أمين جالس بجانبه عند الحنفية الثانية (على يمينه) بقلنسوته السوداء وأكمامه **لم تُرفع بعد**، وينظر إلى يوسف باهتمام وخشوع طفولي. الزليج التركوازي والحنفيات الكروم تلمع بالبلل.

**ارفع معها (بالترتيب):** `REF_ENV_ABLUTION`، `REF_YOUCEF`، `REF_AMIN`

```text
Use the uploaded reference images listed in the scene header, in that order (the FIRST one is the portrait base). Reproduce the exact faces, clothes, location layout and props. AMIN: 24-year-old Algerian young man, pale olive skin, slightly gaunt cheeks, dark messy wavy hair, patchy five-day stubble, dark circles under sorrowful brown eyes, oversized faded black hoodie with the hood DOWN over a dark grey T-shirt, dark charcoal washed jeans, worn scuffed sneakers (street). In the mosque: the same hoodie with the sleeves pushed above the elbows, barefoot. YOUCEF: 27-year-old Algerian young man, warm medium-olive skin, full neatly trimmed black beard, short neat black hair, gentle brown eyes, calm compassionate face, a clean cream-beige Algerian cotton qamis (long, light embroidery at the collar) over simple trousers, leather sandals in the street, barefoot in the mosque. LOCATION LOCK (REF_ENV_ABLUTION, never change): a clean traditional Algerian mosque ablution room. A long wall tiled in turquoise-and-white zellige with a row of four polished chrome faucets about 70 cm above a long low smooth stone bench that runs along the wall; a narrow marble drain trough on the damp grey stone floor in front of the bench; soft white ceiling light plus warm wall lamps; faint steam. SEATING: Youcef sits at the LEFT faucet and Amin at the next faucet to his RIGHT, side by side, both facing the faucets. SHOT: Medium two-shot from the LEFT end of the row of faucets, angled slightly into the room, eye level. Youcef, nearest to the camera, sits at the left faucet with his qamis sleeves pushed above his elbows, washing his hands under the running water, droplets on his hands. Amin sits beside him at the next faucet on his right in his black hoodie with the sleeves still DOWN, watching Youcef with intense childlike attention. Both in three-quarter profile facing the faucets. Wet turquoise zellige tiles and chrome faucets gleam. Photorealistic live-action film still, natural 35mm lens look, soft natural film grain, real skin texture with pores and fine lines, no beauty retouching, believable fabric creases and wet-surface reflections, motivated practical lighting, accurate hands with five fingers each. Vertical 9:16 portrait. NEGATIVE: no 3D render, no CGI look, no illustration, no painting, no plastic or waxy skin, no HDR over-sharpening, no landscape or square format, no identity drift, no face change, no age change, no clothing change, no extra people, no duplicate bodies, no extra fingers, no distorted hands, no floating objects, no mirrored layout, no readable text, no logos, no brand labels, no watermark, no subtitles.
```


##### 🖼️ SC06_B — إطار النهاية

**كيفاش راح تكون الصورة:** نفس الكادر. يوسف التفت برأسه نحو أمين وقطرات الماء على لحيته وابتسامة معلمة هادئة، ويده اليمنى المبللة مرفوعة بثلاثة أصابع ممدودة لتبيين «ثلاث مرات». أمين يستمع ويومئ، ويبدأ بدفع أكمام قلنسوته السوداء نحو المرفقين.

**ارفع معها (بالترتيب):** `REF_ENV_ABLUTION`، `REF_YOUCEF`، `REF_AMIN`، + صورة SC06_A كأم

```text
Use the uploaded reference images listed in the scene header, in that order (the FIRST one is the portrait base). Reproduce the exact faces, clothes, location layout and props. AMIN: 24-year-old Algerian young man, pale olive skin, slightly gaunt cheeks, dark messy wavy hair, patchy five-day stubble, dark circles under sorrowful brown eyes, oversized faded black hoodie with the hood DOWN over a dark grey T-shirt, dark charcoal washed jeans, worn scuffed sneakers (street). In the mosque: the same hoodie with the sleeves pushed above the elbows, barefoot. YOUCEF: 27-year-old Algerian young man, warm medium-olive skin, full neatly trimmed black beard, short neat black hair, gentle brown eyes, calm compassionate face, a clean cream-beige Algerian cotton qamis (long, light embroidery at the collar) over simple trousers, leather sandals in the street, barefoot in the mosque. LOCATION LOCK (REF_ENV_ABLUTION, never change): a clean traditional Algerian mosque ablution room. A long wall tiled in turquoise-and-white zellige with a row of four polished chrome faucets about 70 cm above a long low smooth stone bench that runs along the wall; a narrow marble drain trough on the damp grey stone floor in front of the bench; soft white ceiling light plus warm wall lamps; faint steam. SEATING: Youcef sits at the LEFT faucet and Amin at the next faucet to his RIGHT, side by side, both facing the faucets. SHOT: Same framing as the previous image (use it as the exact base). Youcef has turned his head toward Amin with water droplets on his beard and a calm teaching smile, his wet right hand raised with three fingers extended to show 'three times'. Amin listens and nods, starting to push the sleeves of his black hoodie up toward his elbows. Photorealistic live-action film still, natural 35mm lens look, soft natural film grain, real skin texture with pores and fine lines, no beauty retouching, believable fabric creases and wet-surface reflections, motivated practical lighting, accurate hands with five fingers each. Vertical 9:16 portrait. NEGATIVE: no 3D render, no CGI look, no illustration, no painting, no plastic or waxy skin, no HDR over-sharpening, no landscape or square format, no identity drift, no face change, no age change, no clothing change, no extra people, no duplicate bodies, no extra fingers, no distorted hands, no floating objects, no mirrored layout, no readable text, no logos, no brand labels, no watermark, no subtitles.
```


#### المشهد 07 — التطهير


##### 🖼️ SC07_A — إطار البداية

**كيفاش راح تكون الصورة:** لقطة قريبة جدًا على أمين عند الحنفية: أكمام قلنسوته مرفوعة فوق المرفقين، يداه المضمومتان ممتلئتان بماء صافٍ مرفوعتان تحت ذقنه، عيناه مغمضتان قبل غسل الوجه، وجهه شاحب ومتعب. خلفه على اليسار وبشكل ضبابي يوسف ينظر إليه بابتسامة فخر أخوية. الزليج والحنفيات في خلفية ناعمة.

**ارفع معها (بالترتيب):** `REF_ENV_ABLUTION`، `REF_AMIN`، `REF_YOUCEF`

```text
Use the uploaded reference images listed in the scene header, in that order (the FIRST one is the portrait base). Reproduce the exact faces, clothes, location layout and props. AMIN: 24-year-old Algerian young man, pale olive skin, slightly gaunt cheeks, dark messy wavy hair, patchy five-day stubble, dark circles under sorrowful brown eyes, oversized faded black hoodie with the hood DOWN over a dark grey T-shirt, dark charcoal washed jeans, worn scuffed sneakers (street). In the mosque: the same hoodie with the sleeves pushed above the elbows, barefoot. YOUCEF: 27-year-old Algerian young man, warm medium-olive skin, full neatly trimmed black beard, short neat black hair, gentle brown eyes, calm compassionate face, a clean cream-beige Algerian cotton qamis (long, light embroidery at the collar) over simple trousers, leather sandals in the street, barefoot in the mosque. LOCATION LOCK (REF_ENV_ABLUTION, never change): a clean traditional Algerian mosque ablution room. A long wall tiled in turquoise-and-white zellige with a row of four polished chrome faucets about 70 cm above a long low smooth stone bench that runs along the wall; a narrow marble drain trough on the damp grey stone floor in front of the bench; soft white ceiling light plus warm wall lamps; faint steam. SEATING: Youcef sits at the LEFT faucet and Amin at the next faucet to his RIGHT, side by side, both facing the faucets. SHOT: Close-up on Amin at his faucet. His black hoodie sleeves are pushed above his elbows, his cupped hands are full of clear water raised just below his chin, eyes closed, about to wash his face; his face is pale and tired. In the soft-focus background on the left, Youcef watches him with a warm proud brotherly smile. Zellige tiles and chrome faucets softly out of focus. Photorealistic live-action film still, natural 35mm lens look, soft natural film grain, real skin texture with pores and fine lines, no beauty retouching, believable fabric creases and wet-surface reflections, motivated practical lighting, accurate hands with five fingers each. Vertical 9:16 portrait. NEGATIVE: no 3D render, no CGI look, no illustration, no painting, no plastic or waxy skin, no HDR over-sharpening, no landscape or square format, no identity drift, no face change, no age change, no clothing change, no extra people, no duplicate bodies, no extra fingers, no distorted hands, no floating objects, no mirrored layout, no readable text, no logos, no brand labels, no watermark, no subtitles.
```


##### 🖼️ SC07_B — إطار النهاية

**كيفاش راح تكون الصورة:** نفس الكادر. أمين أنزل يديه، والماء يقطر من ذقنه وفكه ورموشه، عيناه مفتوحتان صافيتان وهادئتان وتنظران قليلًا نحو يوسف بامتنان، ووجهه منتعش ومطمئن. يوسف خلفه ضبابي يومئ بابتسامة حانية.

**ارفع معها (بالترتيب):** `REF_ENV_ABLUTION`، `REF_AMIN`، `REF_YOUCEF`، + صورة SC07_A كأم

```text
Use the uploaded reference images listed in the scene header, in that order (the FIRST one is the portrait base). Reproduce the exact faces, clothes, location layout and props. AMIN: 24-year-old Algerian young man, pale olive skin, slightly gaunt cheeks, dark messy wavy hair, patchy five-day stubble, dark circles under sorrowful brown eyes, oversized faded black hoodie with the hood DOWN over a dark grey T-shirt, dark charcoal washed jeans, worn scuffed sneakers (street). In the mosque: the same hoodie with the sleeves pushed above the elbows, barefoot. YOUCEF: 27-year-old Algerian young man, warm medium-olive skin, full neatly trimmed black beard, short neat black hair, gentle brown eyes, calm compassionate face, a clean cream-beige Algerian cotton qamis (long, light embroidery at the collar) over simple trousers, leather sandals in the street, barefoot in the mosque. LOCATION LOCK (REF_ENV_ABLUTION, never change): a clean traditional Algerian mosque ablution room. A long wall tiled in turquoise-and-white zellige with a row of four polished chrome faucets about 70 cm above a long low smooth stone bench that runs along the wall; a narrow marble drain trough on the damp grey stone floor in front of the bench; soft white ceiling light plus warm wall lamps; faint steam. SEATING: Youcef sits at the LEFT faucet and Amin at the next faucet to his RIGHT, side by side, both facing the faucets. SHOT: Same framing as the previous image (use it as the exact base). Amin has lowered his hands, water dripping from his chin, jaw and eyelashes, his eyes open, clear and calm, looking slightly toward Youcef with gratitude, his face visibly refreshed and peaceful. Youcef, out of focus behind him, nods with an affectionate smile. Photorealistic live-action film still, natural 35mm lens look, soft natural film grain, real skin texture with pores and fine lines, no beauty retouching, believable fabric creases and wet-surface reflections, motivated practical lighting, accurate hands with five fingers each. Vertical 9:16 portrait. NEGATIVE: no 3D render, no CGI look, no illustration, no painting, no plastic or waxy skin, no HDR over-sharpening, no landscape or square format, no identity drift, no face change, no age change, no clothing change, no extra people, no duplicate bodies, no extra fingers, no distorted hands, no floating objects, no mirrored layout, no readable text, no logos, no brand labels, no watermark, no subtitles.
```


#### المشهد 08 — الوقوف بين يدي الله


##### 🖼️ SC08_A — إطار البداية

**كيفاش راح تكون الصورة:** لقطة متوسطة كاملة من **الخلف قليلًا لليمين** على بعد 2.5 م بمستوى العين، تنظر نحو جدار القبلة والمحراب البعيد في الوسط. يوسف على **يسار** الكادر وأمين على **يمينه**، واقفان حافيين كتفًا بكتف على نفس الخط الكريمي من السجاد الأخضر. يوسف يميل برأسه قليلًا لليمين ليهمس لأمين. أمين بقلنسوته السوداء المرفوعة الأكمام فوق المرفقين والقلنسوة للخلف ويداه بجانبيه. ضوء الفجر الأزرق الناعم من النوافذ العالية.

**ارفع معها (بالترتيب):** `REF_ENV_PRAYER`، `REF_YOUCEF`، `REF_AMIN`

```text
Use the uploaded reference images listed in the scene header, in that order (the FIRST one is the portrait base). Reproduce the exact faces, clothes, location layout and props. AMIN: 24-year-old Algerian young man, pale olive skin, slightly gaunt cheeks, dark messy wavy hair, patchy five-day stubble, dark circles under sorrowful brown eyes, oversized faded black hoodie with the hood DOWN over a dark grey T-shirt, dark charcoal washed jeans, worn scuffed sneakers (street). In the mosque: the same hoodie with the sleeves pushed above the elbows, barefoot. YOUCEF: 27-year-old Algerian young man, warm medium-olive skin, full neatly trimmed black beard, short neat black hair, gentle brown eyes, calm compassionate face, a clean cream-beige Algerian cotton qamis (long, light embroidery at the collar) over simple trousers, leather sandals in the street, barefoot in the mosque. LOCATION LOCK (REF_ENV_PRAYER, never change): a modest Algerian mosque prayer hall. The qibla wall at the far end with a white plaster horseshoe mihrab in its center and a wooden minbar to the right of the mihrab; a green wool prayer carpet with cream stripes running PARALLEL to the qibla wall; two white plaster columns left and right; high arched windows in the right wall letting in soft cool-blue dawn light with a first warm tint; warm pendant lamps; the hall is empty except the two men. The men stand and pray on the SAME cream stripe, shoulder to shoulder, feet aligned. Praying positions: Amin stands on the RIGHT of Youcef (Youcef is the imam). From a camera BEHIND them: Youcef is on the LEFT of the frame and Amin on the RIGHT. From a camera IN FRONT of them (facing them): Amin is on the LEFT of the frame and Youcef on the RIGHT. SHOT: Medium full shot from slightly BEHIND and to the right, about 2.5 m back at eye level, looking toward the qibla wall with the mihrab centered in the distance. Youcef is on the LEFT of the frame and Amin on the RIGHT, standing barefoot shoulder to shoulder on the same cream stripe of the green carpet. Youcef turns his head slightly to his right to whisper to Amin. Amin's black hoodie sleeves are pushed above his elbows, hood down, hands at his sides. Soft cool-blue dawn light from the high windows. Photorealistic live-action film still, natural 35mm lens look, soft natural film grain, real skin texture with pores and fine lines, no beauty retouching, believable fabric creases and wet-surface reflections, motivated practical lighting, accurate hands with five fingers each. Vertical 9:16 portrait. NEGATIVE: no 3D render, no CGI look, no illustration, no painting, no plastic or waxy skin, no HDR over-sharpening, no landscape or square format, no identity drift, no face change, no age change, no clothing change, no extra people, no duplicate bodies, no extra fingers, no distorted hands, no floating objects, no mirrored layout, no readable text, no logos, no brand labels, no watermark, no subtitles.
```


##### 🖼️ SC08_B — إطار النهاية

**كيفاش راح تكون الصورة:** نفس الكادر والأماكن. الاثنان رفعا يديهما للتكبير ثم وضعا اليد اليمنى على اليسرى على الصدر، والعينان مخفوضتان نحو موضع السجود، سكون تام وكتفاهما متلاصقان وقدماهما متوازيتان. (يوسف يسار الكادر وأمين يمينه، بلا أي تبديل).

**ارفع معها (بالترتيب):** `REF_ENV_PRAYER`، `REF_YOUCEF`، `REF_AMIN`، + صورة SC08_A كأم

```text
Use the uploaded reference images listed in the scene header, in that order (the FIRST one is the portrait base). Reproduce the exact faces, clothes, location layout and props. AMIN: 24-year-old Algerian young man, pale olive skin, slightly gaunt cheeks, dark messy wavy hair, patchy five-day stubble, dark circles under sorrowful brown eyes, oversized faded black hoodie with the hood DOWN over a dark grey T-shirt, dark charcoal washed jeans, worn scuffed sneakers (street). In the mosque: the same hoodie with the sleeves pushed above the elbows, barefoot. YOUCEF: 27-year-old Algerian young man, warm medium-olive skin, full neatly trimmed black beard, short neat black hair, gentle brown eyes, calm compassionate face, a clean cream-beige Algerian cotton qamis (long, light embroidery at the collar) over simple trousers, leather sandals in the street, barefoot in the mosque. LOCATION LOCK (REF_ENV_PRAYER, never change): a modest Algerian mosque prayer hall. The qibla wall at the far end with a white plaster horseshoe mihrab in its center and a wooden minbar to the right of the mihrab; a green wool prayer carpet with cream stripes running PARALLEL to the qibla wall; two white plaster columns left and right; high arched windows in the right wall letting in soft cool-blue dawn light with a first warm tint; warm pendant lamps; the hall is empty except the two men. The men stand and pray on the SAME cream stripe, shoulder to shoulder, feet aligned. Praying positions: Amin stands on the RIGHT of Youcef (Youcef is the imam). From a camera BEHIND them: Youcef is on the LEFT of the frame and Amin on the RIGHT. From a camera IN FRONT of them (facing them): Amin is on the LEFT of the frame and Youcef on the RIGHT. SHOT: Same framing and positions as the previous image (use it as the exact base). Both have raised their hands for the opening takbir and now stand with the right hand folded over the left on the chest, eyes lowered to the place of prostration, perfect stillness, shoulders aligned, feet parallel. Youcef stays on the LEFT of the frame and Amin on the RIGHT. Photorealistic live-action film still, natural 35mm lens look, soft natural film grain, real skin texture with pores and fine lines, no beauty retouching, believable fabric creases and wet-surface reflections, motivated practical lighting, accurate hands with five fingers each. Vertical 9:16 portrait. NEGATIVE: no 3D render, no CGI look, no illustration, no painting, no plastic or waxy skin, no HDR over-sharpening, no landscape or square format, no identity drift, no face change, no age change, no clothing change, no extra people, no duplicate bodies, no extra fingers, no distorted hands, no floating objects, no mirrored layout, no readable text, no logos, no brand labels, no watermark, no subtitles.
```


#### المشهد 09 — السجود الطويل


##### 🖼️ SC09_A — إطار البداية

**كيفاش راح تكون الصورة:** لقطة **أمامية منخفضة** من جهة القبلة (الكاميرا على ارتفاع 30 سم فوق السجاد وعلى بعد 3 م وتنظر نحوهما). بسبب مواجهة الكاميرا لهما: **أمين على يسار الكادر ويوسف على يمينه** (انقلاب طبيعي). كلاهما في السجود جنبًا إلى جنب على نفس الخط: الجبهة والأنف على السجاد، الكفان مبسوطتان بجانب الرأس، والمرفقان مرفوعان عن الأرض. بقعة ضوء فجر ناعمة تنزل على أمين.

**ارفع معها (بالترتيب):** `REF_ENV_PRAYER`، `REF_YOUCEF`، `REF_AMIN`

```text
Use the uploaded reference images listed in the scene header, in that order (the FIRST one is the portrait base). Reproduce the exact faces, clothes, location layout and props. AMIN: 24-year-old Algerian young man, pale olive skin, slightly gaunt cheeks, dark messy wavy hair, patchy five-day stubble, dark circles under sorrowful brown eyes, oversized faded black hoodie with the hood DOWN over a dark grey T-shirt, dark charcoal washed jeans, worn scuffed sneakers (street). In the mosque: the same hoodie with the sleeves pushed above the elbows, barefoot. YOUCEF: 27-year-old Algerian young man, warm medium-olive skin, full neatly trimmed black beard, short neat black hair, gentle brown eyes, calm compassionate face, a clean cream-beige Algerian cotton qamis (long, light embroidery at the collar) over simple trousers, leather sandals in the street, barefoot in the mosque. LOCATION LOCK (REF_ENV_PRAYER, never change): a modest Algerian mosque prayer hall. The qibla wall at the far end with a white plaster horseshoe mihrab in its center and a wooden minbar to the right of the mihrab; a green wool prayer carpet with cream stripes running PARALLEL to the qibla wall; two white plaster columns left and right; high arched windows in the right wall letting in soft cool-blue dawn light with a first warm tint; warm pendant lamps; the hall is empty except the two men. The men stand and pray on the SAME cream stripe, shoulder to shoulder, feet aligned. Praying positions: Amin stands on the RIGHT of Youcef (Youcef is the imam). From a camera BEHIND them: Youcef is on the LEFT of the frame and Amin on the RIGHT. From a camera IN FRONT of them (facing them): Amin is on the LEFT of the frame and Youcef on the RIGHT. SHOT: Low FRONT view from the qibla side: the camera sits 30 cm above the carpet, about 3 m in front of the two men, facing back toward them. Because we face them, AMIN is on the LEFT of the frame and YOUCEF on the RIGHT. Both are in sujood side by side on the same stripe: foreheads and noses on the carpet, palms flat beside their heads, elbows lifted off the floor. A soft pool of dawn light falls over Amin. Photorealistic live-action film still, natural 35mm lens look, soft natural film grain, real skin texture with pores and fine lines, no beauty retouching, believable fabric creases and wet-surface reflections, motivated practical lighting, accurate hands with five fingers each. Vertical 9:16 portrait. NEGATIVE: no 3D render, no CGI look, no illustration, no painting, no plastic or waxy skin, no HDR over-sharpening, no landscape or square format, no identity drift, no face change, no age change, no clothing change, no extra people, no duplicate bodies, no extra fingers, no distorted hands, no floating objects, no mirrored layout, no readable text, no logos, no brand labels, no watermark, no subtitles.
```


##### 🖼️ SC09_B — إطار النهاية

**كيفاش راح تكون الصورة:** نفس الكادر الأمامي المنخفض. يوسف (يمين الكادر) صار جالسًا معتدلًا في جلسة التشهد، يداه على فخذيه وسبابته اليمنى مرفوعة، وفي عينيه ركن خاطف نحو أمين. أمين (يسار الكادر) ما زال في السجود، بلا حركة، في سكون كامل.

**ارفع معها (بالترتيب):** `REF_ENV_PRAYER`، `REF_YOUCEF`، `REF_AMIN`، + صورة SC09_A كأم

```text
Use the uploaded reference images listed in the scene header, in that order (the FIRST one is the portrait base). Reproduce the exact faces, clothes, location layout and props. AMIN: 24-year-old Algerian young man, pale olive skin, slightly gaunt cheeks, dark messy wavy hair, patchy five-day stubble, dark circles under sorrowful brown eyes, oversized faded black hoodie with the hood DOWN over a dark grey T-shirt, dark charcoal washed jeans, worn scuffed sneakers (street). In the mosque: the same hoodie with the sleeves pushed above the elbows, barefoot. YOUCEF: 27-year-old Algerian young man, warm medium-olive skin, full neatly trimmed black beard, short neat black hair, gentle brown eyes, calm compassionate face, a clean cream-beige Algerian cotton qamis (long, light embroidery at the collar) over simple trousers, leather sandals in the street, barefoot in the mosque. LOCATION LOCK (REF_ENV_PRAYER, never change): a modest Algerian mosque prayer hall. The qibla wall at the far end with a white plaster horseshoe mihrab in its center and a wooden minbar to the right of the mihrab; a green wool prayer carpet with cream stripes running PARALLEL to the qibla wall; two white plaster columns left and right; high arched windows in the right wall letting in soft cool-blue dawn light with a first warm tint; warm pendant lamps; the hall is empty except the two men. The men stand and pray on the SAME cream stripe, shoulder to shoulder, feet aligned. Praying positions: Amin stands on the RIGHT of Youcef (Youcef is the imam). From a camera BEHIND them: Youcef is on the LEFT of the frame and Amin on the RIGHT. From a camera IN FRONT of them (facing them): Amin is on the LEFT of the frame and Youcef on the RIGHT. SHOT: Same low front framing as the previous image (use it as the exact base). Youcef (RIGHT of the frame) now sits upright in the tashahhud posture, hands on his thighs, his right index finger lifted, with a brief sideways glance toward Amin. Amin (LEFT of the frame) is still in sujood, motionless, in complete stillness. Photorealistic live-action film still, natural 35mm lens look, soft natural film grain, real skin texture with pores and fine lines, no beauty retouching, believable fabric creases and wet-surface reflections, motivated practical lighting, accurate hands with five fingers each. Vertical 9:16 portrait. NEGATIVE: no 3D render, no CGI look, no illustration, no painting, no plastic or waxy skin, no HDR over-sharpening, no landscape or square format, no identity drift, no face change, no age change, no clothing change, no extra people, no duplicate bodies, no extra fingers, no distorted hands, no floating objects, no mirrored layout, no readable text, no logos, no brand labels, no watermark, no subtitles.
```


#### المشهد 10 — حسن الخاتمة


##### 🖼️ SC10_A — إطار البداية

**كيفاش راح تكون الصورة:** لقطة أمامية منخفضة نفس كادر المشهد 9 (أمين يسار الكادر، يوسف يمينه). يوسف أنهى للتو التسليم إلى جهة **يمينه** (رأسه ملتفت نحو أمين) بابتسامة حانية، ويده اليمنى تمتد لتلمس **كتف أمين الأيسر** برفق. أمين ما زال في السجود.

**ارفع معها (بالترتيب):** `REF_ENV_PRAYER`، `REF_YOUCEF`، `REF_AMIN`

```text
Use the uploaded reference images listed in the scene header, in that order (the FIRST one is the portrait base). Reproduce the exact faces, clothes, location layout and props. AMIN: 24-year-old Algerian young man, pale olive skin, slightly gaunt cheeks, dark messy wavy hair, patchy five-day stubble, dark circles under sorrowful brown eyes, oversized faded black hoodie with the hood DOWN over a dark grey T-shirt, dark charcoal washed jeans, worn scuffed sneakers (street). In the mosque: the same hoodie with the sleeves pushed above the elbows, barefoot. YOUCEF: 27-year-old Algerian young man, warm medium-olive skin, full neatly trimmed black beard, short neat black hair, gentle brown eyes, calm compassionate face, a clean cream-beige Algerian cotton qamis (long, light embroidery at the collar) over simple trousers, leather sandals in the street, barefoot in the mosque. LOCATION LOCK (REF_ENV_PRAYER, never change): a modest Algerian mosque prayer hall. The qibla wall at the far end with a white plaster horseshoe mihrab in its center and a wooden minbar to the right of the mihrab; a green wool prayer carpet with cream stripes running PARALLEL to the qibla wall; two white plaster columns left and right; high arched windows in the right wall letting in soft cool-blue dawn light with a first warm tint; warm pendant lamps; the hall is empty except the two men. The men stand and pray on the SAME cream stripe, shoulder to shoulder, feet aligned. Praying positions: Amin stands on the RIGHT of Youcef (Youcef is the imam). From a camera BEHIND them: Youcef is on the LEFT of the frame and Amin on the RIGHT. From a camera IN FRONT of them (facing them): Amin is on the LEFT of the frame and Youcef on the RIGHT. SHOT: Low front framing, the same as the scene 9 frames: Amin on the LEFT of the frame, Youcef on the RIGHT. Youcef has just finished the taslim to his RIGHT (his head turned toward Amin) with a gentle affectionate smile, and his right hand reaches to lightly touch Amin's LEFT shoulder. Amin is still down in sujood. Photorealistic live-action film still, natural 35mm lens look, soft natural film grain, real skin texture with pores and fine lines, no beauty retouching, believable fabric creases and wet-surface reflections, motivated practical lighting, accurate hands with five fingers each. Vertical 9:16 portrait. NEGATIVE: no 3D render, no CGI look, no illustration, no painting, no plastic or waxy skin, no HDR over-sharpening, no landscape or square format, no identity drift, no face change, no age change, no clothing change, no extra people, no duplicate bodies, no extra fingers, no distorted hands, no floating objects, no mirrored layout, no readable text, no logos, no brand labels, no watermark, no subtitles.
```


##### 🖼️ SC10_B — لحظة الوسط (مرجع إضافي)

**كيفاش راح تكون الصورة:** نفس الكادر. جسد أمين مال بهدوء نحو يوسف (نحو يمين الكادر) واستقر على السجاد بجانبه، ووجهه ظاهر للكاميرا: عيناه مغمضتان بسلام، وملامح صافية، وابتسامة خفيفة نقية على شفتيه. ابتسامة يوسف تجمدت من إدراك الحقيقة ويداه على كتفي أمين.

**ارفع معها (بالترتيب):** `REF_ENV_PRAYER`، `REF_YOUCEF`، `REF_AMIN`، + صورة SC10_A كأم

```text
Use the uploaded reference images listed in the scene header, in that order (the FIRST one is the portrait base). Reproduce the exact faces, clothes, location layout and props. AMIN: 24-year-old Algerian young man, pale olive skin, slightly gaunt cheeks, dark messy wavy hair, patchy five-day stubble, dark circles under sorrowful brown eyes, oversized faded black hoodie with the hood DOWN over a dark grey T-shirt, dark charcoal washed jeans, worn scuffed sneakers (street). In the mosque: the same hoodie with the sleeves pushed above the elbows, barefoot. YOUCEF: 27-year-old Algerian young man, warm medium-olive skin, full neatly trimmed black beard, short neat black hair, gentle brown eyes, calm compassionate face, a clean cream-beige Algerian cotton qamis (long, light embroidery at the collar) over simple trousers, leather sandals in the street, barefoot in the mosque. LOCATION LOCK (REF_ENV_PRAYER, never change): a modest Algerian mosque prayer hall. The qibla wall at the far end with a white plaster horseshoe mihrab in its center and a wooden minbar to the right of the mihrab; a green wool prayer carpet with cream stripes running PARALLEL to the qibla wall; two white plaster columns left and right; high arched windows in the right wall letting in soft cool-blue dawn light with a first warm tint; warm pendant lamps; the hall is empty except the two men. The men stand and pray on the SAME cream stripe, shoulder to shoulder, feet aligned. Praying positions: Amin stands on the RIGHT of Youcef (Youcef is the imam). From a camera BEHIND them: Youcef is on the LEFT of the frame and Amin on the RIGHT. From a camera IN FRONT of them (facing them): Amin is on the LEFT of the frame and Youcef on the RIGHT. SHOT: Same framing as the previous image (use it as the exact base). Amin's body has gently slumped toward Youcef (toward the RIGHT of the frame) and rests on the carpet beside him, his face visible to the camera: eyes peacefully closed, serene skin, a faint pure smile on his lips. Youcef's smile has frozen in realization, his hands on Amin's shoulders. Photorealistic live-action film still, natural 35mm lens look, soft natural film grain, real skin texture with pores and fine lines, no beauty retouching, believable fabric creases and wet-surface reflections, motivated practical lighting, accurate hands with five fingers each. Vertical 9:16 portrait. NEGATIVE: no 3D render, no CGI look, no illustration, no painting, no plastic or waxy skin, no HDR over-sharpening, no landscape or square format, no identity drift, no face change, no age change, no clothing change, no extra people, no duplicate bodies, no extra fingers, no distorted hands, no floating objects, no mirrored layout, no readable text, no logos, no brand labels, no watermark, no subtitles.
```


##### 🖼️ SC10_C — إطار النهاية

**كيفاش راح تكون الصورة:** نفس الكادر. يوسف جالس يحتضن رأس أمين على حجره بلطف، دموع على خديه، ونظره مرفوع قليلًا للأعلى بدهشة وخشوع وانكسار هادئ. وجه أمين مطمئن بابتسامة خفيفة. ضوء فجر أزرق ذهبي ناعم على الاثنين، بلا مبالغة.

**ارفع معها (بالترتيب):** `REF_ENV_PRAYER`، `REF_YOUCEF`، `REF_AMIN`، + صورة SC10_B كأم

```text
Use the uploaded reference images listed in the scene header, in that order (the FIRST one is the portrait base). Reproduce the exact faces, clothes, location layout and props. AMIN: 24-year-old Algerian young man, pale olive skin, slightly gaunt cheeks, dark messy wavy hair, patchy five-day stubble, dark circles under sorrowful brown eyes, oversized faded black hoodie with the hood DOWN over a dark grey T-shirt, dark charcoal washed jeans, worn scuffed sneakers (street). In the mosque: the same hoodie with the sleeves pushed above the elbows, barefoot. YOUCEF: 27-year-old Algerian young man, warm medium-olive skin, full neatly trimmed black beard, short neat black hair, gentle brown eyes, calm compassionate face, a clean cream-beige Algerian cotton qamis (long, light embroidery at the collar) over simple trousers, leather sandals in the street, barefoot in the mosque. LOCATION LOCK (REF_ENV_PRAYER, never change): a modest Algerian mosque prayer hall. The qibla wall at the far end with a white plaster horseshoe mihrab in its center and a wooden minbar to the right of the mihrab; a green wool prayer carpet with cream stripes running PARALLEL to the qibla wall; two white plaster columns left and right; high arched windows in the right wall letting in soft cool-blue dawn light with a first warm tint; warm pendant lamps; the hall is empty except the two men. The men stand and pray on the SAME cream stripe, shoulder to shoulder, feet aligned. Praying positions: Amin stands on the RIGHT of Youcef (Youcef is the imam). From a camera BEHIND them: Youcef is on the LEFT of the frame and Amin on the RIGHT. From a camera IN FRONT of them (facing them): Amin is on the LEFT of the frame and Youcef on the RIGHT. SHOT: Same framing as the previous image (use it as the exact base). Youcef sits cradling Amin's head gently on his lap, tears on his cheeks, his gaze lifted slightly upward in awe, reverence and quiet heartbreak. Amin's face is peaceful with a faint smile. Soft cool-blue and gold dawn light over them both, subtle, not exaggerated. Photorealistic live-action film still, natural 35mm lens look, soft natural film grain, real skin texture with pores and fine lines, no beauty retouching, believable fabric creases and wet-surface reflections, motivated practical lighting, accurate hands with five fingers each. Vertical 9:16 portrait. NEGATIVE: no 3D render, no CGI look, no illustration, no painting, no plastic or waxy skin, no HDR over-sharpening, no landscape or square format, no identity drift, no face change, no age change, no clothing change, no extra people, no duplicate bodies, no extra fingers, no distorted hands, no floating objects, no mirrored layout, no readable text, no logos, no brand labels, no watermark, no subtitles.
```


---

## 5) البلوكات الشاملة للوكيل (ثلاث دفعات)

> كل دفعة في بلوك واحد تنسخه للوكيل مع رفع المراجع المذكورة. الوصف المشترك (الشخصيات والمكان والأسلوب) مكتوب مرة واحدة في أول البلوك.


### 🟦 الدفعة 1: الزقاق (SC01 → SC05، 8 صور)

**ارفع:** `REF_ENV_STREET` + `REF_AMIN` + `REF_YOUCEF`

```text
Generate 8 separate PORTRAIT 9:16 images (1080x1920), named SC01_A, SC02_A, SC02_B, SC03_A, SC04_A, SC04_B, SC05_A, SC05_B, for a photorealistic live-action short film. Every output MUST be vertical portrait 9:16. For each image attach ONLY the references listed in its header, in that order (the first is the portrait base). Reproduce the exact faces, clothes, location layout and props; do not redesign anything and do not mirror the layout. If a reference is missing, stop and tell me instead of inventing it. Generate in order and label each image with its name. For images marked 'previous image as base', also attach the image generated just before it and keep the framing and positions identical.

AMIN: 24-year-old Algerian young man, pale olive skin, slightly gaunt cheeks, dark messy wavy hair, patchy five-day stubble, dark circles under sorrowful brown eyes, oversized faded black hoodie with the hood DOWN over a dark grey T-shirt, dark charcoal washed jeans, worn scuffed sneakers (street). In the mosque: the same hoodie with the sleeves pushed above the elbows, barefoot. YOUCEF: 27-year-old Algerian young man, warm medium-olive skin, full neatly trimmed black beard, short neat black hair, gentle brown eyes, calm compassionate face, a clean cream-beige Algerian cotton qamis (long, light embroidery at the collar) over simple trousers, leather sandals in the street, barefoot in the mosque.

LOCATION LOCK (REF_ENV_STREET, never change): a narrow old alley in a working-class Algiers quarter in the last hour before dawn, still dark with a faint deep-blue glow at the top of the sky. Seen from across the alley at eye level: on the LEFT-center a tall old building wall with peeling plaster and a closed rolled-down metal shop shutter, with a raised concrete curb along its base; a tall pole with ONE dim warm sodium streetlamp above the curb at the center-left; damp cracked asphalt with small puddles reflecting the lamp; the alley continues to the RIGHT with a slight bend, and far away on the right a small arched doorway glows warm yellow-green (the mosque entrance), tiny and distant. Nothing else in the alley. Chilly air, very faint mist.

Photorealistic live-action film still, natural 35mm lens look, soft natural film grain, real skin texture with pores and fine lines, no beauty retouching, believable fabric creases and wet-surface reflections, motivated practical lighting, accurate hands with five fingers each. Vertical 9:16 portrait.
NEGATIVE: no 3D render, no CGI look, no illustration, no painting, no plastic or waxy skin, no HDR over-sharpening, no landscape or square format, no identity drift, no face change, no age change, no clothing change, no extra people, no duplicate bodies, no extra fingers, no distorted hands, no floating objects, no mirrored layout, no readable text, no logos, no brand labels, no watermark, no subtitles.

=== SC01_A — refs: REF_ENV_STREET, REF_AMIN ===
Low-angle medium close-up, slightly from below. Amin sits slumped on the raised concrete curb in front of the closed shop shutter under the dim sodium streetlamp. His right hand hangs between his knees holding a dark glass bottle with NO label whose base touches the pavement. His head is bowed in deep shame and regret, sunken eyes, hollow cheeks, hood down. Amber light from the lamp on one side of his face, deep shadow on the other. In the far right background, tiny and out of focus, the warm glow of the distant arched doorway.

=== SC02_A — refs: REF_ENV_STREET, REF_AMIN, REF_YOUCEF ===
Medium-wide shot across the alley at eye level (about 1.3 m). Amin sits on the curb in the right-center, bottle in his right hand, head bowed. At the LEFT edge of the frame, Youcef enters walking toward the right (toward the distant mosque glow), caught mid-stride, head turning toward Amin with immediate concern. Both fully visible, streetlamp above the curb, wet asphalt.

=== SC02_B — refs: REF_ENV_STREET, REF_AMIN, REF_YOUCEF, + صورة SC02_A كأم ===
Same framing and positions as the previous image (use it as the exact base). Youcef has stopped about 1.2 m in front of Amin, bent slightly at the waist, extending his open right hand toward him with a warm humble brotherly smile. Amin has lifted his head and looks up with wide startled eyes caught between defense and vulnerability, the bottle still held low in his right hand.

=== SC03_A — refs: REF_ENV_STREET, REF_AMIN, REF_YOUCEF ===
Over-the-shoulder medium close-up. The camera is behind Youcef's RIGHT shoulder at chest height, looking slightly down. The blurred cream qamis shoulder and the side of Youcef's head fill the RIGHT edge of the frame (his face is not visible). In sharp focus in the left-center: Amin's face, seated on the curb below, looking down and slightly away to the left, lips slightly parted as if about to speak, brows drawn together, eyes glistening with held-back tears. His right hand and the dark unlabeled bottle are visible low at the bottom edge. Lamp light from the upper left, shallow depth of field.

=== SC04_A — refs: REF_ENV_STREET, REF_YOUCEF, REF_AMIN ===
Medium close-up at Amin's eye level. Youcef is lowering himself, his right knee about to touch the wet ground, his face level with Amin's, his right hand extended toward Amin's LEFT shoulder but not touching it yet, an expression of calm compassion. At the left foreground edge, out of focus: Amin's bowed head and slumped shoulder in the black hoodie. Warm lamp light from the upper left, a faint cool blue glow behind them.

=== SC04_B — refs: REF_ENV_STREET, REF_YOUCEF, REF_AMIN, + صورة SC04_A كأم ===
Same framing as the previous image (use it as the exact base). Youcef kneels on one knee on the damp ground, his right hand resting on Amin's LEFT shoulder, a radiant loving smile of encouragement, his eyes looking into Amin's. Amin stays at the left foreground edge, out of focus, head still bowed.

=== SC05_A — refs: REF_ENV_STREET, REF_AMIN, REF_YOUCEF ===
Medium-wide shot across the alley at eye level, same direction as the scene 2 frames. Amin sits on the curb in the right-center; his right hand has just opened and the dark unlabeled glass bottle is slipping from it, tipping, about to roll toward the gutter. Youcef stands beside him on the LEFT, leaning slightly, his right hand extended down toward Amin's left hand. Both fully visible, streetlamp above.

=== SC05_B — refs: REF_ENV_STREET, REF_AMIN, REF_YOUCEF, + صورة SC05_A كأم ===
Same framing as the previous image (use it as the exact base). Both now stand up side by side: Amin grips Youcef's right hand tightly with both of his hands, Youcef's left arm supports Amin's back. They have turned to the RIGHT toward the distant warm arched doorway, seen in three-quarter back view, taking the first step together. The dark unlabeled bottle lies on its side at the curb behind them, no liquid pool.
```


### 🟩 الدفعة 2: الميضأة (SC06 → SC07، 4 صور)

**ارفع:** `REF_ENV_ABLUTION` + `REF_AMIN` + `REF_YOUCEF`

```text
Generate 4 separate PORTRAIT 9:16 images (1080x1920), named SC06_A, SC06_B, SC07_A, SC07_B, for a photorealistic live-action short film. Every output MUST be vertical portrait 9:16. For each image attach ONLY the references listed in its header, in that order (the first is the portrait base). Reproduce the exact faces, clothes, location layout and props; do not redesign anything and do not mirror the layout. If a reference is missing, stop and tell me instead of inventing it. Generate in order and label each image with its name. For images marked 'previous image as base', also attach the image generated just before it and keep the framing and positions identical.

AMIN: 24-year-old Algerian young man, pale olive skin, slightly gaunt cheeks, dark messy wavy hair, patchy five-day stubble, dark circles under sorrowful brown eyes, oversized faded black hoodie with the hood DOWN over a dark grey T-shirt, dark charcoal washed jeans, worn scuffed sneakers (street). In the mosque: the same hoodie with the sleeves pushed above the elbows, barefoot. YOUCEF: 27-year-old Algerian young man, warm medium-olive skin, full neatly trimmed black beard, short neat black hair, gentle brown eyes, calm compassionate face, a clean cream-beige Algerian cotton qamis (long, light embroidery at the collar) over simple trousers, leather sandals in the street, barefoot in the mosque.

LOCATION LOCK (REF_ENV_ABLUTION, never change): a clean traditional Algerian mosque ablution room. A long wall tiled in turquoise-and-white zellige with a row of four polished chrome faucets about 70 cm above a long low smooth stone bench that runs along the wall; a narrow marble drain trough on the damp grey stone floor in front of the bench; soft white ceiling light plus warm wall lamps; faint steam. SEATING: Youcef sits at the LEFT faucet and Amin at the next faucet to his RIGHT, side by side, both facing the faucets.

Photorealistic live-action film still, natural 35mm lens look, soft natural film grain, real skin texture with pores and fine lines, no beauty retouching, believable fabric creases and wet-surface reflections, motivated practical lighting, accurate hands with five fingers each. Vertical 9:16 portrait.
NEGATIVE: no 3D render, no CGI look, no illustration, no painting, no plastic or waxy skin, no HDR over-sharpening, no landscape or square format, no identity drift, no face change, no age change, no clothing change, no extra people, no duplicate bodies, no extra fingers, no distorted hands, no floating objects, no mirrored layout, no readable text, no logos, no brand labels, no watermark, no subtitles.

=== SC06_A — refs: REF_ENV_ABLUTION, REF_YOUCEF, REF_AMIN ===
Medium two-shot from the LEFT end of the row of faucets, angled slightly into the room, eye level. Youcef, nearest to the camera, sits at the left faucet with his qamis sleeves pushed above his elbows, washing his hands under the running water, droplets on his hands. Amin sits beside him at the next faucet on his right in his black hoodie with the sleeves still DOWN, watching Youcef with intense childlike attention. Both in three-quarter profile facing the faucets. Wet turquoise zellige tiles and chrome faucets gleam.

=== SC06_B — refs: REF_ENV_ABLUTION, REF_YOUCEF, REF_AMIN, + صورة SC06_A كأم ===
Same framing as the previous image (use it as the exact base). Youcef has turned his head toward Amin with water droplets on his beard and a calm teaching smile, his wet right hand raised with three fingers extended to show 'three times'. Amin listens and nods, starting to push the sleeves of his black hoodie up toward his elbows.

=== SC07_A — refs: REF_ENV_ABLUTION, REF_AMIN, REF_YOUCEF ===
Close-up on Amin at his faucet. His black hoodie sleeves are pushed above his elbows, his cupped hands are full of clear water raised just below his chin, eyes closed, about to wash his face; his face is pale and tired. In the soft-focus background on the left, Youcef watches him with a warm proud brotherly smile. Zellige tiles and chrome faucets softly out of focus.

=== SC07_B — refs: REF_ENV_ABLUTION, REF_AMIN, REF_YOUCEF, + صورة SC07_A كأم ===
Same framing as the previous image (use it as the exact base). Amin has lowered his hands, water dripping from his chin, jaw and eyelashes, his eyes open, clear and calm, looking slightly toward Youcef with gratitude, his face visibly refreshed and peaceful. Youcef, out of focus behind him, nods with an affectionate smile.
```


### 🟨 الدفعة 3: قاعة الصلاة (SC08 → SC10، 7 صور)

**ارفع:** `REF_ENV_PRAYER` + `REF_AMIN` + `REF_YOUCEF`

```text
Generate 7 separate PORTRAIT 9:16 images (1080x1920), named SC08_A, SC08_B, SC09_A, SC09_B, SC10_A, SC10_B, SC10_C, for a photorealistic live-action short film. Every output MUST be vertical portrait 9:16. For each image attach ONLY the references listed in its header, in that order (the first is the portrait base). Reproduce the exact faces, clothes, location layout and props; do not redesign anything and do not mirror the layout. If a reference is missing, stop and tell me instead of inventing it. Generate in order and label each image with its name. For images marked 'previous image as base', also attach the image generated just before it and keep the framing and positions identical.

AMIN: 24-year-old Algerian young man, pale olive skin, slightly gaunt cheeks, dark messy wavy hair, patchy five-day stubble, dark circles under sorrowful brown eyes, oversized faded black hoodie with the hood DOWN over a dark grey T-shirt, dark charcoal washed jeans, worn scuffed sneakers (street). In the mosque: the same hoodie with the sleeves pushed above the elbows, barefoot. YOUCEF: 27-year-old Algerian young man, warm medium-olive skin, full neatly trimmed black beard, short neat black hair, gentle brown eyes, calm compassionate face, a clean cream-beige Algerian cotton qamis (long, light embroidery at the collar) over simple trousers, leather sandals in the street, barefoot in the mosque.

LOCATION LOCK (REF_ENV_PRAYER, never change): a modest Algerian mosque prayer hall. The qibla wall at the far end with a white plaster horseshoe mihrab in its center and a wooden minbar to the right of the mihrab; a green wool prayer carpet with cream stripes running PARALLEL to the qibla wall; two white plaster columns left and right; high arched windows in the right wall letting in soft cool-blue dawn light with a first warm tint; warm pendant lamps; the hall is empty except the two men. The men stand and pray on the SAME cream stripe, shoulder to shoulder, feet aligned. Praying positions: Amin stands on the RIGHT of Youcef (Youcef is the imam). From a camera BEHIND them: Youcef is on the LEFT of the frame and Amin on the RIGHT. From a camera IN FRONT of them (facing them): Amin is on the LEFT of the frame and Youcef on the RIGHT.

Photorealistic live-action film still, natural 35mm lens look, soft natural film grain, real skin texture with pores and fine lines, no beauty retouching, believable fabric creases and wet-surface reflections, motivated practical lighting, accurate hands with five fingers each. Vertical 9:16 portrait.
NEGATIVE: no 3D render, no CGI look, no illustration, no painting, no plastic or waxy skin, no HDR over-sharpening, no landscape or square format, no identity drift, no face change, no age change, no clothing change, no extra people, no duplicate bodies, no extra fingers, no distorted hands, no floating objects, no mirrored layout, no readable text, no logos, no brand labels, no watermark, no subtitles.

=== SC08_A — refs: REF_ENV_PRAYER, REF_YOUCEF, REF_AMIN ===
Medium full shot from slightly BEHIND and to the right, about 2.5 m back at eye level, looking toward the qibla wall with the mihrab centered in the distance. Youcef is on the LEFT of the frame and Amin on the RIGHT, standing barefoot shoulder to shoulder on the same cream stripe of the green carpet. Youcef turns his head slightly to his right to whisper to Amin. Amin's black hoodie sleeves are pushed above his elbows, hood down, hands at his sides. Soft cool-blue dawn light from the high windows.

=== SC08_B — refs: REF_ENV_PRAYER, REF_YOUCEF, REF_AMIN, + صورة SC08_A كأم ===
Same framing and positions as the previous image (use it as the exact base). Both have raised their hands for the opening takbir and now stand with the right hand folded over the left on the chest, eyes lowered to the place of prostration, perfect stillness, shoulders aligned, feet parallel. Youcef stays on the LEFT of the frame and Amin on the RIGHT.

=== SC09_A — refs: REF_ENV_PRAYER, REF_YOUCEF, REF_AMIN ===
Low FRONT view from the qibla side: the camera sits 30 cm above the carpet, about 3 m in front of the two men, facing back toward them. Because we face them, AMIN is on the LEFT of the frame and YOUCEF on the RIGHT. Both are in sujood side by side on the same stripe: foreheads and noses on the carpet, palms flat beside their heads, elbows lifted off the floor. A soft pool of dawn light falls over Amin.

=== SC09_B — refs: REF_ENV_PRAYER, REF_YOUCEF, REF_AMIN, + صورة SC09_A كأم ===
Same low front framing as the previous image (use it as the exact base). Youcef (RIGHT of the frame) now sits upright in the tashahhud posture, hands on his thighs, his right index finger lifted, with a brief sideways glance toward Amin. Amin (LEFT of the frame) is still in sujood, motionless, in complete stillness.

=== SC10_A — refs: REF_ENV_PRAYER, REF_YOUCEF, REF_AMIN ===
Low front framing, the same as the scene 9 frames: Amin on the LEFT of the frame, Youcef on the RIGHT. Youcef has just finished the taslim to his RIGHT (his head turned toward Amin) with a gentle affectionate smile, and his right hand reaches to lightly touch Amin's LEFT shoulder. Amin is still down in sujood.

=== SC10_B — refs: REF_ENV_PRAYER, REF_YOUCEF, REF_AMIN, + صورة SC10_A كأم ===
Same framing as the previous image (use it as the exact base). Amin's body has gently slumped toward Youcef (toward the RIGHT of the frame) and rests on the carpet beside him, his face visible to the camera: eyes peacefully closed, serene skin, a faint pure smile on his lips. Youcef's smile has frozen in realization, his hands on Amin's shoulders.

=== SC10_C — refs: REF_ENV_PRAYER, REF_YOUCEF, REF_AMIN, + صورة SC10_B كأم ===
Same framing as the previous image (use it as the exact base). Youcef sits cradling Amin's head gently on his lap, tears on his cheeks, his gaze lifted slightly upward in awe, reverence and quiet heartbreak. Amin's face is peaceful with a faint smile. Soft cool-blue and gold dawn light over them both, subtle, not exaggerated.
```


---

## 6) جدول الحوار مع الترجمة (ماشي داخل البرومبتات)

| المشهد | المتحدث | الحوار المشكول | المعنى | التوقيت |
|---|---|---|---|---|
| 1 | — | بلا حوار (تنفس وأنفاس مرتجفة) | — | — |
| 2 | يوسف | «السَّلَامُ عَلَيْكُمْ يَا خُويَا... وَاشْ رَاكْ؟» | السلام عليكم يا أخي، كيف حالك؟ | 4.0–6.0 |
| 3 | يوسف (صوت) | «الْفَجْرْ قْرَّبْ يَا خُويَا... تْجِي مَعَايَ لْلْمَسْجِدْ؟» | الفجر قرب يا أخي، تجي معي للمسجد؟ | 0.3–3.2 |
| 3 | أمين | «وَعَلَيْكُمْ السَّلَامْ... أَنَا أَمِينْ. رَانِي مْوَسَّخْ، مَا نَصْلَحْشْ نَدْخَلْ لْبِيتْ رَبِّي.» | وعليكم السلام، أنا أمين. أنا موسّخ ولا أصلح لدخول بيت الله | 3.4–8.0 |
| 4 | يوسف | «رَبِّي يَغْفَرْ كُلَّشْ يَا أَمِينْ... بِيتْ رَبِّي مَفْتُوحْ لْلتَّايْبِينْ. نُوضْ مَعَايَ يَا خُويَا.» | الله يغفر كل شيء يا أمين، بيت الله مفتوح للتائبين. قم معي يا أخي | 2.5–8.0 |
| 5 | أمين | «يَا رَبّْ... بِسْمِ اللهْ.» | يا رب... بسم الله | 3.2–4.5 |
| 5 | يوسف | «تَوَكَّلْ عَلَى رَبِّي يَا أَمِينْ.» | توكل على ربي يا أمين | 5.0–6.5 |
| 6 | يوسف | «بِسْمِ اللهْ... نَبْدَاوْ بِلِيدِينْ، تْلَاتْ مَرَّاتْ. هَاذِي سُنَّةْ النَّبِيّْ، صَلَّى اللهُ عَلَيْهِ وَسَلَّمْ.» | بسم الله، نبدأ باليدين ثلاث مرات. هذه سنة النبي ﷺ | 3.0–8.2 |
| 7 | أمين (همسًا) | «أَشْهَدُ أَنْ لَا إِلَهَ إِلَّا اللهُ وَحْدَهُ لَا شَرِيكَ لَهُ، وَأَشْهَدُ أَنَّ مُحَمَّدًا عَبْدُهُ وَرَسُولُهُ.» | الشهادة كاملة بعد الوضوء | 5.2–9.5 |
| 8 | يوسف (همسًا) | «نْصَلُّو رَكْعَتِينْ... تَبْعَنِي بَرْكْ، وَاسْتَحْضَرْ عَظَمَةْ رَبِّي.» | نصلي ركعتين، اتبعني واستحضر عظمة ربي | 1.0–3.8 |
| 8 | يوسف | «اللهُ أَكْبَرْ.» | التكبير | 6.0–7.5 |
| 9 | يوسف (همس غير مسموع) | «التَّحِيَّاتُ لِلَّهِ وَالصَّلَوَاتُ وَالطَّيِّبَاتُ...» | التشهد | 4.5–10 |
| 10 | يوسف | «أَمِينْ؟ خَلْصَتْ الصَّلَاةْ يَا خُويَا...» | أمين؟ خلصت الصلاة يا أخي | 1.5–3.0 |
| 10 | يوسف (باكيًا) | «إِنَّا لِلَّهِ وَإِنَّا إِلَيْهِ رَاجِعُونَ... هَنِيئًا لِيكْ.» | إنا لله وإنا إليه راجعون... هنيئًا لك | 6.3–10.0 |

> **ملاحظة:** إذا غلط الصوت في آية أو ذكر، **أعد التوليد** أو ولّد المقطع بلا كلام وركّب التلاوة صوتيًا في CapCut.


---

## 7) برومبتات الفيديو (Google Flow) — مقطع بمقطع

> كل بلوك مستقل. ارفع الصور المذكورة (الإطار الأول والأخير) وانسخ.


### 🎬 SC01 (الإطار الأول فقط: SC01_A)

```text
Create a photorealistic live-action scene for the Algerian short film “Al-Tawba”. Duration exactly 10 seconds. Vertical 9:16 only (1080x1920).

FRAMES: Use the provided FIRST FRAME as the exact opening frame (there is no last frame; follow the action below). Keep faces, clothes, location layout, props and light direction identical to the frames.

CONTINUITY: AMIN: 24-year-old Algerian young man, pale olive skin, slightly gaunt cheeks, dark messy wavy hair, patchy five-day stubble, dark circles under sorrowful brown eyes, oversized faded black hoodie with the hood DOWN over a dark grey T-shirt, dark charcoal washed jeans, worn scuffed sneakers (street). In the mosque: the same hoodie with the sleeves pushed above the elbows, barefoot. The alley, closed shutter, curb, single streetlamp, puddles and the tiny glowing arched doorway on the right stay exactly as in the frames. The bottle is a dark glass bottle with NO label.

ACTION AND TIMING:
- 0.0-3.5s: Amin sits almost frozen on the curb, staring blankly at the wet asphalt between his sneakers, the unlabeled dark glass bottle loose in his right hand, its base resting on the pavement. His chest rises with one slow, heavy, tired breath.
- 3.5-7.0s: He blinks slowly; a single tear wells in his left eye; his fingers tremble slightly around the neck of the bottle; he lowers his head a little more and closes his eyes in deep self-reproach.
- 7.0-10.0s: A cold breeze lightly stirs his hair and hoodie. He swallows hard, his jaw tightens, and he stays motionless, overwhelmed.

DIALOGUE:
No dialogue. Total silence from the character except heavy trembling breath through the nose around 4.0-5.5s.
Natural Algerian Darja with an urban Algerian accent, spoken by native Algerian voices (the Quranic and prophetic phrases in clear classical Arabic). Never Egyptian, Gulf or Syrian. Pronounce the words exactly as written, including the sukun marks, without adding, translating or rewriting words. Only the named speaker moves his lips; every other face stays still. No overlapping lines.

CAMERA: Locked-off tripod shot with at most a very slow, barely visible push-in (about 3 percent) over the 10 seconds. No cuts, no pans, no handheld shake, no zoom jumps, no reframing. Faces and hands always stay inside the frame.

PERFORMANCE: Subtle natural micro-expressions, real blinks, believable breathing, realistic hands with correct fingers, natural weight and timing of body movement. Restrained emotion, nothing theatrical.

SOUND (diegetic only): Cold night wind softly through the alley, a faint distant tire hiss on wet road, one small glass-on-concrete clink as the bottle touches the curb at about 2.0s, a heavy low sigh. Dialogue clearly in front of the ambience.

END FRAME: Amin still seated, head lower, eyes closed, bottle still in his right hand.

NEGATIVE: no horizontal or square format; no cuts, no pans, no handheld shake, no fast zooms; no morphing, no identity drift, no new people, no extra fingers, no warped hands, no distorted faces; no objects teleporting, duplicating or vanishing (the dark glass bottle never changes shape and never spills a puddle); no readable text, no subtitles, no logos, no watermark; NO MUSIC OF ANY KIND, no score, no humming, no choir; no melodrama.
```


### 🎬 SC02 (SC02_A ← SC02_B)

```text
Create a photorealistic live-action scene for the Algerian short film “Al-Tawba”. Duration exactly 10 seconds. Vertical 9:16 only (1080x1920).

FRAMES: Use the provided FIRST FRAME (SC02_A) as the exact opening frame and the provided LAST FRAME (SC02_B) as the exact closing frame. Keep faces, clothes, location layout, props and light direction identical to the frames.

CONTINUITY: AMIN: 24-year-old Algerian young man, pale olive skin, slightly gaunt cheeks, dark messy wavy hair, patchy five-day stubble, dark circles under sorrowful brown eyes, oversized faded black hoodie with the hood DOWN over a dark grey T-shirt, dark charcoal washed jeans, worn scuffed sneakers (street). In the mosque: the same hoodie with the sleeves pushed above the elbows, barefoot. YOUCEF: 27-year-old Algerian young man, warm medium-olive skin, full neatly trimmed black beard, short neat black hair, gentle brown eyes, calm compassionate face, a clean cream-beige Algerian cotton qamis (long, light embroidery at the collar) over simple trousers, leather sandals in the street, barefoot in the mosque. The alley, closed shutter, curb, single streetlamp, puddles and the tiny glowing arched doorway on the right stay exactly as in the frames. The bottle is a dark glass bottle with NO label. Youcef enters from the LEFT edge walking toward the RIGHT; Amin stays seated on the curb with the bottle in his right hand.

ACTION AND TIMING:
- 0.0-3.0s: Youcef walks into frame from the left with measured dignified steps, notices Amin on the curb, slows down and stops about 1.2 m in front of him.
- 3.0-6.5s: Youcef bends slightly at the waist and extends his open right hand toward Amin with a warm brotherly smile. He speaks his greeting between 4.0s and 6.0s.
- 6.5-10.0s: Amin flinches slightly, slowly lifts his chin, his eyes go to Youcef's hand and then up to Youcef's face, frozen between disbelief and embarrassment, lips slightly parted, no words.

DIALOGUE:
يوسف: «السَّلَامُ عَلَيْكُمْ يَا خُويَا... وَاشْ رَاكْ؟»
Natural Algerian Darja with an urban Algerian accent, spoken by native Algerian voices (the Quranic and prophetic phrases in clear classical Arabic). Never Egyptian, Gulf or Syrian. Pronounce the words exactly as written, including the sukun marks, without adding, translating or rewriting words. Only the named speaker moves his lips; every other face stays still. No overlapping lines.

CAMERA: Locked-off tripod shot with at most a very slow, barely visible push-in (about 3 percent) over the 10 seconds. No cuts, no pans, no handheld shake, no zoom jumps, no reframing. Faces and hands always stay inside the frame.

PERFORMANCE: Subtle natural micro-expressions, real blinks, believable breathing, realistic hands with correct fingers, natural weight and timing of body movement. Restrained emotion, nothing theatrical.

SOUND (diegetic only): Soft footsteps of leather sandals on damp asphalt stopping at about 2.8s, the rustle of cotton cloth, a clear warm greeting with natural street reverb, the quiet night hum. Dialogue clearly in front of the ambience.

END FRAME: Youcef bent slightly with his right hand extended, Amin looking up with startled eyes, exactly the LAST FRAME.

NEGATIVE: no horizontal or square format; no cuts, no pans, no handheld shake, no fast zooms; no morphing, no identity drift, no new people, no extra fingers, no warped hands, no distorted faces; no objects teleporting, duplicating or vanishing (the dark glass bottle never changes shape and never spills a puddle); no readable text, no subtitles, no logos, no watermark; NO MUSIC OF ANY KIND, no score, no humming, no choir; no melodrama.
```


### 🎬 SC03 (الإطار الأول فقط: SC03_A)

```text
Create a photorealistic live-action scene for the Algerian short film “Al-Tawba”. Duration exactly 10 seconds. Vertical 9:16 only (1080x1920).

FRAMES: Use the provided FIRST FRAME as the exact opening frame (there is no last frame; follow the action below). Keep faces, clothes, location layout, props and light direction identical to the frames.

CONTINUITY: AMIN: 24-year-old Algerian young man, pale olive skin, slightly gaunt cheeks, dark messy wavy hair, patchy five-day stubble, dark circles under sorrowful brown eyes, oversized faded black hoodie with the hood DOWN over a dark grey T-shirt, dark charcoal washed jeans, worn scuffed sneakers (street). In the mosque: the same hoodie with the sleeves pushed above the elbows, barefoot. YOUCEF: 27-year-old Algerian young man, warm medium-olive skin, full neatly trimmed black beard, short neat black hair, gentle brown eyes, calm compassionate face, a clean cream-beige Algerian cotton qamis (long, light embroidery at the collar) over simple trousers, leather sandals in the street, barefoot in the mosque. The alley, closed shutter, curb, single streetlamp, puddles and the tiny glowing arched doorway on the right stay exactly as in the frames. The bottle is a dark glass bottle with NO label. Youcef's face is never visible: only his blurred shoulder and the side of his head at the right edge of the frame. Amin sits on the curb.

ACTION AND TIMING:
- 0.0-0.3s: Amin keeps his head lowered, avoiding any eye contact.
- 0.3-3.2s: Youcef's voice is heard from behind the blurred shoulder (his lips are not visible). Amin does not look up; his eyes glisten.
- 3.4-8.0s: Amin looks up for a fleeting moment toward Youcef, his voice breaking, and speaks his line with raw shame, then looks away again, chin trembling, shaking his head slightly.
- 8.0-10.0s: Amin lowers his gaze, squeezes his eyes shut, a tear slides down his hollow cheek, breathing heavy and broken.

DIALOGUE:
يوسف (صوت من خلف الكتف، وجهه غير ظاهر): «الْفَجْرْ قْرَّبْ يَا خُويَا... تْجِي مَعَايَ لْلْمَسْجِدْ؟»
أمين: «وَعَلَيْكُمْ السَّلَامْ... أَنَا أَمِينْ. رَانِي مْوَسَّخْ، مَا نَصْلَحْشْ نَدْخَلْ لْبِيتْ رَبِّي.»
Natural Algerian Darja with an urban Algerian accent, spoken by native Algerian voices (the Quranic and prophetic phrases in clear classical Arabic). Never Egyptian, Gulf or Syrian. Pronounce the words exactly as written, including the sukun marks, without adding, translating or rewriting words. Only the named speaker moves his lips; every other face stays still. No overlapping lines.

CAMERA: Locked-off tripod shot with at most a very slow, barely visible push-in (about 3 percent) over the 10 seconds. No cuts, no pans, no handheld shake, no zoom jumps, no reframing. Faces and hands always stay inside the frame.

PERFORMANCE: Subtle natural micro-expressions, real blinks, believable breathing, realistic hands with correct fingers, natural weight and timing of body movement. Restrained emotion, nothing theatrical.

SOUND (diegetic only): Quiet pre-dawn alley ambience, a crack and tremble in Amin's voice, a sharp intake of breath at about 3.2s, a muffled sniffle at about 8.2s, hoodie rustle. Dialogue clearly in front of the ambience.

END FRAME: Amin looking down, eyes shut, a tear on his cheek, in the same position and framing as the first frame.

NEGATIVE: no horizontal or square format; no cuts, no pans, no handheld shake, no fast zooms; no morphing, no identity drift, no new people, no extra fingers, no warped hands, no distorted faces; no objects teleporting, duplicating or vanishing (the dark glass bottle never changes shape and never spills a puddle); no readable text, no subtitles, no logos, no watermark; NO MUSIC OF ANY KIND, no score, no humming, no choir; no melodrama.
```


### 🎬 SC04 (SC04_A ← SC04_B)

```text
Create a photorealistic live-action scene for the Algerian short film “Al-Tawba”. Duration exactly 10 seconds. Vertical 9:16 only (1080x1920).

FRAMES: Use the provided FIRST FRAME (SC04_A) as the exact opening frame and the provided LAST FRAME (SC04_B) as the exact closing frame. Keep faces, clothes, location layout, props and light direction identical to the frames.

CONTINUITY: AMIN: 24-year-old Algerian young man, pale olive skin, slightly gaunt cheeks, dark messy wavy hair, patchy five-day stubble, dark circles under sorrowful brown eyes, oversized faded black hoodie with the hood DOWN over a dark grey T-shirt, dark charcoal washed jeans, worn scuffed sneakers (street). In the mosque: the same hoodie with the sleeves pushed above the elbows, barefoot. YOUCEF: 27-year-old Algerian young man, warm medium-olive skin, full neatly trimmed black beard, short neat black hair, gentle brown eyes, calm compassionate face, a clean cream-beige Algerian cotton qamis (long, light embroidery at the collar) over simple trousers, leather sandals in the street, barefoot in the mosque. The alley, closed shutter, curb, single streetlamp, puddles and the tiny glowing arched doorway on the right stay exactly as in the frames. The bottle is a dark glass bottle with NO label. Amin stays seated at the left foreground edge, out of focus, head bowed.

ACTION AND TIMING:
- 0.0-2.5s: Youcef lowers himself onto his right knee on the damp ground so his eyes are level with Amin's, and places his right hand on Amin's LEFT shoulder with a gentle reassuring squeeze.
- 2.5-8.0s: Youcef speaks his line in a soft soothing cadence, softly shaking his head as if dismissing Amin's despair, leaning slightly closer with mercy in his eyes.
- 8.0-10.0s: Youcef gives a radiant loving smile of encouragement and gently pats Amin's shoulder.

DIALOGUE:
يوسف: «رَبِّي يَغْفَرْ كُلَّشْ يَا أَمِينْ... بِيتْ رَبِّي مَفْتُوحْ لْلتَّايْبِينْ. نُوضْ مَعَايَ يَا خُويَا.»
Natural Algerian Darja with an urban Algerian accent, spoken by native Algerian voices (the Quranic and prophetic phrases in clear classical Arabic). Never Egyptian, Gulf or Syrian. Pronounce the words exactly as written, including the sukun marks, without adding, translating or rewriting words. Only the named speaker moves his lips; every other face stays still. No overlapping lines.

CAMERA: Locked-off tripod shot with at most a very slow, barely visible push-in (about 3 percent) over the 10 seconds. No cuts, no pans, no handheld shake, no zoom jumps, no reframing. Faces and hands always stay inside the frame.

PERFORMANCE: Subtle natural micro-expressions, real blinks, believable breathing, realistic hands with correct fingers, natural weight and timing of body movement. Restrained emotion, nothing theatrical.

SOUND (diegetic only): Soft deep resonant voice with intimate acoustics, a cloth rustle as the hand settles at about 1.0s, a quiet distant breeze. Dialogue clearly in front of the ambience.

END FRAME: Youcef kneeling with his right hand on Amin's shoulder and a warm smile, exactly the LAST FRAME. No hand slipping through the shoulder, no change in the number of fingers.

NEGATIVE: no horizontal or square format; no cuts, no pans, no handheld shake, no fast zooms; no morphing, no identity drift, no new people, no extra fingers, no warped hands, no distorted faces; no objects teleporting, duplicating or vanishing (the dark glass bottle never changes shape and never spills a puddle); no readable text, no subtitles, no logos, no watermark; NO MUSIC OF ANY KIND, no score, no humming, no choir; no melodrama.
```


### 🎬 SC05 (SC05_A ← SC05_B)

```text
Create a photorealistic live-action scene for the Algerian short film “Al-Tawba”. Duration exactly 10 seconds. Vertical 9:16 only (1080x1920).

FRAMES: Use the provided FIRST FRAME (SC05_A) as the exact opening frame and the provided LAST FRAME (SC05_B) as the exact closing frame. Keep faces, clothes, location layout, props and light direction identical to the frames.

CONTINUITY: AMIN: 24-year-old Algerian young man, pale olive skin, slightly gaunt cheeks, dark messy wavy hair, patchy five-day stubble, dark circles under sorrowful brown eyes, oversized faded black hoodie with the hood DOWN over a dark grey T-shirt, dark charcoal washed jeans, worn scuffed sneakers (street). In the mosque: the same hoodie with the sleeves pushed above the elbows, barefoot. YOUCEF: 27-year-old Algerian young man, warm medium-olive skin, full neatly trimmed black beard, short neat black hair, gentle brown eyes, calm compassionate face, a clean cream-beige Algerian cotton qamis (long, light embroidery at the collar) over simple trousers, leather sandals in the street, barefoot in the mosque. The alley, closed shutter, curb, single streetlamp, puddles and the tiny glowing arched doorway on the right stay exactly as in the frames. The bottle is a dark glass bottle with NO label. Camera is locked across the alley; the movement happens inside a fixed frame. The bottle ends lying on its side at the curb, no liquid pool.

ACTION AND TIMING:
- 0.0-3.0s: Amin's hand opens completely; the unlabeled dark glass bottle tips over and rolls slowly a short distance along the curb with a dull glass clatter.
- 3.0-6.0s: Amin grips Youcef's extended right hand with both of his hands like a drowning man grabbing a lifeline. Youcef pulls him up with firm brotherly strength.
- 6.0-10.0s: Amin rises to his feet beside Youcef. Youcef puts his left arm around Amin's back. They turn to the RIGHT toward the distant warm glow and take their first step together.

DIALOGUE:
أمين: «يَا رَبّْ... بِسْمِ اللهْ.»
يوسف: «تَوَكَّلْ عَلَى رَبِّي يَا أَمِينْ.»
(Amin speaks at 3.2-4.5s; Youcef answers at 5.0-6.5s.)
Natural Algerian Darja with an urban Algerian accent, spoken by native Algerian voices (the Quranic and prophetic phrases in clear classical Arabic). Never Egyptian, Gulf or Syrian. Pronounce the words exactly as written, including the sukun marks, without adding, translating or rewriting words. Only the named speaker moves his lips; every other face stays still. No overlapping lines.

CAMERA: Locked-off tripod shot with at most a very slow, barely visible push-in (about 3 percent) over the 10 seconds. No cuts, no pans, no handheld shake, no zoom jumps, no reframing. Faces and hands always stay inside the frame.

PERFORMANCE: Subtle natural micro-expressions, real blinks, believable breathing, realistic hands with correct fingers, natural weight and timing of body movement. Restrained emotion, nothing theatrical.

SOUND (diegetic only): Glass clattering and rolling on pavement at about 1.0-2.8s, cloth friction as the hands clasp at about 3.5s, sneaker and sandal scuffs pushing off the ground at about 6.0s, a deep emotional exhale. Dialogue clearly in front of the ambience.

END FRAME: Both men standing side by side, turned toward the distant glow, Amin's hands around Youcef's hand, the bottle lying at the curb, exactly the LAST FRAME.

NEGATIVE: no horizontal or square format; no cuts, no pans, no handheld shake, no fast zooms; no morphing, no identity drift, no new people, no extra fingers, no warped hands, no distorted faces; no objects teleporting, duplicating or vanishing (the dark glass bottle never changes shape and never spills a puddle); no readable text, no subtitles, no logos, no watermark; NO MUSIC OF ANY KIND, no score, no humming, no choir; no melodrama.
```


### 🎬 SC06 (SC06_A ← SC06_B)

```text
Create a photorealistic live-action scene for the Algerian short film “Al-Tawba”. Duration exactly 10 seconds. Vertical 9:16 only (1080x1920).

FRAMES: Use the provided FIRST FRAME (SC06_A) as the exact opening frame and the provided LAST FRAME (SC06_B) as the exact closing frame. Keep faces, clothes, location layout, props and light direction identical to the frames.

CONTINUITY: AMIN: 24-year-old Algerian young man, pale olive skin, slightly gaunt cheeks, dark messy wavy hair, patchy five-day stubble, dark circles under sorrowful brown eyes, oversized faded black hoodie with the hood DOWN over a dark grey T-shirt, dark charcoal washed jeans, worn scuffed sneakers (street). In the mosque: the same hoodie with the sleeves pushed above the elbows, barefoot. YOUCEF: 27-year-old Algerian young man, warm medium-olive skin, full neatly trimmed black beard, short neat black hair, gentle brown eyes, calm compassionate face, a clean cream-beige Algerian cotton qamis (long, light embroidery at the collar) over simple trousers, leather sandals in the street, barefoot in the mosque. The tiled wall, four chrome faucets, stone bench and drain trough stay exactly as in the frames. Youcef sits at the left faucet, Amin at the next faucet on his right. Amin's hoodie sleeves are DOWN at the start and he pushes them up toward his elbows at the end.

ACTION AND TIMING:
- 0.0-3.0s: Youcef rubs his hands under the clear running water, washing them carefully.
- 3.0-8.2s: Youcef turns his head toward Amin with water droplets glistening in his beard and speaks his line with a calm teaching smile, showing three fingers of his wet right hand to mean 'three times'.
- 8.2-10.0s: Amin nods slowly with complete attention and begins pushing the sleeves of his black hoodie up toward his elbows.

DIALOGUE:
يوسف: «بِسْمِ اللهْ... نَبْدَاوْ بِلِيدِينْ، تْلَاتْ مَرَّاتْ. هَاذِي سُنَّةْ النَّبِيّْ، صَلَّى اللهُ عَلَيْهِ وَسَلَّمْ.»
Natural Algerian Darja with an urban Algerian accent, spoken by native Algerian voices (the Quranic and prophetic phrases in clear classical Arabic). Never Egyptian, Gulf or Syrian. Pronounce the words exactly as written, including the sukun marks, without adding, translating or rewriting words. Only the named speaker moves his lips; every other face stays still. No overlapping lines.

CAMERA: Locked-off tripod shot with at most a very slow, barely visible push-in (about 3 percent) over the 10 seconds. No cuts, no pans, no handheld shake, no zoom jumps, no reframing. Faces and hands always stay inside the frame.

PERFORMANCE: Subtle natural micro-expressions, real blinks, believable breathing, realistic hands with correct fingers, natural weight and timing of body movement. Restrained emotion, nothing theatrical.

SOUND (diegetic only): A soothing, crisp, continuous trickle of running water on stone, wet hands rubbing at about 1.0-2.5s, soft room acoustics with a faint echo, the calm voice. Dialogue clearly in front of the ambience.

END FRAME: Youcef turned toward Amin with three fingers raised, Amin nodding and pushing up his sleeves, exactly the LAST FRAME. No gelatinous or floating water, no change in water flow rate.

NEGATIVE: no horizontal or square format; no cuts, no pans, no handheld shake, no fast zooms; no morphing, no identity drift, no new people, no extra fingers, no warped hands, no distorted faces; no objects teleporting, duplicating or vanishing (the dark glass bottle never changes shape and never spills a puddle); no readable text, no subtitles, no logos, no watermark; NO MUSIC OF ANY KIND, no score, no humming, no choir; no melodrama.
```


### 🎬 SC07 (SC07_A ← SC07_B)

```text
Create a photorealistic live-action scene for the Algerian short film “Al-Tawba”. Duration exactly 10 seconds. Vertical 9:16 only (1080x1920).

FRAMES: Use the provided FIRST FRAME (SC07_A) as the exact opening frame and the provided LAST FRAME (SC07_B) as the exact closing frame. Keep faces, clothes, location layout, props and light direction identical to the frames.

CONTINUITY: AMIN: 24-year-old Algerian young man, pale olive skin, slightly gaunt cheeks, dark messy wavy hair, patchy five-day stubble, dark circles under sorrowful brown eyes, oversized faded black hoodie with the hood DOWN over a dark grey T-shirt, dark charcoal washed jeans, worn scuffed sneakers (street). In the mosque: the same hoodie with the sleeves pushed above the elbows, barefoot. YOUCEF: 27-year-old Algerian young man, warm medium-olive skin, full neatly trimmed black beard, short neat black hair, gentle brown eyes, calm compassionate face, a clean cream-beige Algerian cotton qamis (long, light embroidery at the collar) over simple trousers, leather sandals in the street, barefoot in the mosque. The tiled wall, four chrome faucets, stone bench and drain trough stay exactly as in the frames. Youcef sits at the left faucet, Amin at the next faucet on his right. Amin is in sharp foreground with his sleeves pushed above the elbows; Youcef is soft and blurred in the background.

ACTION AND TIMING:
- 0.0-3.5s: Amin brings his water-filled hands to his face and washes it with deep focus and relief, rubbing his cheeks, forehead and stubble.
- 3.5-5.2s: He lowers his hands; water streams down his chin and forearms; he opens his eyes, clear and calm, no longer dark with despair.
- 5.2-9.5s: He whispers the testimony of faith with awe, turning his head slightly toward Youcef, who nods slowly in the blurred background.
- 9.5-10.0s: A soft exhale of gratitude, still.

DIALOGUE:
أمين (همسًا): «أَشْهَدُ أَنْ لَا إِلَهَ إِلَّا اللهُ وَحْدَهُ لَا شَرِيكَ لَهُ، وَأَشْهَدُ أَنَّ مُحَمَّدًا عَبْدُهُ وَرَسُولُهُ.»
Natural Algerian Darja with an urban Algerian accent, spoken by native Algerian voices (the Quranic and prophetic phrases in clear classical Arabic). Never Egyptian, Gulf or Syrian. Pronounce the words exactly as written, including the sukun marks, without adding, translating or rewriting words. Only the named speaker moves his lips; every other face stays still. No overlapping lines.

CAMERA: Locked-off tripod shot with at most a very slow, barely visible push-in (about 3 percent) over the 10 seconds. No cuts, no pans, no handheld shake, no zoom jumps, no reframing. Faces and hands always stay inside the frame.

PERFORMANCE: Subtle natural micro-expressions, real blinks, believable breathing, realistic hands with correct fingers, natural weight and timing of body movement. Restrained emotion, nothing theatrical.

SOUND (diegetic only): Splashing water on skin and the stone basin at about 0.5-3.0s, a wet hand moving along a forearm, the whispered testimony reverberating softly in the tiled room, droplet echoes. Dialogue clearly in front of the ambience.

END FRAME: Amin with clear open eyes and dripping water, turned slightly toward Youcef, exactly the LAST FRAME. No water flowing upward, no blur of the face during water contact.

NEGATIVE: no horizontal or square format; no cuts, no pans, no handheld shake, no fast zooms; no morphing, no identity drift, no new people, no extra fingers, no warped hands, no distorted faces; no objects teleporting, duplicating or vanishing (the dark glass bottle never changes shape and never spills a puddle); no readable text, no subtitles, no logos, no watermark; NO MUSIC OF ANY KIND, no score, no humming, no choir; no melodrama.
```


### 🎬 SC08 (SC08_A ← SC08_B)

```text
Create a photorealistic live-action scene for the Algerian short film “Al-Tawba”. Duration exactly 10 seconds. Vertical 9:16 only (1080x1920).

FRAMES: Use the provided FIRST FRAME (SC08_A) as the exact opening frame and the provided LAST FRAME (SC08_B) as the exact closing frame. Keep faces, clothes, location layout, props and light direction identical to the frames.

CONTINUITY: AMIN: 24-year-old Algerian young man, pale olive skin, slightly gaunt cheeks, dark messy wavy hair, patchy five-day stubble, dark circles under sorrowful brown eyes, oversized faded black hoodie with the hood DOWN over a dark grey T-shirt, dark charcoal washed jeans, worn scuffed sneakers (street). In the mosque: the same hoodie with the sleeves pushed above the elbows, barefoot. YOUCEF: 27-year-old Algerian young man, warm medium-olive skin, full neatly trimmed black beard, short neat black hair, gentle brown eyes, calm compassionate face, a clean cream-beige Algerian cotton qamis (long, light embroidery at the collar) over simple trousers, leather sandals in the street, barefoot in the mosque. The mihrab, minbar, columns, windows, carpet stripes and the position of the two men stay exactly as in the frames. They stay on the same stripe, shoulder to shoulder. The camera is BEHIND the men: Youcef (imam) stays on the LEFT of the frame, Amin on the RIGHT. Positions never swap.

ACTION AND TIMING:
- 0.0-1.0s: Both stand still facing the qibla.
- 1.0-3.8s: Youcef turns his head slightly to his right and whispers kind instructions to Amin.
- 3.8-5.5s: Amin nods with humility and aligns his right shoulder and bare feet with Youcef's. Both lower their eyes to the place of prostration.
- 5.5-8.5s: Both raise their hands to ear level together for the opening takbir; Youcef says the takbir aloud at 6.0-7.5s.
- 8.5-10.0s: Both fold the right hand over the left on the chest in complete stillness.

DIALOGUE:
يوسف (همسًا): «نْصَلُّو رَكْعَتِينْ... تَبْعَنِي بَرْكْ، وَاسْتَحْضَرْ عَظَمَةْ رَبِّي.»
يوسف (بصوت مسموع ورخيم): «اللهُ أَكْبَرْ.»
Natural Algerian Darja with an urban Algerian accent, spoken by native Algerian voices (the Quranic and prophetic phrases in clear classical Arabic). Never Egyptian, Gulf or Syrian. Pronounce the words exactly as written, including the sukun marks, without adding, translating or rewriting words. Only the named speaker moves his lips; every other face stays still. No overlapping lines.

CAMERA: Locked-off tripod shot with at most a very slow, barely visible push-in (about 3 percent) over the 10 seconds. No cuts, no pans, no handheld shake, no zoom jumps, no reframing. Faces and hands always stay inside the frame.

PERFORMANCE: Subtle natural micro-expressions, real blinks, believable breathing, realistic hands with correct fingers, natural weight and timing of body movement. Restrained emotion, nothing theatrical.

SOUND (diegetic only): An intimate warm whisper, the soft rustle of cloth as the arms rise, a clear resonant takbir echoing gently in the vaulted hall, the reverent silence of the dawn. Dialogue clearly in front of the ambience.

END FRAME: Both men standing shoulder to shoulder with the right hand over the left on the chest, eyes lowered, exactly the LAST FRAME. No foot sliding, no drifting carpet stripes, no swapped positions.

NEGATIVE: no horizontal or square format; no cuts, no pans, no handheld shake, no fast zooms; no morphing, no identity drift, no new people, no extra fingers, no warped hands, no distorted faces; no objects teleporting, duplicating or vanishing (the dark glass bottle never changes shape and never spills a puddle); no readable text, no subtitles, no logos, no watermark; NO MUSIC OF ANY KIND, no score, no humming, no choir; no melodrama.
```


### 🎬 SC09 (SC09_A ← SC09_B)

```text
Create a photorealistic live-action scene for the Algerian short film “Al-Tawba”. Duration exactly 10 seconds. Vertical 9:16 only (1080x1920).

FRAMES: Use the provided FIRST FRAME (SC09_A) as the exact opening frame and the provided LAST FRAME (SC09_B) as the exact closing frame. Keep faces, clothes, location layout, props and light direction identical to the frames.

CONTINUITY: AMIN: 24-year-old Algerian young man, pale olive skin, slightly gaunt cheeks, dark messy wavy hair, patchy five-day stubble, dark circles under sorrowful brown eyes, oversized faded black hoodie with the hood DOWN over a dark grey T-shirt, dark charcoal washed jeans, worn scuffed sneakers (street). In the mosque: the same hoodie with the sleeves pushed above the elbows, barefoot. YOUCEF: 27-year-old Algerian young man, warm medium-olive skin, full neatly trimmed black beard, short neat black hair, gentle brown eyes, calm compassionate face, a clean cream-beige Algerian cotton qamis (long, light embroidery at the collar) over simple trousers, leather sandals in the street, barefoot in the mosque. The mihrab, minbar, columns, windows, carpet stripes and the position of the two men stay exactly as in the frames. They stay on the same stripe, shoulder to shoulder. The camera is IN FRONT, low: Amin is on the LEFT of the frame and Youcef on the RIGHT. Positions never swap.

ACTION AND TIMING:
- 0.0-3.0s: Both are in sujood side by side. Amin's back rises and falls very slowly with breathing.
- 3.0-5.0s: Youcef rises from sujood into a seated upright posture. Amin stays in sujood; his breathing becomes slower and almost imperceptible.
- 5.0-7.0s: Youcef sits in the tashahhud posture, hands on his thighs, his lips moving in a silent recitation. Amin remains completely still.
- 7.0-10.0s: Youcef raises his right index finger and glances for a split second at Amin, assuming he is simply prolonging his prayer. Soft dawn light falls over Amin's still back.

DIALOGUE:
يوسف (همسًا شبه غير مسموع، شفتاه تتحركان): «التَّحِيَّاتُ لِلَّهِ وَالصَّلَوَاتُ وَالطَّيِّبَاتُ...»
Natural Algerian Darja with an urban Algerian accent, spoken by native Algerian voices (the Quranic and prophetic phrases in clear classical Arabic). Never Egyptian, Gulf or Syrian. Pronounce the words exactly as written, including the sukun marks, without adding, translating or rewriting words. Only the named speaker moves his lips; every other face stays still. No overlapping lines.

CAMERA: Locked-off tripod shot with at most a very slow, barely visible push-in (about 3 percent) over the 10 seconds. No cuts, no pans, no handheld shake, no zoom jumps, no reframing. Faces and hands always stay inside the frame.

PERFORMANCE: Subtle natural micro-expressions, real blinks, believable breathing, realistic hands with correct fingers, natural weight and timing of body movement. Restrained emotion, nothing theatrical.

SOUND (diegetic only): A faint whispered recitation, the total hush of the prayer hall, a distant bird at about 8.0s, the soft shift of cloth as Youcef sits up. Dialogue clearly in front of the ambience.

END FRAME: Youcef seated in the tashahhud with his finger raised, Amin still in sujood, exactly the LAST FRAME. No twitching or shuddering of Amin's body, no floating knees or hands.

NEGATIVE: no horizontal or square format; no cuts, no pans, no handheld shake, no fast zooms; no morphing, no identity drift, no new people, no extra fingers, no warped hands, no distorted faces; no objects teleporting, duplicating or vanishing (the dark glass bottle never changes shape and never spills a puddle); no readable text, no subtitles, no logos, no watermark; NO MUSIC OF ANY KIND, no score, no humming, no choir; no melodrama.
```


### 🎬 SC10 (SC10_A ← SC10_C، المرجع الإضافي SC10_B)

```text
Create a photorealistic live-action scene for the Algerian short film “Al-Tawba”. Duration exactly 10 seconds. Vertical 9:16 only (1080x1920).

FRAMES: Use the provided FIRST FRAME (SC10_A) as the exact opening frame and the provided LAST FRAME (SC10_C) as the exact closing frame. Optional extra reference image: SC10_B, the middle moment where Amin has gently slumped toward Youcef. Keep faces, clothes, location layout, props and light direction identical to the frames.

CONTINUITY: AMIN: 24-year-old Algerian young man, pale olive skin, slightly gaunt cheeks, dark messy wavy hair, patchy five-day stubble, dark circles under sorrowful brown eyes, oversized faded black hoodie with the hood DOWN over a dark grey T-shirt, dark charcoal washed jeans, worn scuffed sneakers (street). In the mosque: the same hoodie with the sleeves pushed above the elbows, barefoot. YOUCEF: 27-year-old Algerian young man, warm medium-olive skin, full neatly trimmed black beard, short neat black hair, gentle brown eyes, calm compassionate face, a clean cream-beige Algerian cotton qamis (long, light embroidery at the collar) over simple trousers, leather sandals in the street, barefoot in the mosque. The mihrab, minbar, columns, windows, carpet stripes and the position of the two men stay exactly as in the frames. They stay on the same stripe, shoulder to shoulder. The camera is IN FRONT, low: Amin is on the LEFT of the frame and Youcef on the RIGHT. Positions never swap.

ACTION AND TIMING:
- 0.0-2.5s: Youcef finishes the taslim to his right, turns toward Amin with a warm smile and gently taps Amin's LEFT shoulder with his right hand. He says his first line between 1.5s and 3.0s.
- 2.5-5.5s: Amin does not wake; his body gently and smoothly slumps toward Youcef onto the carpet beside him, softly, never abruptly. His face is revealed with eyes peacefully closed, serene skin and a faint pure smile.
- 5.5-8.5s: Youcef's smile freezes in realization. He steadies Amin's shoulders and places two trembling fingers on his neck, then looks at Amin's peaceful face.
- 8.5-10.0s: Youcef cradles Amin's head on his lap, tears running down his cheeks. Instead of panic, his face turns to quiet awe; he looks slightly upward. He says his final line between 6.3s and 10.0s.

DIALOGUE:
يوسف (بابتسامة): «أَمِينْ؟ خَلْصَتْ الصَّلَاةْ يَا خُويَا...»
يوسف (بصوت باكٍ هامس): «إِنَّا لِلَّهِ وَإِنَّا إِلَيْهِ رَاجِعُونَ... هَنِيئًا لِيكْ.»
Natural Algerian Darja with an urban Algerian accent, spoken by native Algerian voices (the Quranic and prophetic phrases in clear classical Arabic). Never Egyptian, Gulf or Syrian. Pronounce the words exactly as written, including the sukun marks, without adding, translating or rewriting words. Only the named speaker moves his lips; every other face stays still. No overlapping lines.

CAMERA: Locked-off tripod shot with at most a very slow, barely visible push-in (about 3 percent) over the 10 seconds. No cuts, no pans, no handheld shake, no zoom jumps, no reframing. Faces and hands always stay inside the frame.

PERFORMANCE: Subtle natural micro-expressions, real blinks, believable breathing, realistic hands with correct fingers, natural weight and timing of body movement. Restrained emotion, nothing theatrical.

SOUND (diegetic only): A gentle cloth tap at about 1.8s, the soft dull rustle of a body leaning onto the carpet at about 3.5s, a sharp gasp from Youcef at about 5.8s, a choked tearful whisper echoing in the quiet mosque, absolute silence. Dialogue clearly in front of the ambience.

END FRAME: Youcef cradling Amin's peaceful head, tears on his cheeks, exactly the LAST FRAME. No violent or abrupt falling, no distorted neck or fingers, no theatrical overacting. Restrained, tender realism only.

NEGATIVE: no horizontal or square format; no cuts, no pans, no handheld shake, no fast zooms; no morphing, no identity drift, no new people, no extra fingers, no warped hands, no distorted faces; no objects teleporting, duplicating or vanishing (the dark glass bottle never changes shape and never spills a puddle); no readable text, no subtitles, no logos, no watermark; NO MUSIC OF ANY KIND, no score, no humming, no choir; no melodrama.
```


---

## 8) المونتاج (CapCut)

- رتّب المقاطع من 1 إلى 10 بقطع مباشر، 1080×1920 و30 FPS.
- **بلا موسيقى** كما في السيناريو. الأصوات اللي يولّدها Flow تكفي.
- **اختياري ويقوي الواقعية:** أذان الفجر بعيد جدًا (من مكتبة مجانية) يبدأ في المشهد 4 بصوت خافت جدًا (5 إلى 8%) ويتلاشى عند وصولهما للمسجد.
- أضف نص الخاتمة في آخر ثانيتين من المشهد 10 (اختياري): «لا تقنطوا من رحمة الله».
- ثبّت آخر نصف ثانية.

## 9) النشر

### العناوين (اختر واحدًا)
1. «راني موسّخ ما نصلحش لبيت ربي»... فيلم قصير عن التوبة 🕌
2. من ضياع الحومة إلى أول سجدة... فيلم قصير مؤثر
3. فيلم قصير: أول توبة وآخر سجدة 🤍
4. لا تقنط من رحمة الله... قصة توبة (فيلم قصير)

### الوصف
```text
فيلم قصير (دراما اجتماعية) عن التوبة وسعة رحمة الله، من إنتاج وإخراج بالذكاء الاصطناعي.
«قُلْ يَا عِبَادِيَ الَّذِينَ أَسْرَفُوا عَلَىٰ أَنفُسِهِمْ لَا تَقْنَطُوا مِن رَّحْمَةِ اللَّهِ».
هذا العمل خيالي، وشخصياته ومشاهده مولّدة بالذكاء الاصطناعي.
شاركه لعلّه يكون سببًا في رجوع أحد إلى الله.
```

### الهاشتاقات
```text
#فيلم_قصير #التوبة #رحمة_الله #قصص_مؤثرة #دراما_جزائرية #الجزائر #الحومة #الصلاة #المسجد #Shorts
```

### تنبيهات
- هذا فيلم خيالي: **ما تكتبش في العنوان أو الوصف أنه قصة حقيقية.**
- يوتيوب يطلب غالبًا الإفصاح عن المحتوى الاصطناعي الواقعي (أشخاص يبدون حقيقيين). فعّل خيار الإفصاح عند الرفع.
- الصورة المصغرة: لقطة SC04_B (يد يوسف على كتف أمين) أو SC10_C. النص: «آخر سجدة» أو «توبة صادقة».

---

## 10) قائمة الفحص قبل التمرير لـ Flow

**الزقاق (SC01-05):**
- يوسف يدخل من **اليسار** ماشيًا نحو **اليمين**، والقوس المضيء **بعيد جدًا على اليمين**.
- القارورة داكنة **بلا ملصق**، في يد أمين اليمنى، وتسقط في المشهد 5 فقط.
- يد يوسف **اليمنى على كتف أمين الأيسر** في المشهد 4.
- قلنسوة أمين مرخاة للخلف، وأكمامه **لم ترفع بعد**.

**الميضأة (SC06-07):**
- يوسف عند الحنفية **اليسرى** وأمين **على يمينه**.
- أكمام أمين مرفوعة فقط من نهاية SC06، وفي SC07 كاملة فوق المرفقين.
- الماء يتدفق من الحنفية بشكل طبيعي، بلا شكل هلامي.

**قاعة الصلاة (SC08-10):**
- من الخلف (SC08): يوسف **يسار** الكادر، أمين **يمينه**. من الأمام (SC09-10): أمين **يسار** الكادر، يوسف **يمينه**.
- كتفًا بكتف، **نفس الخط الكريمي**، حافيان.
- في SC09: يوسف جالس وأمين في السجود. في SC10: أمين يميل نحو يوسف **بهدوء**، لا يسقط بعنف.

**الفيديو:**
- راجع النطق الجزائري في أول 3 ثواني من أول مقطع.
- تأكد أن إطار النهاية يطابق الصورة قبل الانتقال للمقطع التالي.
- إذا بان الكلام مستعجل: اختصر الجملة بدل ما تضغطها.

---

## 11) ملاحظات فقهية موجزة (للتحقق قبل النشر)

- **ترتيب الوضوء:** النية، اليدان ثلاثًا، المضمضة والاستنشاق، الوجه، اليدان إلى المرفقين، مسح الرأس والأذنين، الرجلان. الفيلم يعرض اختصارًا سينمائيًا (اليدان ثم الوجه ثم الساعدان).
- **وقوف الاثنين في الجماعة:** المأموم الواحد يقف **عن يمين الإمام** بمحاذاته. هو المعروف من حديث ابن عباس في صلاة الليل، ولذلك جعلناها «ركعتين» نافلة بالجماعة.
- **اليدان بعد التكبير:** الفيلم يعرض وضع اليمنى على اليسرى. وإن كان جمهورك على السدل (المالكي) فاستبدل في برومبتات SC08 جملة «right hand folded over the left» بـ «arms relaxed at the sides».
- **مشهد الوفاة:** أُخرج بلا عنف وبلا تفاصيل طبية، فقط سكون وسكينة. وهذا مقصود.
