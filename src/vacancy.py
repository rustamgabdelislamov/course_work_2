class Vacancy:
    """Класс для работы с вакансиями"""
    __slots__ = ("_name", "link", "salary", "salary_from", "salary_to", "description")

    def __init__(self, name, link, salary, description):
        self.name = name
        self.link = link
        self.description = description
        self.__validate(salary)  # Вызов метода валидации

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Имя должно быть строкой.")
        self._name = value

    def __validate(self, salary):
        """Метод для валидации и установки значений зарплаты"""
        if salary:
            self.salary_from = salary["from"] if salary["from"] else 0  # Используем get для безопасного извлечения
            self.salary_to = salary.get("to", 0)
        else:
            self.salary_from = 0
            self.salary_to = 0

    def __eq__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return (self.name == other.name and
                self.link == other.link and
                self.salary_from == other.salary_from and self.salary_to == other.salary_to and
                self.description == other.description)

    def __lt__(self, other):
        """<"""
        return self.salary_from < other.salary_from

    def __repr__(self):
        return (f"Vacancy(Название: {self.name}, Ссылка: {self.link}, Зарплата: {self.salary_from} - {self.salary_to},"
                f"Описание: {self.description})")

    def __str__(self):
        return f"""Название: {self.name}{"\n"}Ссылка: {self.link}{"\n"}Зарплата: {self.salary_from} - {self.salary_to}
Описание: {self.description}{"\n"}"""
