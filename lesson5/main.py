import requests


def get_vacancies(url):
    languages = ['C#', 'CSS', 'C++', 'PHP', 'Ruby', 'Python', 'Java', 'JavaScript']
    for language in languages:
        params = {
            'text': f'программист {language}',
            'area': '1',
            'only_with_salary': 'true',
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        result_found = response.json()['found']
        print(
            {
                language: result_found
            }
        )


def get_python_vacancies(url):
    params = {
        'text': 'программист Python',
        'area': '1',
        'only_with_salary': 'true',
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    for item in response.json()['items']:
        print(predict_rub_salary(item['id'], url))


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
    return (salary['from']+salary['to'])/2


def main():
    url = 'https://api.hh.ru/vacancies/'
    # get_vacancies(url)
    get_python_salaries(url)
    get_python_vacancies(url)


if __name__ == '__main__':
    main()
