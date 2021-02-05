
def predict_salary(salary_from, salary_to):
    if salary_from is None or salary_from == 0:
        return salary_to * 0.8
    if salary_to is None or salary_to == 0:
        return salary_from * 1.2
    return (salary_from + salary_to) / 2
