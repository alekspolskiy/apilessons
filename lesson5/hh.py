import requests
import statistics
from utils import predict_salary


def get_vacancies_hh(language):
    url = 'https://api.hh.ru/vacancies/'
    page = 0
    pages_number = 1

    vacancies = []
    params = {
        'text': f'программист {language}',
        'area': '1',
        'only_with_salary': 'true',
    }
    while page < pages_number:
        params['page'] = page
        page_response = requests.get(url, params=params)
        page_response.raise_for_status()
        pages_number = page_response.json()['pages']
        page += 1
        [vacancies.append(item) for item in page_response.json()['items']]

    return vacancies


def predict_rub_salary_hh(language):
    vacancies = get_vacancies_hh(language)
    salaries = []
    for vacancy in vacancies:
        if vacancy['salary']['currency'] == 'RUR':
            salary = predict_salary(vacancy['salary']['from'], vacancy['salary']['to'])
            salaries.append(salary)

    return {
        'vacancies_found': len(vacancies),
        'vacancies_processed': len(salaries),
        'average_salary': int(statistics.mean(salaries))
    }


def get_average_language_salary(languages):
    vacancy_data = dict()
    for language in languages:
        vacancy_info = predict_rub_salary_hh(language)
        vacancy_data[language] = {
                'vacancies_found': vacancy_info['vacancies_found'],
                'vacancies_processed': vacancy_info['vacancies_processed'],
                'average_salary': vacancy_info['average_salary']
        }
    return vacancy_data


def get_python_salaries(url):
    params = {
        'text': 'программист Python',
        'area': '1',
        'only_with_salary': 'true',
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    for item in response.json()['items']:
        print(item['salary'])
