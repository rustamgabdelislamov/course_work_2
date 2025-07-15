import json
import os
from src.abstract import AbstractFile
from src.vacancy import Vacancy


class JsonSaver(AbstractFile):
    """Класс для работы с файлами в формате JSON"""

    def __init__(self, file_path='data/vacancies.json'):
        self.__file_path = file_path

    def write_vacancies(self, vacancies: list[dict]):
        """Сохраняет данные в JSON-файл проверяя нет ли дублирующих вакансий через ссылку на вакансию."""

        vacancies_filter = []

        for vacancy in vacancies:
            vacancies_filter.append({
                "name": vacancy["name"],
                "link": vacancy["alternate_url"],
                "salary": vacancy["salary"],
                "description": vacancy["snippet"]["requirement"]
            })

        # Проверяем, существуют ли уже вакансии в файле
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as x:
                existing_data = json.load(x)
                existing_links = {vacancy['link'] for vacancy in existing_data}  # Сохраняем ссылки существующих
                # вакансий
        except FileNotFoundError:
            existing_data = []
            existing_links = set()  # Если файл не найден, создаем пустое множество

        # Добавляем только новые вакансии
        for vacancy in vacancies_filter:
            if vacancy['link'] not in existing_links:
                existing_data.append(vacancy)

        # Записываем все данные (новые и существующие) обратно в файл
        with open(self.__file_path, 'w', encoding='utf-8') as x:
            json.dump(existing_data, x, ensure_ascii=False, indent=4)

    def read_vacancies(self):
        """Загружает данные из JSON-файла в виде вакансий с 4 атрибутами"""

        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                # Используем list comprehension для создания списка вакансий
                vacancies = [Vacancy(**vacancy) for vacancy in data]
                return vacancies

            except json.JSONDecodeError:
                print("Ошибка при декодировании JSON. Проверьте формат файла.")
                return []
            except Exception as e:
                print(f"Произошла ошибка: {e}")
                return []
        else:
            print(f"Файл {self.__file_path} не найден.")
            return []

    def delete_vacancies(self, new_item: str):
        """Удаляет элемент по имени из JSON-файла."""

        try:
            # Читаем файл с вакансиями
            with open(self.__file_path, 'r', encoding='utf-8') as x:
                data = json.load(x)

            if data:  # Проверяем, что данные не пустые
                # Используем list comprehension для фильтрации данных
                filtered_data = [item for item in data if item.get('name') != new_item]

                if len(filtered_data) < len(data):
                    # Если размер отфильтрованных данных меньше, значит, была удалена хотя бы одна вакансия
                    with open(self.__file_path, 'w', encoding='utf-8') as x:
                        json.dump(filtered_data, x, ensure_ascii=False, indent=4)
                    print(f"Элемент с именем '{new_item}' был удален.")
                else:
                    print(f"Элемент с именем '{new_item}' не найден.")
            else:
                print("Файл пуст или не содержит данных.")

        except FileNotFoundError:
            print("Файл не найден. Проверьте путь к файлу.")
        except json.JSONDecodeError:
            print("Ошибка при чтении JSON. Убедитесь, что файл имеет правильный формат.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")
