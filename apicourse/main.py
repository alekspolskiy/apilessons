import requests


def main():
    cities = ['Лондон', 'Шереметьево', 'Череповец']
    url_template = 'http://wttr.in/{}'
    params = {
        "nTqm": "",
        "lang": "ru",
    }
    responses = []
    urls = [url_template.format(city) for city in cities]
    for url in urls:
        response = requests.get(url, params=params)
        response.raise_for_status()
        responses.append(response)

    return responses


if __name__ == '__main__':
    for resp in main():
        print(resp.text)
