import random
import os
from PIL import Image, ImageDraw, ImageFont

# Directories to save the images and text files
output_dir = 'output_spells'
os.makedirs(output_dir, exist_ok=True)

# Load the Elder Futhark font
font_path = 'RUNE.ttf'
font_size = 100
font = ImageFont.truetype(font_path, font_size)

ELEMENTS = {
    'a': 'Fire',  # ᚨ
    'b': 'Water',  # ᛒ
    'c': 'Earth',  # ᚲ
    'd': 'Air',  # ᛞ
    'e': 'Light',  # ᛖ
    'f': 'Darkness'  # ᚠ
}

SHAPES = {
    'g': 'Beam',  # ᚷ
    'h': 'Wave',  # ᚻ
    # 'i': 'Bolt',  # ᛁ
    'j': 'Explosion',  # ᛃ
    'l': 'Barrier',  # ᛚ
    'm': 'Cloud/Fog',  # ᛗ
    'n': 'Burst',  # ᚾ
    'o': 'Sphere'  # ᛟ
}

OFFSETS = {
    'p': 'Self',  # ᛈ
    'r': 'Touch',  # ᚱ
    's': 'Projectile',  # ᛋ
    't': 'Area',  # ᛏ
    'u': 'Summon',  # ᚢ
    # 'v': 'Chain',  # ᚹ
    'z': 'Trap',  # ᛉ
    'y': 'Homing',  # ᛇ
    # 'x': 'Delayed Activation',  # Þ
    'q': 'Wide Arc'  # ᛜ
}

# Combine all dictionaries
ALL_COMPONENTS = {**ELEMENTS, **SHAPES, **OFFSETS}
TEXT_SPACING = 100


# Function to generate spells
def generate_spells(num_letters):
    for _ in range(10):  # Generate 10 spells
        spell_components = [random.choice(list(ELEMENTS.keys()))]  # Ensure at least one element
        spell_components += random.sample(list(ALL_COMPONENTS.keys()), num_letters - 1)  # Add remaining components

        # Create an image with white background
        image = Image.new('RGB', (TEXT_SPACING * num_letters + 100, 200), color='white')
        draw = ImageDraw.Draw(image)

        # Draw each component on the image
        for i, component in enumerate(spell_components):
            bbox = draw.textbbox((0, 0), component, font=font)
            text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
            position = ((i * TEXT_SPACING) + (TEXT_SPACING - text_width) + 50 // 2, (200 - text_height) // 2)
            draw.text(position, component, font=font, fill='black')

        # Save the image
        image_path = os.path.join(output_dir, f"{''.join(spell_components)}.png")
        image.save(image_path)

        # Create the corresponding text file
        text_file_path = os.path.join(output_dir, f"{''.join(spell_components)}.txt")
        with open(text_file_path, 'w') as file:
            file.write(''.join(spell_components))

    print("Spells generated successfully.")


# Example usage
generate_spells(2)  # Generate spells with 5 letters
