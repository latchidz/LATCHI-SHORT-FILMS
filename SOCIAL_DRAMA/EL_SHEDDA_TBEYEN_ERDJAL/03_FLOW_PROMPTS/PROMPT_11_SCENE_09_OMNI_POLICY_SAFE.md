# 🎬 PROMPT 11 — SCENE 09 (OMNI 1.1 FLASH FIXED · QA V2)
## THE DOOR OPENS — Clinic Waiting Room Reunion (Twist Part 1)

| البند | الإعداد المعتمد |
|---|---|
| **Model** | `Gemini Omni 1.1 Flash` (Google Flow) |
| **Mode** | `Video > Frames > First and last` |
| **Aspect / Duration** | `9:16` · `8 seconds` · `24fps` |
| **Audio** | **Native Algerian Darija Speech ON** · **ZERO Background Music** |
| **FIRST FRAME** | `02_SCENES/SCENE_09/S09a_DOOR_OPENS_FIXED.png` |
| **LAST FRAME** | `02_SCENES/SCENE_09/S09b_FOUR_MEN_RISE_FIXED.png` |

---

## 🔍 تقرير الفحص والتصحيح للمشهد 09 (`QA Audit`)
1. **إصلاح توقيت الليل (`Night Continuity`):** في النسخة السابقة كان يظهر ضوء نهار ساطع خلف الباب والنافذة العلوية رغم أن المشهد 08 ليلي والحوار يقول *«في هاد الليل»* — تم ضبط النافذة العلوية على ظلام الليل والممر الخلفي على إضاءة مستشفى ليلية خافتة مع ضبط ساعة الحائط على `10:10` ليلاً.
2. **إصلاح ملامح الوقار وإغلاق الفم (`Expression & Lip-Sync Lock`):** تم إلغاء الابتسامات العريضة في `S09b` وفتح الفم المسبق في `S09a`، وضبط الوجوه الخمسة على وقار وهيبة المستشفى بأفواه مغلقة في البداية والنهاية لكي تخرج مزامنة الشفاه (`Lip-sync`) في Google Flow نظيفة 100%.
3. **إصلاح هندسة الكراسي والباب:** ضبط 4 كراسي انتظار برتقالية متصلة بدون أي قطعة حديد مشوهة تحت عمي حمزة، وفتح الباب الزجاجي المضبب للداخل بعيداً عن الكراسي مع تطابق كاميرا التريپود بنسبة `100%` بين `S09a` و`S09b`.
4. **تطابق المراجع الجديدة (`V2 Cast`):** أمين بمرجع `REF_AMIN_V2_MASTER_SHEET.png` بقميص الفيلم الزيتي والملف الطبي الخالي من النصوص، ويوسف بمرجع `REF_YOUSSEF_V2_SUNGLASSES_MASTER_SHEET.png` بالنظارات السوداء المستطيلة والظرف البني المغلق بإحكام، مع رامي وكريم وعمي حمزة.

---

## 📋 البرومبت المصلّح الجاهز للّصق مباشرة في Google Flow

```text
In a single unbroken scene and a single continuous shot with a completely static, locked-off tripod camera from start to finish. No scene cuts, no pans, and no zooms. Vertical 9:16, 8 seconds, 24fps. Photorealistic live-action Algerian family hospital drama shot on 35mm Cinestill 800T film stock inside a pale-green hospital waiting room at night under overhead fluorescent tubes, natural skin pores, organic film grain.

FRAME AND SET LOCK:
Animate smoothly in one unbroken take from <FIRST_FRAME> to <LAST_FRAME>. Keep the blank pale-green hospital walls (zero posters, zero text), the round analog wall clock reading 10:10 at night, the dark night sky visible through the high upper-right transom window, the open frosted-glass doorway leading to the dimly lit hospital corridor on the right, the speckled terrazzo floor, and the row of orange plastic waiting chairs along the left wall 100% locked in place without shifting or mirroring.

CHARACTER, MOOD, AND GAZE LOCK:
Solemn, heavy, dignified hospital mood — strictly no smiling or grinning. The camera is an invisible observer — zero eye contact with the lens by any of the five men.
- AMIN (standing on the right just inside the open doorway facing left): Exact Algerian father with sleek short flat-layered dark hair and clean high skin-fade, sparse-cheek short trimmed chin beard (~1 cm), wearing his worn olive-green long-sleeve button-up shirt, dark charcoal trousers, and dark shoes, holding his plain blank manila medical folder.
- THE FOUR FRIENDS ON THE LEFT (facing right toward Amin): YOUSSEF (short buzz cut, black rolled-sleeve button-up shirt, dark trousers, black rectangular sunglasses kept permanently over his eyes in every frame, holding a completely sealed plain brown kraft A4 envelope with closed flap and zero visible contents), RAMI (dark-blue mechanic coveralls and brown work boots), KARIM (spiky fade hair, black button-up shirt, black jeans, white sneakers), and UNCLE HAMZA (grey beard, grey polo shirt, stained dark-green grocer's apron).

TIMING AND PHYSICAL ACTION (8 SECONDS, SINGLE CONTINUOUS SHOT):
[0.0s–2.6s] Starting from <FIRST_FRAME>, Amin stands stunned just inside the right doorway holding the manila folder against his chest with both hands, looking across the room at his four seated friends; ONLY Amin speaks in a quiet, surprised, emotional Algerian Darija male voice while the four friends remain seated looking solemnly at him:
"خاوتي؟ واش جابكم لهنا في هاد الليل؟"
[2.6s–7.2s] Immediately after Amin finishes speaking, all four friends rise smoothly and respectfully together from the orange plastic chairs to stand upright side-by-side in front of the chairs facing Amin in silent brotherly solidarity — Youssef holding the sealed brown A4 envelope with both hands in front of his waist, sunglasses firmly over his eyes. As Amin holds the medical folder in his left hand and places his right palm quietly flat over his heart on his chest, ONLY Youssef speaks in a calm, steady, dignified Algerian Darija male voice from 3.0s to 7.1s:
"حسبت نخلّوك وحدك يا أمين؟ الدكتور خبّرنا وفرزنا معاه كلشي على العملية."
[7.2s–8.0s] Complete vocal silence with closed, solemn mouths as all five men hold the exact standing positions of <LAST_FRAME> looking quietly at one another across the waiting room.

SOUND DESIGN:
Natural Algerian Darija speech with accurate side-profile lip-sync, subtle plastic chair creak and quiet footsteps on hospital terrazzo as the four men stand up, soft night fluorescent hum. Strictly no background music, no subtitles, no wall text, and no watermarks.
```
