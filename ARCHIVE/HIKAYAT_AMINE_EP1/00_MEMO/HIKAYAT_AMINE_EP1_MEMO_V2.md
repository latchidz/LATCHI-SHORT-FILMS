# مذكرة الإنتاج V2 — «حكايات أمين» الحلقة الأولى (Master Reset)
## SC01 → SC19 • كلها في الكراج • تنتهي بالشاشة السوداء (كليفهانغر)

**المدة:** 19 مشهد × 10ث = **3:10** • أفقي 16:9 (1376×768) • فوتوريالستيك
**قواعد صارمة:** كل برومبت فيديو = 10ث بالضبط • لقطة واحدة متواصلة • كاميرا مقفلة (Locked-off) — صفر pan/زوم/حركة • القطع المباشر بين المشاهد فقط • الحوار **حرفياً** كيما كتبو العميل (مشكول) • بلا موسيقى (أصوات بيئة + الأذان في SC13 فقط) • لا نص/شعارات • **السارق لا يظهر إطلاقاً في هذه الحلقة** • **السيارات بحجم طبيعي منطقي دائماً — ما تبانش كبار** (قاعدة العميل 18 أكتوبر) • نيجاتيف الصور منفصل عن الفيديو.

---

## المرحلة 1 — مراجع البيئة (مولّدة ✅ في `HIKAYAT_AMINE_REFS/`)

| المرجع | الوصف | البرومبت (مختصر) |
|---|---|---|
| `REF_GARAGE_EXT_CORNER.png` | الواجهتان (أمامية + جانبية) من زاوية الشارع — المدخلان المتدحرجان على الواجهة الأمامية + الجدار الجانبي المهترئ | نفس المرجع الأساسي من زاوية ثلاثة أرباع تُظهر الواجهتين، الشارع يسار، ضوء صباحي من اليسار، بلا لافتات |
| `REF_WORKSHOP_INT.png` | داخل الورشة واسعاً: المدخلان المضيئان + **المكتب في العمق** عبر ممر جانبي (مو عند المدخل المفتوح) + **باب الحمّام الأخضر** على الحائط الأيسر | نفس materials تاع WORKSHOP_MAIN + الكاميرا قرب مدخل تنظر قطرياً للعمق: ممر ضيق يودي لباب مكتب عميق + الباب الأخضر يسار الوسط |
| `REF_OFFICE_INT.png` | المكتب مطابق 100% للجزء الثاني + **آلة حاسبة** + **ورقة حسابات الفورنيسور** (خط غير مقروء) | تعديل OFFICE_MONITOR_BOX: إضافة آلة حاسبة رمادية صغيرة + ورقة سطور مخطوطة بخط غير مقروء حذا الصندوق الخشبي — بلا أي تغيير آخر |

**مراجع الشخصيات والسيارات (جاهزة ✅):** REF_CUSTOMER_A • REF_CUSTOMER_B • AMINE_FRONT/THREE_QUARTER • HAJ_FRONT/THREE_QUARTER • REF_MERCEDES • REF_DACIA_STEPWAY • REF_TOW_TRUCK • REF_GARAGE_EXTERIOR (واجهة أمامية مباشرة) • REF_WC_DOOR

