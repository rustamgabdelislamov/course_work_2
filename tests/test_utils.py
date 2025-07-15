from freezegun import freeze_time

from src.utils import determining_time_day, filter_vacancies
from src.vacancy import Vacancy


@freeze_time("15:50:00")
def test_determining_time_day_success():
    """Тест при правильном формате даты"""
    assert determining_time_day() == 'Добрый день'


@freeze_time("20:50:00")
def test_determining_time_day_success_():
    """Тест при правильном формате даты"""
    assert determining_time_day() == 'Добрый вечер'


def test_filter_vacancies():
    vacancy1 = Vacancy("QA Engineer", "https://hh.ru/vacancy/122023399", 0,
                       "Знание языков программирования для написания автоматизированных тестов.")
    vacancy2 = Vacancy("Стажёр — менеджер продукта", "https://hh.ru/vacancy/121950103", {
                        "from": 80000,
                        "to": 80000,
                        "currency": "RUR",
                        "gross": "true"
                    },
                       "Опыт работы с облачными платформами (AWS, Google, Yandex, VK, Sber")

    vacancy_list = [vacancy1, vacancy2]

    result = filter_vacancies(vacancy_list, ["Qa"])

    expected = [Vacancy("QA Engineer", "https://hh.ru/vacancy/122023399", 0,
                        "Знание языков программирования для написания автоматизированных тестов.")]

    assert result == expected
