import requests
import statistics
from utils import predict_salary


def get_vacancies_hh(language, vacancies_ids_check: bool):
    url = 'https://api.hh.ru/vacancies/'
    page = 0
    pages_number = 1

    vacancies = []
    vacancies_ids = []
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
        if not vacancies_ids_check:
            [vacancies.append(item) for item in page_response.json()['items']]
        else:
            [vacancies_ids.append(item['id']) for item in page_response.json()['items']]

    if vacancies_ids_check:
        return vacancies_ids
    return vacancies


def get_vacancies_salaries_hh(language):
    vacancies_ids = get_vacancies_hh(language, vacancies_ids_check=True)
    print(vacancies_ids)
    language_salaries = []
    for vacancy_id in vacancies_ids:
        salary_info = predict_rub_salary_hh(language, vacancy_id)
        if salary_info['salary_currency'] == 'RUR':
            salary = predict_salary(
                                    salary_info['salary_from'],
                                    salary_info['salary_to']
                                    )
            language_salaries.append(salary)

    return {
        'vacancies_found': len(vacancies_ids),
        'vacancies_processed': len(language_salaries),
        'average_salary': int(statistics.mean(language_salaries))
    }


def predict_rub_salary_hh(language, vacancy_id):
    vacancies = get_vacancies_hh(language, vacancies_ids_check=False)
    for vacancy in vacancies:
        if vacancy['id'] == vacancy_id:
            return {
                'salary_currency': vacancy['salary']['currency'],
                'salary_from': vacancy['salary']['from'],
                'salary_to': vacancy['salary']['to']
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
