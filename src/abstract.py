from abc import ABC, abstractmethod


class AbstractApi(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def _connect(self, text):
        pass

    @abstractmethod
    def get_vacancies(self, text):
        pass


class AbstractFile(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def __init__(self, file_path):
        pass

    @abstractmethod
    def write_vacancies(self, data):
        pass

    @abstractmethod
    def read_vacancies(self):
        pass

    @abstractmethod
    def delete_vacancies(self, key):
        pass


