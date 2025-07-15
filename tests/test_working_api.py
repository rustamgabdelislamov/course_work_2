from src.working_api import HH
from unittest.mock import patch
from requests import Response


@patch("requests.get")
def test_hh_connect(mock_get):
    """Тест ответа от сервера"""
    hh = HH()
    response = Response()
    response.status_code = 200
    mock_get.return_value = response
    mock_get.return_value.status_code = response.status_code
    assert hh._connect("test") == response
    mock_get.assert_called_once()


@patch("requests.get")
def test_get_vacancies(mock_get):
    """Тест возврата вакансии"""
    # Создаем экземпляр класса HH
    hh = HH()

    # Подготовка мока ответа
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "items": [
            {"id": "1", "name": "Python Developer"},
            {"id": "2", "name": "Senior Python Developer"}
        ]
    }

    # Ожидаемый результат
    expected_result = [
        {"id": "1", "name": "Python Developer"},
        {"id": "2", "name": "Senior Python Developer"}
    ]

    # Вызов метода get_vacancies
    result = hh.get_vacancies("python", 1)  # ставим 1 чтобы только первую страницу вызвать

    assert expected_result == result
