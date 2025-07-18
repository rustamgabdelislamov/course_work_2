from src.abstract import AbstractApi
import requests


class HH(AbstractApi):
    """Класс для работы с API HeadHunter"""

    def __init__(self, page=0):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__params = {'page': page, 'per_page': 30}

    def _connect(self, text):
        self.__params["text"] = text
        response = requests.get(self.__url, params=self.__params)
        response.raise_for_status()
        return response

    def get_vacancies(self, text, page=2):
        all_vacancies = []
        while self.__params["page"] < page:
            vacancies = self._connect(text).json()["items"]
            all_vacancies.extend(vacancies)
            self.__params["page"] += 1
        return all_vacancies
