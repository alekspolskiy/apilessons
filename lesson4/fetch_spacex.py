import requests
import os


def fetch_spacex(urls, images_folder):

    for url_number, url in enumerate(urls, start=1):
        response = requests.get(url)
        response.raise_for_status()
        with open(f'{images_folder}/spacex{url_number}.jpg', 'wb') as file:
            file.write(response.content)


def get_last_launch_links():
    url = 'https://api.spacexdata.com/v4/launches/latest'
    response = requests.get(url)
    response.raise_for_status()

    return response.json()['links']['flickr']['original']
