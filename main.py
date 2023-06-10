import ctypes
import datetime
import time
from PIL import Image, ImageDraw, ImageFont


def create_countdown_image(image_path, months, days, minutes, seconds):
    image = Image.open(image_path)

    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("arial.ttf", 36)

    countdown_text = f"{months} months, {days} days, {minutes} minutes, {seconds} seconds"
    text_position = (580, 300)
    text_color = (255, 255, 255)

    draw.text(text_position, countdown_text, font=font, fill=text_color)

    image.save("Wallpaper_Changer\\images\\countdown_image.png")
    return "Wallpaper_Changer\\images\\countdown_image.png"


def change_wallpaper(image_path):
    try:
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(
            SPI_SETDESKWALLPAPER, 0, "C:\Projects\Wallpaper_Changer\images\countdown_image.png", 3)
    except Exception as e:
        print(f"Failed to change wallpaper: {e}")


def calculate_time_remaining(target_date):
    now = datetime.datetime.now()
    remaining_time = target_date - now

    months = remaining_time.days // 30
    days = remaining_time.days % 30
    minutes = remaining_time.seconds // 60
    seconds = remaining_time.seconds % 60

    return months, days, minutes, seconds


def main():
    while True:

        background_path = r"C:\Projects\Wallpaper_Changer\images\Base.png"
        target_date = datetime.datetime(2023, 8, 8)
        remaining_months, remaining_days, remaining_minutes, remaining_seconds = calculate_time_remaining(
            target_date)
        path = create_countdown_image(
            background_path, remaining_months, remaining_days, remaining_minutes, remaining_seconds)
        change_wallpaper(background_path)
        time.sleep(0.8)


main()
