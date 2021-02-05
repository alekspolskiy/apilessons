import requests
import statistics
from itertools import count
from utils import predict_salary


def get_vacancies_sj(secret_key, language):
    url = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {
        'X-Api-App-Id': secret_key
    }
    vacancies = []
    catalogues_key = 48
    moscow_key = 4
    vacancies_per_page = 100
    params = {
        'catalogues': catalogues_key,
        'town': moscow_key,
        'keyword': language,
        'count': vacancies_per_page
    }
    more = True
    page = count()
    while more:
        params['page'] = next(page)
        page_response = requests.get(url, headers=headers, params=params)
        page_response.raise_for_status()
        for vacancy in page_response.json()['objects']:
            vacancies.append(vacancy)
        more = page_response.json()['more']
    return vacancies


def get_average_language_salary_sj(secret_key, languages):
    vacancy_data = dict()
    for language in languages:
        vacancy_info = predict_rub_salary_sj(secret_key, language)
        vacancy_data[language] = {
            'vacancies_found': vacancy_info['vacancies_found'],
            'vacancies_processed': vacancy_info['vacancies_processed'],
            'average_salary': vacancy_info['average_salary']
        }
    return vacancy_data


def predict_rub_salary_sj(secret_key, language):
    vacancies = get_vacancies_sj(secret_key, language)
    salaries = []
    for vacancy in vacancies:
        if vacancy['currency'] == 'rub' and (vacancy['payment_from'] or vacancy['payment_to']):
            salary = predict_salary(vacancy['payment_from'], vacancy['payment_to'])
            salaries.append(salary)
    return {
        'vacancies_found': len(vacancies),
        'vacancies_processed': len(salaries),
        'average_salary': int(statistics.mean(salaries))
    }
