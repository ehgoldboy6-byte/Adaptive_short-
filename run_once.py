from moviepy.editor import VideoFileClip, AudioFileClip
from gtts import gTTS
import os
import random
from datetime import datetime

# =========================
# 1. LOAD SCRIPT ACAK
# =========================

with open("scripts/psychology_facts.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

script_text = random.choice(lines)

print("Script terpilih:")
print(script_text)

# =========================
# 2. TEXT TO SPEECH
# =========================

os.makedirs("output", exist_ok=True)

voice_path = "output/voice.mp3"
tts = gTTS(text=script_text, lang="id")
tts.save(voice_path)

print("Voice dibuat.")

# =========================
# 3. VIDEO + AUDIO
# =========================

video = VideoFileClip("assets/bg_video.mp4")
voice = AudioFileClip(voice_path)

final_video = video.subclip(0, voice.duration).set_audio(voice)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_path = f"output/video_{timestamp}.mp4"

final_video.write_videofile(
    output_path,
    codec="libx264",
    audio_codec="aac"
)

print("Selesai:", output_path)
