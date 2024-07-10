from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime

if __name__ == '__main__':
    print(f'это главный файл модуль {__name__}')
    print(f'Сегодня {datetime.now():%d.%m.%Y}')
    calculate_salary()
    get_employees()