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
    params = {
        'text': f'программист {language}',
        'area': '1',
        'only_with_salary': 'true',
    }
    response = requests.get(url, params=params)
    response.raise_for_status()

    return [predict_rub_salary(item['id'], url) for item in response.json()['items'] if
            predict_rub_salary(item['id'], url) is not None]


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


def predict_rub_salary(vacancy_id, url):
    url += vacancy_id
    response = requests.get(url)
    response.raise_for_status()
    salary = response.json()['salary']
    if salary['currency'] != 'RUR':
        return None
    if salary['from'] is None:
        return salary['to'] * 0.8
    if salary['to'] is None:
        return salary['from'] * 1.2
    return (salary['from'] + salary['to']) / 2


def get_average_languages_salary(languages):
    for language in languages:
        print({
            language: {
                'vacancies_found': get_vacancies(language)[f'{language}'],
                'vacancies_processed': len(get_vacancies_salaries(language)),
                'average_salary': int(statistics.mean(get_vacancies_salaries(language)))
            }
        })


def main():
    languages = ['C#', 'CSS', 'C++', 'PHP', 'Ruby', 'Python', 'Java', 'JavaScript']
    url = 'https://api.hh.ru/vacancies/'
    # get_vacancies(url, languages)
    # get_python_salaries(url)
    # print(get_vacancies_salaries(languages[0]))
    get_average_languages_salary(languages)


if __name__ == '__main__':
    main()
