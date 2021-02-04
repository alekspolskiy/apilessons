import requests
import statistics
from utils import predict_salary


def get_vacancies_hh(language):
    url = 'https://api.hh.ru/vacancies/'
    page = 0
    pages_number = 1

    vacancies = []
    vacancies_ids = []
    while page < pages_number:
        params = {
            'text': f'программист {language}',
            'area': '1',
            'only_with_salary': 'true',
            'page': page
        }
        page_response = requests.get(url, params=params)
        page_response.raise_for_status()
        pages_number = page_response.json()['pages']
        page += 1
        [vacancies.append(item) for item in page_response.json()['items']]
    [vacancies_ids.append(item['id']) for item in vacancies]
    return vacancies_ids


def get_vacancies_salaries_hh(language):
    vacancies_ids = get_vacancies_hh(language)
    language_salaries = []
    for vacancy_id in vacancies_ids:
        salary_info = predict_rub_salary_hh(vacancy_id)
        salary = predict_salary(salary_info['salary_currency'],
                                salary_info['salary_from'],
                                salary_info['salary_to']
                                )
        if salary is not None:
            language_salaries.append(salary)

    return {
        'vacancies_found': len(vacancies_ids),
        'vacancies_processed': len(language_salaries),
        'average_salary': int(statistics.mean(language_salaries))
    }


def predict_rub_salary_hh(vacancy_id):
    url = f'https://api.hh.ru/vacancies/{vacancy_id}'
    response = requests.get(url)
    response.raise_for_status()
    salary = response.json()['salary']
    return {
        'salary_currency': salary['currency'],
        'salary_from': salary['from'],
        'salary_to': salary['to']
    }


def get_average_language_salary(languages):
    vacancy_data = dict()
    for language in languages:
        vacancy_info = get_vacancies_salaries_hh(language)
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
