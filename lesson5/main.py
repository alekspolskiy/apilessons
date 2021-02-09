from __future__ import print_function

import os

from dotenv import load_dotenv
from terminaltables import AsciiTable
from hh import get_average_language_salary
from superjob import get_average_language_salary_sj


def get_table_data(languages, data, header):
    table_data = [header]
    for language in languages:
        table_data.append([language,
                           data[language]['vacancies_found'],
                           data[language]['vacancies_processed'],
                           data[language]['average_salary']]
                          )
    return table_data


def create_table(title, data):
    table_instance = AsciiTable(data, title)
    table_instance.justify_columns[2] = 'right'

    return table_instance.table


def main():
    languages = ['C#', 'CSS', 'C++', 'PHP', 'Ruby', 'Python', 'Java', 'JavaScript']
    header = ('Prog Language', 'Vacancies found', 'Vacancies processed', 'Average salary')
    load_dotenv('.env')
    secret_key = os.getenv('SUPERJOB_SECRET_KEY')
    data_hh = get_average_language_salary(languages)
    data_sj = get_average_language_salary_sj(secret_key, languages)
    table_hh = create_table(
        'hh Moscow',
        get_table_data(languages, data_hh, header)
    )
    table_sj = create_table(
        'SuperJob Moscow',
        get_table_data(languages, data_sj, header)
    )
    print(table_hh)
    print(table_sj)


if __name__ == '__main__':
    main()
