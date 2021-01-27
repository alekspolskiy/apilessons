import requests
from dotenv import load_dotenv
from urllib.parse import urlparse
import os
import sys


def shorten_link(token, link):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }
    url = 'https://api-ssl.bitly.com/v4/shorten'
    data = {
        'long_url': link
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


def check_bitlink(token, link):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{link}', headers=headers)

    return response.ok


def parse_link(link):
    if link.startswith('http'):
        return urlparse(link).netloc + urlparse(link).path

    return link


def main():
    load_dotenv('.env')
    token = os.getenv('BIT_API_TOKEN')
    link = input("Enter link: ")

    try:
        if check_bitlink(token, parse_link(link)):
            clicks_count = count_clicks(token, parse_link(link))
            print(clicks_count)
        else:
            bitlink = shorten_link(token, link)
            print(bitlink)
    except requests.exceptions.HTTPError:
        sys.stderr.write("Not correct link\n")
        sys.exit()


if __name__ == '__main__':
    main()
