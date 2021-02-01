import requests
import os


def fetch_spacex(urls, images_folder):
    if not os.path.exists(f'{images_folder}'):
        os.makedirs(f'{images_folder}')

    for url_number, url in enumerate(urls):
        response = requests.get(url)
        response.raise_for_status()
        with open(f'{images_folder}/spacex{url_number + 1}.jpg', 'wb') as file:
            file.write(response.content)


def get_last_launch_links():
    url = 'https://api.spacexdata.com/v4/launches/latest'
    response = requests.get(url)
    response.raise_for_status()

    return response.json()['links']['flickr']['original']
