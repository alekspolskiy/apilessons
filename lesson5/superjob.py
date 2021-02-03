import requests


def get_vacancies(secret_key):
    url = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {
        'X-Api-App-Id': secret_key
    }
    params = {
        'catalogues': 48,
        'town': 4
    }

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    for vacancy in response.json()['objects']:
        print(vacancy['profession'])