## جغرافيا الكراج المقفلة (Master Reference — Anchor ثابت لكل المشاهد الخارجية)
1. **الهندسة العامة:** مبنى خرساني قديم متهالك على **ناصية شارع** في حي جزائري شعبي • الواجهة الرئيسية فيها **بوابتان ضخمتان متجاورتان** • **عمود كهرباء خرساني** بالضبط عند الزاوية اليسرى حيث يتفرع الشارع نحو الخلفية يساراً
2. **البوابتان كلتاهما مفتوحتان دائماً:** البابان المعدنيان الأزرقان/الرماديان الصدئان مرفوعان بالكامل في كل لقطة
3. **داخل البوابتين:** **غير الأدوات والمعدات والسيارة الزرقاء** (رينو 4 زرقاء على الرافعة الهيدروليكية الزرقاء في البوابة اليمنى) — لا سيارات أخرى، لا براميل، لا فوضى • فوق البوابة اليسرى صف نوافذ Transom مستطيلة
4. **المحيط:** أسفلت متصدع ببقع زيت سوداء • الشارع اليسري فيه منازل قديمة بطلاء باهت (أصفر فاتح/أبيض) + أسلاك كهرباء متقاطعة • **ضوء صباحي من جهة الشارع في كل اللقطات**
- **من الداخل (مراجع الجزء الثاني):** الورشة واسعة • **المكتب في العمق** عبر ممر جانبي • **باب الحمّام الأخضر** على الحائط الأيسر
- **STAGING مقفل:** الديباناج دائماً في الشارع يساراً عند العمود • المرسيدس/الستيبواي دائماً على الرصفة قدام البوابة اليمنى المفتوحة، المقدمة نحو اليسار، جهة السائق نحو الكاميرا • الشارع والضوء والمواقع لا يتغيرون بين اللقطات — فقط الحركة والكاميرا
- **SC01 لقطتان:** `SC01_A` (الوصول — المرسيدس فوق الديباناج) + `SC01_B` (بعد النزول — على الأرض قدام الكراج)

## الكتل المشتركة (تُلصق في كل برومبت)

**[IMG-COMMON]:**
```
Photorealistic cinematic film still, like a real Algerian TV drama, live-action look. LANDSCAPE 16:9, 1376x768. Natural light, realistic hands and anatomy, real skin texture. Characters look at what they interact with and never at the camera. Vehicles always at TRUE REALISTIC scale and distance — never oversized, never exaggerated, real-world proportions. No text, no logos, no watermark, no extra people, no duplicated limbs, no 3D, no cartoon.
```

**[EXT]:**
```
Exact garage exterior of REF_GARAGE_EXTERIOR (Master Reference, LOCKED design): an old worn CONCRETE building on a street corner in a working-class Algerian neighborhood. The main facade has TWO adjacent huge bays, BOTH WIDE OPEN — their rusty blue-grey metal doors fully raised, both interiors fully visible. Inside the two bays ONLY mechanic tools and equipment (a red tool cabinet, a workbench, wall-mounted tools) and ONE BLUE vintage Renault 4 raised on a blue two-post hydraulic lift in the right bay — no other cars, no barrels, no clutter. Above the left bay a row of rectangular glass transom windows. A tall concrete utility pole stands exactly at the LEFT corner of the building where the street branches toward the background left between old faded light-yellow and white houses with crossing electric wires. Cracked asphalt apron with dark oil stains in front. Morning sunlight from the street side. Do not mirror. NEVER close a bay, NEVER change the street layout, NEVER resize cars.
```

**[WS-INT]:**
```
Exact workshop interior of REF_WORKSHOP_INT: worn concrete floor, car on the hydraulic lift, wooden worktable, oil barrels, stacked tires, the two bright roll-up street entrances, the narrow side corridor with the office door DEEP in the background, the pale-green WC door on the LEFT wall mid-ground. Do not mirror.
```

**[OFFICE-INT]:**
```
Exact office interior of REF_OFFICE_INT: small room deep in the workshop, wooden desk facing the door, the wooden money box with hinged lid on the LEFT side of the desk, a small grey desk calculator and one unreadable handwritten supplier invoice paper beside it, the CCTV monitor on the wall to the RIGHT of the desk, small tea glass, hanging key, warm practical light. No computer. Do not mirror.
```

**[VID-COMMON]:**
```
Image-to-video, LANDSCAPE 16:9, duration EXACTLY 10 seconds, ONE continuous shot. Strict locked-off tripod shot — zero pan, zero zoom, zero camera movement. Keep the first frame exactly: same faces, clothes, body proportions, vehicles, plates, room layout and lighting. Photorealistic live-action look like a real Algerian TV drama, natural subtle motion only. No morphing, no face changes, no new characters, no objects appearing or disappearing, no text, no subtitles, no logos, no watermark. Characters look at what they interact with, never into the camera. Mouths move naturally as if speaking Algerian Darija.
```

