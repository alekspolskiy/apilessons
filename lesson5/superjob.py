import requests


def get_vacancies(secret_key):
    url = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {
        'X-Api-App-Id': secret_key
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    for vacancy in response.json()['objects']:
        print(vacancy['profession'])
