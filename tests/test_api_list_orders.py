import pytest
import allure
import requests
from helpers import *
from data.data_list_orders import *
from data.data_url import *

class TestApiV1ListOrdersGet:
#тестирование ручки Получение списка заказов, все заказы курьера
    @allure.title("Проверка структуры ответа при получении списка заказов")
    def test_check_answer_structure(self, fixture_check_answer_structure):
        courier_id = fixture_check_answer_structure

        with allure.step('Отправка запроса на получение списка заказов'):
            response = requests.get(f"{api_order}?courierId={courier_id}")
            allure.attach(f"Response: {response.text}")

        with allure.step('Проверка статуса ответа'):
            assert response.status_code == 200, f"Ошибка: ожидается статус 200, получен {response.status_code}"


        response_data = response.json()
        with allure.step('Проверка, что структура ответа правильная'):
            assert check_keys(response_data,
                                   expected_keys.keys()), "Некорректная структура: отсутствуют ключи на верхнем уровне"

            # Проверка наличия ключей в orders
            assert 'orders' in response_data, "Некорректная структура: отсутствует ключ 'orders'"
            assert all(check_keys(order, expected_keys['orders']) for order in
                       response_data['orders']), "Некорректная структура: отсутствуют ключи в orders"

            # Проверка наличия ключей в pageInfo
            assert 'pageInfo' in response_data, "Некорректная структура: отсутствует ключ 'pageInfo'"
            assert check_keys(response_data['pageInfo'],
                                   expected_keys['pageInfo']), "Некорректная структура: отсутствуют ключи в pageInfo"

            # Проверка наличия ключей в availableStations
            assert 'availableStations' in response_data, "Некорректная структура: отсутствует ключ 'availableStations'"
            assert all(check_keys(station, expected_keys['availableStations']) for station in response_data[
                'availableStations']), "Некорректная структура: отсутствуют ключи в availableStations"