**[VID-NEG]:**
```
cartoon, 3D render, anime, camera pan, camera zoom, camera movement, cut inside the clip, scene change, distorted hands, extra fingers, extra limbs, face morphing, identity drift, flickering, warped floor, duplicated people, extra people, text overlay, subtitles, watermark, looking at camera, wrong license plate, changed car shape, fast motion, music
```

---

# الفصل الأول — «زبون المرسيدس والفيزيبل» (اليوم 1، صباحاً)

### SC01 — الوصول • خارجي/صباح • Wide Shot
**المراجع:** REF_GARAGE_EXT_CORNER + REF_TOW_TRUCK + REF_CUSTOMER_A + HAJ_FRONT
**KEYFRAME:** `[IMG-COMMON] [EXT]` The orange flatbed tow truck parked on the street at the LEFT with its loading ramp DOWN and the black luxury sedan rolling off it onto the apron, mid-unload. CUSTOMER A stands center-frame facing the garage, NO phone, one hand gesturing mid-speech, worried but polite. HADJ steps out of the entrance toward him, welcoming. AMINE small inside the bay. Wide eye-level.
**VIDEO (10ث):** 0-3s the customer speaks warmly with natural hand gestures, no phone anywhere; 3-7s the sedan rolls slowly down the ramp onto the apron, nose ending LEFT; 7-10s Hadj answers with a proud welcoming gesture toward Amine inside. 
**الحوار (حرفياً):**
- **الزبون:** «السَّلَامْ عَلَيْكُمْ يَا الْحَاجْ، أَجْرِي لِي رَانِي كُنْتْ نْسُوقْ فِي لُوطُورُوتْ حَتَّى طْفَاتْ الطُّونُوبِيلْ وَمَا حَبَّتْشْ تْنُوضْ، رَانِي جَبْتْهَا فِي الدِّيبَانَاجْ!»
- **الحاج:** «مَرْحْبَا بِيكْ خُويَا، مَا تَتْقَلَّقْشْ، رَاهْ عَنْدْنَا الْمَايْسْتْرُو تَاْعْنَا أَمِينْ دُرُوكْ يَتْهَلَّى فِيكْ.»
**SOUND:** شارع + محرك الشاحنة الخامل. **END:** إشارة الحاج الترحيبية نحو أمين.

### SC02 — الفحص • خارجي/صباح • Medium-Wide
**المراجع:** REF_GARAGE_EXT_CORNER + REF_MERCEDES + REF_CUSTOMER_A + AMINE_FRONT
**KEYFRAME:** `[IMG-COMMON] [EXT]` No tow truck. The black sedan parked on the apron, nose LEFT, driver side to camera, HOOD OPEN. AMINE leans into the engine bay checking calmly. CUSTOMER A stands beside him, tense, hands clasped, no phone. Medium-wide, both from knees up.
**VIDEO (10ث):** 0-4s Amine runs his fingers carefully along the wiring, absorbed; 4-8s the customer shifts his weight and speaks his worry; 8-10s Amine answers without looking up, reassuring nod.
**الحوار:**
- **الزبون:** «وَاللهْ يَا خُويَا كُنْتْ نْسُوقْ بِيهَا عَادِي حَتَّى طْفَاتْ... رَانِي خَايْفْ لَا يَكُونْ كُولَالِي الْمُوتُورْ!»
- **أمين:** «الْمُوتُورْ رَاهْ لَابَاسْ بِيهْ، مَا تْقَلَّقْ رُوحَكْ.»
**SOUND:** لمسات معدن خفيفة + شارع.

