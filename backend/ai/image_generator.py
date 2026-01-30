from PIL import Image
import os

def generate_images(prompts, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    images = []

    for i, prompt in enumerate(prompts):
        img = Image.new("RGB", (512, 512), color=(20, 20, 20))
        path = f"{output_dir}/frame_{i}.png"
        img.save(path)
        images.append(path)

    return images
