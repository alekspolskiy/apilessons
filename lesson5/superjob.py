import requests
import statistics
from hh import predict_salary


def get_vacancy_salary_sj(secret_key, language):
    url = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {
        'X-Api-App-Id': secret_key
    }
    vacancies_ids = []
    page = 0
    pages_number = 5
    while page < pages_number:
        params = {
            'catalogues': 48,
            'town': 4,
            'keyword': language,
            'page': page,
            'count': 100
        }
        page_response = requests.get(url, headers=headers, params=params)
        page_response.raise_for_status()
        page += 1
        for vacancy in page_response.json()['objects']:
            vacancies_ids.append(vacancy['id'])

    salaries_info = []
    for id in vacancies_ids:
        salaries_info.append(predict_rub_salary_sj(id))
    language_salaries = []
    for salaries in salaries_info:
        salary = predict_salary(salaries['salary_currency'], salaries['salary_from'], salaries['salary_to'])
        if salary != 0:
            language_salaries.append(salary)

    return {
        'vacancies_found': len(vacancies_ids),
        'vacancies_processed': len(language_salaries),
        'average_salary': int(statistics.mean(language_salaries))
    }


def get_average_language_salary_sj(secret_key, languages):
    vacanct_data = dict()
    for language in languages:
        vacancy_info = get_vacancy_salary_sj(secret_key, language)
        vacanct_data[language]= {
                'vacancies_found': vacancy_info['vacancies_found'],
                'vacancies_processed': vacancy_info['vacancies_processed'],
                'average_salary': vacancy_info['average_salary']
        }
    return vacanct_data


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
