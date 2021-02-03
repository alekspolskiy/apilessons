import requests
from hh import predict_salary


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
    vacancies_ids = []
    for vacancy in response.json()['objects']:
        vacancies_ids.append(vacancy['id'])

    salary_info = []
    for id in vacancies_ids:
        salary_info.append(predict_rub_salary_sj(id))
    for i in salary_info:
        print(i)


def predict_rub_salary_sj(vacancy_id):
    url = f'https://api.superjob.ru/2.0/vacancies/{vacancy_id}'
    response = requests.get(url)
    response.raise_for_status()
    salary_info = response.json()
    return {
        'salary_currency': salary_info['currency'],
        'salary_from': salary_info['payment_from'],
        'salary_to': salary_info['payment_to']
    }
