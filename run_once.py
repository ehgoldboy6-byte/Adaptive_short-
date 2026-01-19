from moviepy.editor import VideoFileClip, AudioFileClip
from gtts import gTTS
import os
from datetime import datetime

# =========================
# 1. SCRIPT SEDERHANA
# =========================

script_text = (
    "Tanpa sadar, pikiran kita sering lelah bukan karena masalah besar, "
    "tapi karena hal kecil yang terus kita ulang di kepala."
)

print("Script:")
print(script_text)

# =========================
# 2. TEXT TO SPEECH
# =========================

os.makedirs("output", exist_ok=True)

voice_path = "output/voice.mp3"
tts = gTTS(text=script_text, lang="id")
tts.save(voice_path)

print("Voice berhasil dibuat.")

# =========================
# 3. GABUNG VOICE + VIDEO
# =========================

video = VideoFileClip("assets/bg_video.mp4")
voice = AudioFileClip(voice_path)

# Potong video sesuai durasi suara
final_video = video.subclip(0, voice.duration).set_audio(voice)

# Nama file output
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_path = f"output/video_{timestamp}.mp4"

final_video.write_videofile(
    output_path,
    codec="libx264",
    audio_codec="aac"
)

print("Video selesai dibuat:", output_path)
