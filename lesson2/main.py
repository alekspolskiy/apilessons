import requests
from dotenv import load_dotenv
import os

load_dotenv('.env')

TOKEN = os.getenv('TOKEN')
LINK = input("Enter link: ")


def shorten_link(token, link):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }
    url = 'https://api-ssl.bitly.com/v4/shorten'
    data = {
        'long_url': f'{link}'
    }

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()

    return response.json()['id']


def count_clicks(token, link):
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks/summary'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }
    params = {
        "units": "-1",
    }
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()

    return response.json()['total_clicks']


def main():
    pass


if __name__ == '__main__':
    main()
    if not LINK.startswith('bit'):
        try:
            bitlink = shorten_link(TOKEN, LINK)
        except requests.exceptions.HTTPError:
            raise Exception
        print(bitlink)
    else:
        try:
            clicks_count = count_clicks(TOKEN, LINK)
        except requests.exceptions.HTTPError:
            raise Exception
        print(clicks_count)
