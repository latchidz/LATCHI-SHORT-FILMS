---
name: idea-to-video-story
display_name: Ai Video Story Creator
description: Use when the user wants to turn a simple idea into an organized, consistent AI-generated video story — a structured multi-scene story (10-second scenes, consistent characters, narration/dialogue, hook and twist ending) for YouTube Shorts or short-form video, plus optionally generated character sheets, scene video clips, voiceover, music, and a final assembled video. Also use for story/script-only, character-only, or single-scene stages.
allowed-tools:
- generate_image
- generate_video
- generate_tts
- generate_music
- mix_clips
- create_document
- update_document
- get_document
---


# AI Video Story Creator

Turn any simple idea into an engaging, original short-video story designed for AI-generated videos, then (optionally) produce the actual video with consistent characters and a final assembled cut.

## When to use
- User gives a simple idea and wants an organized, consistent AI video story.
- User wants a story/script, character sheets, scene clips, voiceover, music, or the full idea-to-video pipeline.
- User wants to revise a story or continue to the next stage.

## Reference files
- `references/story-rules.md`: the full SHORTS STORY ARCHITECT spec (story structure, character bible, visual prompts, continuity, narration, output format, packaging). Read it before writing any story.

## Steps

### 0. Plan
First call `write_todos` to list the stages and update it as you progress. If the idea isn't given, ask for it. Confirm preferences: total length (user-controlled; default 20–30 seconds if unspecified — see the duration rules in `references/story-rules.md`), orientation (default portrait 9:16 for YouTube Shorts; landscape if requested), and whether to include voiceover + music (default yes).

### 1. Write the story
Read `references/story-rules.md` and produce the structured story exactly per its output format (title, video overview, character bible, global visual rules, scene-by-scene plan with duration + visual prompt + narration + sound design + continuity note, final payoff, and YouTube Shorts packaging). Save it with `create_document(content=<story>, name=<title>, entity_type='scripts')` and show the user the story.

### 2. Generate character sheets
For each main character, generate a consistent reference image with `generate_image` (model='t2i', orientation matching the video, name=<character name>, entity_type='characters'). Keep appearance, clothing, and colors identical across characters and scenes.

### 3. Generate scene clips
For each scene, generate a video with `generate_video` (model='ref2v', input_urls=[the character reference image(s) appearing in that scene], prompt=<the scene's visual prompt>, orientation=<same as the video>, duration=~10, name='Scene N', entity_type='scene_videos'). Keep the prompt faithful to the story's visual prompt. If the tool only supports short clips (e.g. ~10s), generate each scene as its own clip and assemble them later — never claim a single long clip was produced when the tool only supports shorter ones.

### 4. Voiceover + music (optional, default on)
- Narration/dialogue: `generate_tts` (model='tts.design', text=<scene narration/dialogue>, voice_instruction=<one consistent voice>, name='Narration', entity_type='voiceovers').
- Background music: `generate_music` (model='music', prompt=<mood matching the story>, name='Soundtrack', entity_type='music').

### 5. Assemble the final video
Stitch the scene clips in order with `mix_clips` (clips=[{video:<scene clip>, audio:<voiceover>}, ...], add the music track, and burn in subtitles from the narration via clips[].subtitles). Use `probe_media` first if you need to check clip durations. name=<title>, entity_type='final_videos'.

### 6. Wrap up
Summarize what was produced in natural language. Call `set_guidance` to suggest next actions (e.g. tweak the story, change a scene, make it longer, redo a character).

## Notes
- Keep character appearance, clothing, colors, and personality consistent across all scenes; avoid unnecessary design or location changes between connected scenes.
- Each scene is ~10 seconds; scene count follows the user's requested duration (see duration rules in `references/story-rules.md`).
- Report failures honestly; never fabricate URLs. Video generation does not support NSFW/adult content — politely decline such requests.
- Intermediate products (story, character sheets, scene clips) will be visible on the canvas.