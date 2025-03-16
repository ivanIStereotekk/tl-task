import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tl_project.settings")
django.setup()
import random
import faker
from decimal import Decimal
from datetime import datetime, timedelta
from django.db import transaction
from employ_app.models import Employee, Department
from django.core.management import call_command

# Инициализация Faker для генерации фейковых данных
fake = faker.Faker()

# Данные для структуры компании
BRANCHES = [
    "Офис Компании (Washington)",
    "Офис Компании (Moscow)",
    "Офис Компании (London)",
    "Офис Компании (Bobruysk)",
    "Офис Компании (Tel-Aviv)"
]

DEPARTMENTS = [
    "Экономический отдел",
    "Отдел Кадров",
    "Отдел по подготовке персонала",
    "Бухгалтерия",
    "АйТи отдел"
]

TOTAL_EMPLOYEES = 50_000  # Общее количество сотрудников
# Departments


# Функция для генерации подразделений с иерархией
def create_departments():
    """Создаёт филиалы и подразделения, возвращает список всех департаментов."""
    all_departments = []

    for branch_name in BRANCHES:
        city = branch_name.split("(")[-1].strip(")")
        branch = Department.objects.create(name="Офис Компании", city=city, parent=None)
        all_departments.append(branch)

        for dep_name in DEPARTMENTS:
            department = Department.objects.create(name=dep_name, city=city, parent=branch)
            all_departments.append(department)

    return all_departments

# Функция для генерации сотрудников
def create_employee(departments):
    department = random.choice(departments)
    full_name = fake.name()
    position = fake.job()
    hire_date = fake.date_this_decade()
    salary = Decimal(random.randint(30000, 120000))
    return Employee(
        full_name=full_name,
        position=position,
        hire_date=hire_date,
        salary=salary,
        department=department
    )

# Основная функция для создания данных
def create_data():
    # Очистить существующие данные (для тестирования)
    Department.objects.all().delete()
    Employee.objects.all().delete()

    # Создание иерархии подразделений
    departments = create_departments()

    employees = []
    for _ in range(50000):
        employee = create_employee(departments)
        employees.append(employee)
        if len(employees) >= 1000:  # Записываем батчами по 1000
            with transaction.atomic():
                Employee.objects.bulk_create(employees)
            employees = []

    if employees:
        with transaction.atomic():
            Employee.objects.bulk_create(employees)

if __name__ == "__main__":
    create_data()