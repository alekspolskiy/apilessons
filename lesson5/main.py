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


def main():
    url = 'https://api.hh.ru/vacancies/'
    # get_vacancies(url)
    get_python_salaries(url)


if __name__ == '__main__':
    main()