### SC03 — الاكتشاف • خارجي/صباح • Medium Close
**المراجع:** REF_GARAGE_EXT_CORNER + REF_MERCEDES + AMINE_FRONT + REF_CUSTOMER_A
**KEYFRAME:** `[IMG-COMMON] [EXT]` At the open engine bay: AMINE holds the black plastic FUSE BOX in one hand and, in the other hand, ONE small blackened burnt blade fuse shown clearly to the customer, calm confident look. CUSTOMER A leans in, his face caught BETWEEN laughter and tears — comic shock. Both faces visible.
**VIDEO (10ث):** 0-4s Amine lifts the burnt fuse into the light beside the open fuse box and speaks; 4-9s the customer's face travels from frown to disbelief to a strangled half-laugh, hand covering his mouth; 9-10s he shakes his head in amazement.
**الحوار:**
- **أمين:** «بَسْبَابْ هَادْ الْفِيزِيبْل الْمَحْرُوقْ تَاعْ خَمْسِينْ دِينَارْ، مَا حَبَّتْشْ تْنُوضْلَكْ الطُّونُوبِيلْ.»
**SOUND:** نقرة معدنية خفيفة + شارع. **END:** وجه الزبون المشدوه بين الضحك والبكاء.

### SC04 — التشغيل • خارجي/صباح • Medium-Wide
**المراجع:** REF_GARAGE_EXT_CORNER + REF_MERCEDES + AMINE_FRONT + REF_CUSTOMER_A
**KEYFRAME:** `[IMG-COMMON] [EXT]` The sedan nose LEFT, hood open, driver door open: CUSTOMER A in the driver seat, hand near the start button, face turned to Amine. AMINE beside the engine bay having just pressed the new fuse into the fuse box, looking up at the customer with a confident nod.
**VIDEO (10ث):** 0-3s Amine presses the tiny fuse into place, closes the fuse box lid, says his line; 3-6s the customer presses the start button — the engine starts IMMEDIATELY, dashboard lights on; 6-10s his face floods with relief and joy, he pats the steering wheel, Amine smiles modestly.
**الحوار:**
- **أمين:** «رَانِي فْرِيتْهَالِكْ خُوِيَا، جَرَّبْ دِيمَارِي.»
**SOUND:** تشغيل نظيف للمحرك + هدير خفيف. **END:** فرحة الزبون خلف المقود.

### SC05 — الدفع والأمانة • خارجي/صباح • Medium three-shot
**المراجع:** REF_GARAGE_EXT_CORNER + REF_MERCEDES + REF_CUSTOMER_A + AMINE_FRONT + HAJ_FRONT
**KEYFRAME:** `[IMG-COMMON] [EXT]` Hood closed. HADJ stands with them, hands relaxed, a gentle proud smile. CUSTOMER A holds out a THICK bundle of Algerian banknotes (colors visible, unreadable) toward Amine with both hands, insisting. AMINE, one open palm raised in polite refusal, his other hand already holding ONE single banknote (the 2000-dinar note) he took from the bundle. Medium three-shot.
**VIDEO (10ث):** 0-3s Hadj says his line with a warm proud gesture toward Amine; 3-7s the customer insists with the thick bundle; 7-10s Amine raises his palm gently, shows the single note between two fingers, and speaks his line with humble firmness; the customer's bundle slowly withdraws.
**الحوار:**
- **الحاج:** «مَا قُلْتْلَكْشْ رَاهْ عَنْدْنَا مَايْسْتْرُو تَاعْ طُونُوبِيلَاتْ؟»
- **أمين:** «هَذَا هُوَ حَقِّي يَا خُويَا، الْبَرَكَة فِي الْقَلِيلْ وَمَا نَخْدَعْشْ خُويَا.»
**SOUND:** شارع فقط. **END:** الورقة الواحدة في يد أمين.

