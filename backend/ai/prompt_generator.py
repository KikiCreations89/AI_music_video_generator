def generate_prompts(theme, count):
    return [
        f"{theme}, cinematic gothic fantasy, dark forest, fog, dramatic lighting"
        for _ in range(count)
    ]
