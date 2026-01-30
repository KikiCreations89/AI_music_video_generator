from audio.analyze_audio import analyze_audio
from ai.prompt_generator import generate_prompts
from ai.image_generator import generate_images
from video.video_builder import build_video

AUDIO_FILE = "assets/audio/sample.mp3"
THEME = "gothic vampire forest"
OUTPUT_VIDEO = "assets/output/music_video.mp4"

tempo, beat_count = analyze_audio(AUDIO_FILE)
prompts = generate_prompts(THEME, max(1, beat_count // 4))
images = generate_images(prompts, "assets/frames")
build_video(images, OUTPUT_VIDEO)

print("🎬 Video created successfully")

