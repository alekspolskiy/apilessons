import requests
import statistics


def get_vacancies(language):
    url = 'https://api.hh.ru/vacancies/'
    params = {
        'text': f'программист {language}',
        'area': '1',
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    result_found = response.json()['found']

    return {language: result_found}


def get_vacancies_salaries(language):
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
        print(page)
        [vacancies.append(item) for item in page_response.json()['items']]
    [vacancies_ids.append(item['id']) for item in vacancies]
    language_salaries = []
    for vacancy_id in vacancies_ids:
        salary_info = predict_rub_salary_hh(vacancy_id, url)
        salary = predict_salary(salary_info['salary_currency'],
                                salary_info['salary_from'],
                                salary_info['salary_to']
                                )
        if salary is not None:
            language_salaries.append(salary)

    return {
        'vacancies_processed': len(language_salaries),
        'average_salary': int(statistics.mean(language_salaries))
    }


def predict_salary(salary_currency, salary_from, salary_to):
    if salary_currency != 'RUR' and salary_currency != 'rub':
        return None
    if salary_from is None or salary_from == 0:
        return salary_to * 0.8
    if salary_to is None or salary_to == 0:
        return salary_from * 1.2
    return (salary_from + salary_to) / 2


def predict_rub_salary_hh(vacancy_id, url):
    url += vacancy_id
    response = requests.get(url)
    response.raise_for_status()
    salary = response.json()['salary']
    return {
        'salary_currency': salary['currency'],
        'salary_from': salary['from'],
        'salary_to': salary['to']
    }


def get_average_languages_salary(languages):
    for language in languages:
        vacancy_info = get_vacancies_salaries(language)
        print({
            language: {
                'vacancies_found': get_vacancies(language)[f'{language}'],
                'vacancies_processed': vacancy_info['vacancies_processed'],
                'average_salary': vacancy_info['average_salary']
            }
        })


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
