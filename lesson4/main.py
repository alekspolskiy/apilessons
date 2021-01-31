import os
from PIL import Image
import argparse
import sys
from dotenv import load_dotenv

sys.path.append(os.path.join(sys.path[0], "../"))
from instabot import Bot
from fetch_spacex import fetch_spacex_last_launch, get_links
from fetch_hubble import get_hubble_image, get_image_from_collection


def load_photo(login, password):
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("-u", type=str, help="username")
    parser.add_argument("-p", type=str, help="password")
    parser.add_argument("-proxy", type=str, help="proxy")
    args = parser.parse_args()
    bot = Bot()
    bot.login(username=login, password=password,
              proxy=args.proxy)

    img_list = os.listdir('images')
    for img in img_list:
        bot.upload_photo(f"images/{img}")


def resize_images():
    img_list = os.listdir('images')
    for img in img_list:
        image = Image.open(f'images/{img}')
        if image.width >= image.height:
            if image.height > 1080:
                image.thumbnail((1080, 1080))
            else:
                image.thumbnail((1080, image.height))
        if image.width < image.height:
            if image.width > 1080:
                image.thumbnail((1080, 1080))
            else:
                image.thumbnail((image.width, 1080))
        if image.mode == 'RGBA':
            image = image.convert('RGB')
        image.save("images/{}.jpg".format(img.split('.')[0]), format="JPEG")

    for i in img_list:
        image = Image.open(f'images/{i}')
        if image.width > 1080 or image.height > 1080:
            os.remove(f"images/{i}")


def main():
    load_dotenv('.env')
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    fetch_spacex_last_launch(get_links())
    get_hubble_image(2)
    get_image_from_collection('spacecraft')
    resize_images()
    # load_photo(login, password)
    # os.remove('config')


if __name__ == '__main__':
    main()
