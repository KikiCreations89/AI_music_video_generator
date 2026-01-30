from moviepy.editor import ImageSequenceClip

def build_video(image_paths, output_path):
    clip = ImageSequenceClip(image_paths, fps=2)
    clip.write_videofile(output_path)
