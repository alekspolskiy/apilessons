import requests


def get_vacancies():
    languages = ['C#', 'CSS', 'C++', 'PHP', 'Ruby', 'Python', 'Java', 'JavaScript']
    url = 'https://api.hh.ru/vacancies/'
    for language in languages:
        params = {
            'text': f'программист {language}',
            'area': '1',

        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        result_found = response.json()['found']
        print(
            {
                language: result_found
            }
        )


def main():
    get_vacancies()


if __name__ == '__main__':
    main()
