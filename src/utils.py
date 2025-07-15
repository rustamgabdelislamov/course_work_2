from datetime import datetime


def determining_time_day() -> str:
    """Функция выводит приветствие в зависимости от времени суток"""
    now = datetime.now()
    hour = now.hour
    if 6 <= hour < 12:
        return "Доброе утро"
    elif 12 <= hour < 18:
        return "Добрый день"
    elif 18 <= hour < 24:
        return "Добрый вечер"
    else:
        return "Доброй ночи"


def filter_vacancies(vacancies, filter_words):
    """Фильтрует вакансии по заданным ключевым словам в названии или описании.

    Args:
        vacancies (list): Список объектов Vacancy.
        filter_words (list): Список ключевых слов для фильтрации.

    Returns:
        list: Список отфильтрованных вакансий.
    """
    filtered_vacancies = []

    for vacancy in vacancies:
        # Проверяем название и описание на наличие ключевых слов
        if (any(word.lower() in vacancy.name.lower() for word in filter_words)
                or (vacancy.description and isinstance(vacancy.description, str) and
            any(word.lower() in vacancy.description.lower() for word in filter_words))):
            filtered_vacancies.append(vacancy)

    return filtered_vacancies


def parse_salary_range(salary_range_str):
    """Парсит строку диапазона зарплат в кортеж (min_salary, max_salary)."""
    try:
        salary_from, salary_to = salary_range_str.split('-')
        salary_from = int(salary_from.strip())
        salary_to = int(salary_to.strip())
        return salary_from, salary_to
    except ValueError:
        raise ValueError("Неверный формат диапазона зарплат. Ожидается 'min_salary-max_salary'.")


def get_vacancies_by_salary(vacancies_list, salary_range_str, top_n):
    """Фильтруем вакансии по диапазону зарплат."""
    salary_from, salary_to = parse_salary_range(salary_range_str)

    filtered_vacancies = [
        vacancy for vacancy in vacancies_list
        if vacancy.salary_from is not None and vacancy.salary_to is not None and vacancy.salary_from != 0
           and vacancy.salary_to != 0 and
           (vacancy.salary_from <= salary_to and vacancy.salary_to >= salary_from)
    ]
    sorted_vacancies = sorted(filtered_vacancies, key=lambda x: x. salary_from, reverse=True)[:top_n]
    return sorted_vacancies