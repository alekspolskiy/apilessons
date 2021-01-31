import requests
import os


def fetch_spacex_last_launch(urls):
    if not os.path.exists('images'):
        os.makedirs('images')

    for url_number, url in enumerate(urls):
        response = requests.get(url)
        response.raise_for_status()
        with open(f'images/spacex{url_number + 1}.jpg', 'wb') as file:
            file.write(response.content)


def get_links():
    url = 'https://api.spacexdata.com/v4/launches/latest'
    response = requests.get(url)
    response.raise_for_status()

    return response.json()['links']['flickr']['original']