### SC06 — المغادرة • خارجي/صباح • Medium→Wide
**المراجع:** REF_GARAGE_EXT_CORNER + REF_MERCEDES + REF_CUSTOMER_A
**KEYFRAME:** `[IMG-COMMON] [EXT]` CUSTOMER A beside his sedan's open driver door, one hand on the roof, speaking toward the garage with a deeply moved grateful smile — Hadj and Amine visible small at the entrance behind. 
**VIDEO (10ث):** 0-5s the customer speaks his farewell line from the heart, hand on his chest then on the car roof; 5-8s he gets in, closes the door; 8-10s the sedan pulls away to the LEFT, getting smaller past the two entrances.
**الحوار:**
- **الزبون:** «بَارَكَ اللهُ فِيكْ عَلَى حُسْنْ الْمُعَامَلَة تَاعْكْ، رَاكُمْ قْلَالْ فْهَادْ الزَّمَانْ.» (ثم يركب وينطلق)
**SOUND:** باب السيارة + إطارات على الأسفلت. **END:** المرسيدس تبتعد على اليسار.

---

# الفصل الثاني — «زبون الستيبواي والمكيدة» (اليوم 2، صباحاً)

### SC07 — وصول الزبون الثاني • خارجي/صباح الغد • Medium-Wide
**المراجع:** REF_GARAGE_EXT_CORNER + REF_DACIA_STEPWAY + REF_CUSTOMER_B + AMINE_FRONT
**KEYFRAME:** `[IMG-COMMON] [EXT]` Next morning. The slate-grey Stepway parked on the apron, nose LEFT, plate 58214 123 16 (blank if not exact), HOOD OPEN. CUSTOMER B stands with AMINE in front of the open engine, explaining his problem with expressive hands. Amine listens, arms half-crossed, thoughtful.
**VIDEO (10ث):** 0-4s the customer describes the starting trouble with hand gestures toward the engine; 4-7s Amine leans in, looks at the starter area, nods slowly; 7-10s Amine answers his diagnostic line, tapping the fender lightly.
**الحوار:**
- **الزبون 2:** «الصَّبَاحْ جِيتْ نْنُوضْهَا مَا حَبَّتْشْ، نَسْمَعْهَا حَابَّة تْدِيمَارِي بَصَّحْ تْعَاوْدْ تَطْفَى.»
- **أمين:** «مَا يَكُونْ غِيرْ الْكُونْتَاكْتُورْ وَلَا الدِّيمَارُورْ.»
**SOUND:** شارع صباحي. **END:** إيماءة أمين الفنية.

### SC08 — التصليح • ورشة/صباح • Close-up (بلا حوار)
**المراجع:** REF_WORKSHOP_INT + REF_DACIA_STEPWAY + AMINE_FRONT
**KEYFRAME:** `[IMG-COMMON] [WS-INT]` CLOSE-UP at the Stepway's open engine bay inside the workshop: AMINE's two hands carefully fitting the new STARTER MOTOR (ديمارور) into place with a wrench, his focused face partially visible above, work light on the metal, red rag hanging from his pocket.
**VIDEO (10ث):** 0-4s his hands seat the starter and align its bolts with quiet precision; 4-7s he tightens one bolt with the wrench, a soft metallic creak; 7-10s he wipes his hands briefly on the red rag and inspects his work with a small satisfied nod. NO DIALOGUE.
**SOUND:** مفتاح ربط + صرير معدن خفيف. **END:** نظرة الرضا.

### SC09 — التجربة • ورشة/صباح • Medium
**المراجع:** REF_WORKSHOP_INT + REF_DACIA_STEPWAY + REF_CUSTOMER_B + AMINE_FRONT
**KEYFRAME:** `[IMG-COMMON] [WS-INT]` The Stepway inside the workshop, driver door OPEN: CUSTOMER B in the driver seat, hand near the key, face turned to Amine. AMINE stands beside the open door giving the go-ahead nod. Hood closed now.
**VIDEO (10ث):** 0-3s Amine says his line and nods; 3-6s the customer turns the key — the engine fires UP ON THE FIRST TRY, his face lights up; 6-10s he gives Amine a thumbs-up through the open window; Amine nods modestly.
**الحوار:**
- **أمين:** «رَانِي خْدَمْتْهَالِكْ خْوِيَا، جَرَّبْ دِيمَارِي.»
**SOUND:** اشتعال المحرك من الأولى. **END:** إبهام الزبون.

