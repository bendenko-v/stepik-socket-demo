from PIL import Image, ImageDraw, ImageFont
from PIL.Image import Resampling

from src.config import FONT_PATH, PICTURE_PATH


def resize_picture(pic, new_height):
    original_width, original_height = pic.size
    aspect_ratio = original_width / original_height
    new_width = int(new_height * aspect_ratio)
    return pic.resize((new_width, new_height), resample=Resampling.LANCZOS)


def get_centered_x(draw, text, font, img_width):
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    return (img_width - text_width) / 2


def generate_image(name, score):
    img = Image.new("RGB", (900, 600), color="white")
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype(FONT_PATH, 48)
    font_score = ImageFont.truetype(FONT_PATH, 80)

    text_name = f"Привет, {name}"
    text_result = "Твой результат:"
    text_score = f"{score} / 10"

    img_width, img_height = img.size

    name_x = get_centered_x(draw, text_name, font, img_width * 0.5)
    result_x = get_centered_x(draw, text_result, font, img_width * 0.5)
    score_x = get_centered_x(draw, text_score, font_score, img_width * 0.5)

    draw.text((name_x if name_x > 0 else 0, 130), text_name, font=font, fill="#37B8A9")
    draw.text((result_x if result_x > 0 else 0, 230), text_result, font=font, fill=(0, 0, 0))
    draw.text((score_x if score_x > 0 else 0, 300), text_score, font=font_score, fill="#37B8A9")

    picture = Image.open(PICTURE_PATH).convert("RGBA")
    picture_resized = resize_picture(picture, 360)
    img.paste(picture_resized, (round(img_width / 2 + 60), 120), picture_resized)

    return img
