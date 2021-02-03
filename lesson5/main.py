import os
from hh import get_average_languages_salary
from superjob import get_api
from dotenv import load_dotenv


def main():
    languages = ['C#', 'CSS', 'C++', 'PHP', 'Ruby', 'Python', 'Java', 'JavaScript']
    load_dotenv('.env')
    secret_key = os.getenv('SUPERJOB_SECRET_KEY')
    # get_average_languages_salary(languages)
    get_api(secret_key)


if __name__ == '__main__':
    main()
