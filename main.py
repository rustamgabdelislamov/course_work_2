from src.utils import determining_time_day, get_vacancies_by_salary
from src.working_api import HH
from src.working_file import JsonSaver
from src.utils import filter_vacancies

def user_interaction():
        print(f'{determining_time_day()}!!! Добро пожаловать в программу работы с вакансиями.')
        print('''Выберите необходимый пункт меню:
                          1. Вывести все вакансии.
                          2. Вывести отфильтрованные вакансии по имени или описанию.
                          3. Вывести отфильтрованные вакансии зарплате''')

        input_menu = int(input())
        if input_menu == 1:
                while True:
                        input_search = input('Введите поисковый запрос для запроса вакансий: ')
                        print()
                        hh = HH()
                        vacancies = hh.get_vacancies(input_search)
                        vacancies_ = JsonSaver()
                        vacancies_.write_vacancies(vacancies)
                        vacancies_list = vacancies_.read_vacancies()
                        break
                for vac in vacancies_list:
                        print(vac)
        elif input_menu == 2:
                while True:
                        input_search = input('Введите поисковый запрос для запроса вакансий: ')
                        filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
                        print()
                        hh = HH()
                        vacancies = hh.get_vacancies(input_search)
                        vacancies_ = JsonSaver()
                        vacancies_.write_vacancies(vacancies)
                        vacancies_list = vacancies_.read_vacancies()
                        filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
                        break
                for vac in filtered_vacancies:
                        print(vac)
        elif input_menu == 3:
                while True:
                        input_search = input('Введите поисковый запрос для запроса вакансий: ')
                        filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
                        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
                        salary_range = input("Введите диапазон зарплат: ")
                        print()
                        hh = HH()
                        vacancies = hh.get_vacancies(input_search)
                        vacancies_ = JsonSaver()
                        vacancies_.write_vacancies(vacancies)
                        vacancies_list = vacancies_.read_vacancies()
                        filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
                        ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range, top_n)
                        break
                for vac in ranged_vacancies:
                        print(vac)
        else:
                print("Некорректный пункт меню. Пожалуйста, выберите 1, 2 или 3.")


if __name__ == "__main__":
        user_interaction()
