from __future__ import print_function

import os
from hh import get_average_language_salary
from superjob import get_average_language_salary_sj
from dotenv import load_dotenv
from terminaltables import AsciiTable


def print_tables(secret_key, languages):
    data_sj = get_average_language_salary_sj(secret_key, languages)
    data_hh = get_average_language_salary(languages)
    table_data_sj = [
        ('Prog Language', 'Vacancies found', 'Vacancies processed', 'Average salary'),
    ]
    table_data_hh = [
        ('Prog Language', 'Vacancies found', 'Vacancies processed', 'Average salary'),
    ]

    for language in languages:
        table_data_sj.append([language,
                              data_sj[language]['vacancies_found'],
                              data_sj[language]['vacancies_processed'],
                              data_sj[language]['average_salary']]
                             )
        table_data_hh.append([language,
                              data_hh[language]['vacancies_found'],
                              data_hh[language]['vacancies_processed'],
                              data_hh[language]['average_salary']]
                             )

    title = 'SuperJob Moscow'

    table_instance_sj = AsciiTable(table_data_sj, title)
    table_instance_sj.justify_columns[2] = 'right'
    table_instance_hh = AsciiTable(table_data_hh, title)
    table_instance_hh.justify_columns[2] = 'right'

    return [table_instance_hh.table, table_instance_sj.table]


def main():
    languages = ['C#', 'CSS', 'C++', 'PHP', 'Ruby', 'Python', 'Java', 'JavaScript']
    load_dotenv('.env')
    secret_key = os.getenv('SUPERJOB_SECRET_KEY')
    tables = print_tables(secret_key, ['C++'])
    # for table in tables:
    print(tables[1])


if __name__ == '__main__':
    main()
