from src.working_file import JsonSaver
import os
import json
from unittest.mock import patch, mock_open


def test_write_vacancies():
    test_file = 'test_vacancies.json'
    saver = JsonSaver(test_file)

    vacancies = [
        {
            "name": "Python Developer",
            "alternate_url": "http://job1.com",
            "salary": "100000",
            "snippet": {"requirement": "Experience in Python"}
        },
        {
            "name": "Java Developer",
            "alternate_url": "http://job2.com",
            "salary": "90000",
            "snippet": {"requirement": "Experience in Java"}
        }
    ]

    # Удаляем файл если он существует (чистим среду)
    if os.path.exists(test_file):
        os.remove(test_file)

    # Записываем вакансии впервые
    saver.write_vacancies(vacancies)
    with open(test_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    assert len(data) == 2, "Должно быть 2 вакансии после первой записи"

    # Пытаемся снова записать те же вакансии — дубликатов быть не должно
    saver.write_vacancies(vacancies)
    with open(test_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    assert len(data) == 2, "Дублировать вакансии нельзя"

    # Добавляем новую вакансию
    new_vacancy = {
        "name": "Go Developer",
        "alternate_url": "http://job3.com",
        "salary": "110000",
        "snippet": {"requirement": "Experience in Go"}
    }
    saver.write_vacancies(vacancies + [new_vacancy])
    with open(test_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    assert len(data) == 3, "После добавления новой вакансии должно быть 3 записи"

    saver.delete_vacancies("Go Developer")
    with open(test_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    assert len(data) == 2, "После добавления новой вакансии должно быть 2 записи"
    os.remove(test_file)


def test_read_vacancies():
    """Тест для корректного чтения вакансий с существующим файлом вакансий"""

    saver = JsonSaver()
    mock_data = json.dumps([
        {
            "name": "Разработчик Python",
            "link": "https://example.com/vacancy1",
            "salary": {"from": 1000, "to": 1500},
            "description": "Требуется опыт работы с Python."
        },
        {
            "name": "Frontend Developer",
            "link": "https://example.com/vacancy2",
            "salary": {"from": 800, "to": 1200},
            "description": "Ищем специалиста по JavaScript."
        }
    ]) # json.dumps() используется для сериализации Python-объекта (в данном случае списка словарей) в строку JSON.

    with patch('builtins.open', mock_open(read_data=mock_data)):
        vacancies = saver.read_vacancies()

        assert len(vacancies) == 2
        assert vacancies[0].name == "Разработчик Python"
        assert vacancies[0].link == "https://example.com/vacancy1"
        assert vacancies[0].salary['from'] == 1000
        assert vacancies[0].salary['to'] == 1500
        assert vacancies[0].description == "Требуется опыт работы с Python."

        assert vacancies[1].name == "Frontend Developer"
        assert vacancies[1].link == "https://example.com/vacancy2"
        assert vacancies[1].salary['from'] == 800
        assert vacancies[1].salary['to'] == 1200
        assert vacancies[1].description == "Ищем специалиста по JavaScript."