### SC10 — الدفع في المكتب • مكتب/قبيل الظهر • Medium (بلا حوار)
**المراجع:** REF_OFFICE_INT + REF_CUSTOMER_B + HAJ_FRONT
**KEYFRAME:** `[IMG-COMMON] [OFFICE-INT]` HADJ seated behind the desk; on the desk the grey calculator, the unreadable supplier invoice paper, and the wooden money box OPEN with the thick supplier bundle visible inside. CUSTOMER B on the visitor side hands a neat stack of banknotes; Hadj receives it, about to place it into the box.
**VIDEO (10ث):** 0-3s the customer holds out the neat stack; 3-7s Hadj takes it, places it INSIDE the wooden box beside the thick bundle, closes the hinged lid with a soft wooden click; 7-10s a polite nod exchange. NO DIALOGUE.
**SOUND:** حشرجة ورق + نقرة خشب الصندوق. **END:** غطاء الصندوق ينسكّر.

### SC11 — الاستئذان • ورشة/قبيل الظهر • Medium-Wide
**المراجع:** REF_WORKSHOP_INT + REF_CUSTOMER_B + HAJ_FRONT
**KEYFRAME:** `[IMG-COMMON] [WS-INT]` Just outside the office corridor, in the main workshop: CUSTOMER B asks politely, one hand slightly raised. HADJ points with his open hand toward the pale-green WC door on the LEFT wall mid-ground. The corridor and office door deep in the background right.
**VIDEO (10ث):** 0-3s the customer asks his question; 3-6s Hadj points kindly with his open hand toward the green door and nods; 6-10s the customer walks away toward the WC door while Hadj turns and walks toward Amine's direction in the workshop.
**الحوار:**
- **الزبون:** «يَا الْحَاجْ، رَانِي حَابْ نْرُوحْ لِلْمَرْحَاضْ، وِينْ رَاهْ؟»
- *(الحاج يشير له بيده نحوه — بلا كلام)*
**SOUND:** خطوات + ورشة هادئة. **END:** الزبون يمشي نحو الباب الأخضر.

### SC12 — المغادرة • خارجي/قبيل الظهر • Wide (بلا حوار)
**المراجع:** REF_GARAGE_EXT_CORNER + REF_DACIA_STEPWAY + REF_CUSTOMER_B + HAJ_FRONT + AMINE_FRONT
**KEYFRAME:** `[IMG-COMMON] [EXT]` The Stepway on the apron nose LEFT, CUSTOMER B at the open driver door RAISING HIS HAND in a friendly wave toward the garage. HADJ and AMINE stand together at the entrance, both waving back warmly, relaxed faces — a completely ordinary friendly goodbye.
**VIDEO (10ث):** 0-4s the customer waves from beside the car; 4-7s he gets in; 7-10s the Stepway pulls away to the LEFT, Hadj and Amine's small waves at the entrance, the car shrinking down the street.
**SOUND:** باب + محرك + إطارات. **END:** الستيبواي تبتعد والحاج وأمين يلوّحون.

---

# الفصل الثالث — «الصدمة» (نفس اليوم، الظهر — Cliffhanger)

### SC13 — وقت الصلاة • ورشة/الظهر • Medium two-shot
**المراجع:** REF_WORKSHOP_INT + HAJ_FRONT + AMINE_FRONT
**KEYFRAME:** `[IMG-COMMON] [WS-INT]` Early-afternoon warm light. HADJ and AMINE stand talking calmly in the middle of the workshop near the worktable, Hadj one hand half-raised as he mentions the prayer, both relaxed.
**VIDEO (10ث):** 0-4s Hadj speaks his line calmly, gesturing loosely toward the entrance; 4-8s Amine nods, starts tidying a tool on the worktable; 8-10s Hadj turns toward the deep office corridor.
**الحوار:**
- **الحاج:** «أَذَّنْ الظُّهْرْ... نْرُوحُو نْصَلُّو وَنْفْطَرُو وَمْبَعْدْ نْوَلُّو.»
**SOUND:** **أذان الظهر بعيد في الخلفية** + أجواء هادئة. **END:** الحاج يتجه نحو الممر.

