import os
from PIL import Image
import argparse
import shutil
import sys
from dotenv import load_dotenv

from instabot import Bot
from fetch_spacex import fetch_spacex, get_last_launch_links
from fetch_hubble import get_hubble_image, get_images_from_collection

MAX_SIZE = 1080


def load_photos(login, password, images_folder):
    parser = argparse.ArgumentParser()
    parser.add_argument("-proxy", type=str, help="proxy")
    args = parser.parse_args()
    bot = Bot()
    bot.login(username=login, password=password,
              proxy=args.proxy)

    images = os.listdir(f'{images_folder}')
    for img in images:
        bot.upload_photo(f"{images_folder}/{img}")


def resize_images(images_folder):
    images = os.listdir(images_folder)
    for img in images:
        image = Image.open(f'{images_folder}/{img}')
        if image.width or image.height > MAX_SIZE:
            image.thumbnail((MAX_SIZE, MAX_SIZE))
        if image.mode == 'RGBA':
            image = image.convert('RGB')
        image.save("{}/{}.jpg".format(images_folder, os.path.splitext(img)[0]), format="JPEG")
        print(img)
    for i in images:
        image = Image.open(f'{images_folder}/{i}')
        if image.width > MAX_SIZE or image.height > MAX_SIZE:
            os.remove(f"{images_folder}/{i}")


def main():
    images_folder = 'images'
    load_dotenv('.env')
    login = os.getenv('INSTA_LOGIN')
    password = os.getenv('INSTA_PASSWORD')
    fetch_spacex(get_last_launch_links(), images_folder)
    get_hubble_image(2, images_folder)
    get_images_from_collection('spacecraft', images_folder)
    resize_images(images_folder)
    load_photos(login, password, images_folder)


if __name__ == '__main__':
    try:
        main()
    finally:
        shutil.rmtree('config')
        sys.exit()
