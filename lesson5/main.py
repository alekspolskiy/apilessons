from __future__ import print_function

import os
from hh import get_average_language_salary
from superjob import get_average_language_salary_sj
from dotenv import load_dotenv
from terminaltables import AsciiTable


def print_table_sj(secret_key, languages):
    data_sj = get_average_language_salary_sj(secret_key, languages)
    TABLE_DATA = [
        ('Prog Language', 'Vacancies found', 'Vacancies processed', 'Average salary'),
    ]
    for language in languages:
        TABLE_DATA.append([language,
                           data_sj[language]['vacancies_found'],
                           data_sj[language]['vacancies_processed'],
                           data_sj[language]['average_salary']]
                          )

    """Main function."""
    title = 'SuperJob Moscow'

    # AsciiTable.
    table_instance = AsciiTable(TABLE_DATA, title)
    table_instance.justify_columns[2] = 'right'
    print(table_instance.table)
    print()


def print_table_hh(languages):
    data_sj = get_average_language_salary(languages)
    TABLE_DATA = [
        ('Prog Language', 'Vacancies found', 'Vacancies processed', 'Average salary'),
    ]
    for language in languages:
        TABLE_DATA.append([language,
                           data_sj[language]['vacancies_found'],
                           data_sj[language]['vacancies_processed'],
                           data_sj[language]['average_salary']]
                          )

    """Main function."""
    title = 'SuperJob Moscow'

    # AsciiTable.
    table_instance = AsciiTable(TABLE_DATA, title)
    table_instance.justify_columns[2] = 'right'
    print(table_instance.table)
    print()


def main():
    languages = ['C#', 'CSS', 'C++', 'PHP', 'Ruby', 'Python', 'Java', 'JavaScript']
    load_dotenv('.env')
    secret_key = os.getenv('SUPERJOB_SECRET_KEY')
    # print_table_sj(secret_key, languages)
    print_table_hh(languages)


if __name__ == '__main__':
    main()