### SC14 — تحضير المال • مكتب/الظهر • Medium
**المراجع:** REF_OFFICE_INT + HAJ_FRONT
**KEYFRAME:** `[IMG-COMMON] [OFFICE-INT]` HADJ alone in the office: he holds the handwritten supplier invoice paper, placing it flat on the desk beside the calculator, his other hand resting on the closed wooden money box, about to open it.
**VIDEO (10ث):** 0-4s he lays the invoice paper on the desk and murmurs his line to himself; 4-8s his fingers settle on the box lid; 8-10s he lifts the hinged lid SLOWLY — a sliver of the dark box interior appears.
**الحوار:**
- **الحاج (لنفسه):** «نْوَجَّدْ دْرَاهَمْ الْفُورْنِيسُورْ قْبْلْ مَا يَجِي.»
**SOUND:** ورقة + صمت مشدود. **END:** الغطاء يرتفع ببطء.

### SC15 — الاكتشاف الصادم • مكتب/الظهر • Close-up
**المراجع:** REF_OFFICE_INT + HAJ_FRONT
**KEYFRAME:** `[IMG-COMMON] [OFFICE-INT]` CLOSE on HADJ: the wooden money box OPEN and EMPTY on the desk (only maybe one or two loose small notes at most), his hands frozen on its edges, his face EXPLODING with shock and fury, mouth open mid-scream, eyes wide.
**VIDEO (10ث):** 0-3s he stares into the open empty box, frozen; 3-7s the shock breaks — his voice ERUPTS in the scream line, a hand slamming the desk edge; 7-10s he shouts Amine's name toward the door, half-rising from the chair.
**الحوار:**
- **الحاج:** «وَاشْ هَذَا!! دْرَاهَمْ الْفُورْنِيسُورْ طَارُو!! يَا أَمِيـــنْ!!»
**SOUND:** كف على الخشب + الصرخة. **END:** الحاج نصف واقف يصرخ نحو الباب.

### SC16 — النداء • ورشة/الظهر • Wide (خالية — صوت فقط)
**المراجع:** REF_WORKSHOP_INT
**KEYFRAME:** `[IMG-COMMON] [WS-INT]` The workshop almost EMPTY — no people visible: the car on the lift, the worktable with the red rag folded on it, quiet early-afternoon light, the office corridor deep in the background. A still, tense, empty frame.
**VIDEO (10ث):** 0-4s the empty workshop breathes: dust drifts in the light shafts, a hanging cable sways faintly; 4-8s from OUTSIDE the frame Amine's distant voice answers the call; 8-10s faint footsteps approach off-screen.
**الحوار (صوت فقط، من خارج الكادر):**
- **أمين (صوت):** «رَانِي جَايْ يَا الْحَاجْ! دْقِيقَة بَرْكْ رَانِي جَايْ!»
**SOUND:** صمت الورشة + الصوت البعيد + خطوات تقترب. **END:** الكادر الفارغ المشدود.

### SC17 — الأثر • ممر المكتب/الظهر • Close (بلا حوار)
**المراجع:** OIL_CORRIDOR + AMINE_FRONT
**KEYFRAME:** `[IMG-COMMON]` The narrow side corridor leading to the office door (exact OIL_CORRIDOR reference): AMINE stopped mid-step at the corridor, looking DOWN at DARK OILY FOOTPRINTS on the concrete floor leading toward the office door, his brow furrowed in suspicion, the red rag in his hand. The prints are in the foreground, clearly visible.
**VIDEO (10ث):** 0-3s Amine walks into the corridor and STOPS suddenly mid-step; 3-7s the camera holds as his eyes drop to the oily footprints; he crouches slightly, examining them without touching, suspicion deepening on his face; 7-10s he straightens slowly, looks toward the office door, then exits frame toward it.
**SOUND:** صمت + خطوات تتوقف. **END:** نظرة الشك نحو باب المكتب.
*(بدون حوار)*

