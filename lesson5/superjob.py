import requests
import statistics
from utils import predict_salary


def get_vacancies_sj(secret_key, language, vacancies_ids_check: bool):
    url = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {
        'X-Api-App-Id': secret_key
    }
    vacancies_ids = []
    vacancies = []
    page = 0
    pages_number = 5
    catalogues_key = 48
    moscow_key = 4
    vacancies_per_page = 100
    params = {
        'catalogues': catalogues_key,
        'town': moscow_key,
        'keyword': language,
        'count': vacancies_per_page
    }
    while page < pages_number:
        params['page'] = page
        page_response = requests.get(url, headers=headers, params=params)
        page_response.raise_for_status()
        page += 1
        for vacancy in page_response.json()['objects']:
            if vacancies_ids_check:
                vacancies_ids.append(vacancy['id'])
            else:
                vacancies.append(vacancy)
    if vacancies_ids_check:
        return vacancies_ids
    return vacancies


def get_vacancies_salaries_sj(secret_key, language):
    vacancies_ids = get_vacancies_sj(secret_key, language, vacancies_ids_check=True)
    salaries_info = []
    for vacancy_id in vacancies_ids:
        salaries_info.append(predict_rub_salary_sj(secret_key, language, vacancy_id))
    language_salaries = []
    for salary_info in salaries_info:
        if salary_info['salary_currency'] == 'rub':
            salary = predict_salary(salary_info['salary_from'], salary_info['salary_to'])
            if salary != 0:
                language_salaries.append(salary)

    return {
        'vacancies_found': len(vacancies_ids),
        'vacancies_processed': len(language_salaries),
        'average_salary': int(statistics.mean(language_salaries))
    }


def get_average_language_salary_sj(secret_key, languages):
    vacancy_data = dict()
    for language in languages:
        vacancy_info = get_vacancies_salaries_sj(secret_key, language)
        vacancy_data[language] = {
            'vacancies_found': vacancy_info['vacancies_found'],
            'vacancies_processed': vacancy_info['vacancies_processed'],
            'average_salary': vacancy_info['average_salary']
        }
    return vacancy_data


def predict_rub_salary_sj(secret_key, language, vacancy_id):
    vacancies = get_vacancies_sj(secret_key, language, vacancies_ids_check=False)
    for vacancy in vacancies:
        if vacancy['id'] == vacancy_id:

            return {
                'salary_currency': vacancy['currency'],
                'salary_from': vacancy['payment_from'],
                'salary_to': vacancy['payment_to']
            }