### SC18 — الحاج المنهار • مكتب/الظهر • Medium two-shot
**المراجع:** REF_OFFICE_INT + AMINE_FRONT + HAJ_FRONT
**KEYFRAME:** `[IMG-COMMON] [OFFICE-INT]` AMINE just entered, standing concerned near the doorway. HADJ COLLAPSED on his chair — slumped, one hand over his forehead, devastated, the empty open money box on the desk beside the invoice paper.
**VIDEO (10ث):** 0-4s Amine asks his worried question, stepping one step closer; 4-9s Hadj lifts his head heavily and answers, his voice broken, gesturing weakly at the open empty box; 9-10s Amine's eyes lock onto the box.
**الحوار:**
- **أمين:** «غِيرْ الْخِيرْ إِنْ شَاءَ اللهْ يَا الْحَاجْ؟ رَاكْ خَلَّعْتْنِي.»
- **الحاج:** «وَاللهْ مَا رَانِي مْلِيحْ كَامِلْ يَا وَلِيدِي... جِيتْ نَحْسَبْ دْرَاهَمْ الْفُورْنِيسُورْ مَا لْقِيتْ وَالُو!»
**SOUND:** أجواء مكتب ثقيلة. **END:** عين أمين على الصندوق الفارغ.

### SC19 — الخاتمة المفتوحة • مكتب/الظهر • Medium Close
**المراجع:** REF_OFFICE_INT + AMINE_FRONT + HAJ_FRONT
**KEYFRAME:** `[IMG-COMMON] [OFFICE-INT]` AMINE leans forward, suddenly alert — the connection lighting up in his eyes, one hand half-raised mid-thought, finger almost pointing back toward the corridor. HADJ looks up at him from the chair, a fragile hope in his broken face.
**VIDEO (10ث):** 0-5s Amine speaks fast, connecting the events, his hand gesturing back toward the corridor and the footprints; 5-9s he leans closer to Hadj, urgency rising; 9-10s his mouth opens to say what he saw — **HARD CUT TO BLACK** (يُضاف القطع للسواد في CapCut — ليس داخل كليب Flow).
**الحوار:**
- **أمين:** «بَصَّحْ اصْبَرْ دْقِيقَة يَا الْحَاجْ... رَانِي قْبَلْ مَا نَدْخُلْ عَنْدَكْ هُنَا، شُفْتْ حَاجَة بِيِزَارْ...»
- *(شاشة سوداء — نهاية الحلقة الأولى، الربط المباشر مع الحلقة الثانية)*
**SOUND:** صوت أمين المتصاعد ثم **صمت مفاجئ مع السواد**.

---

# ملاحظات المونتاج (CapCut)
- الترتيب: SC01→SC19 ثم **قطع مباشر للسواد** في نهاية SC19 (نص الحلقة القادمة اختياري: «...تكمل في الحلقة الثانية»)
- الأصوات: حوار + بيئة فقط (شارع/ورشة/مكتب) + **الأذان البعيد في SC13** — **بلا موسيقى**
- القفزات الزمنية بالقطع المباشر: SC06→SC07 (يوم 1 ← يوم 2) وSC12→SC13 (قبيل الظهر ← الظهر)
- القاعدة الذهبية: **السارق لا يظهر إطلاقاً** في هذه الحلقة — حتى في الخلفية

# ترتيب التنفيذ
1. ✅ المراجع: 3 بيئة جديدة (اليوم) + الشخصيات والسيارات (جاهزون)
2. ⏳ صور KEYFRAME الـ19 (موجة بعد موجة: خارجية 01-07 ← ورشة/مكتب 08-11 ← خارجية 12 + الفصل الثالث 13-19)
3. ⏳ الفيديو بنفس الترتيب في Flow (مراجع ← إطار ← برومبت)
4. ⏳ مونتاج CapCut + الحزمة
