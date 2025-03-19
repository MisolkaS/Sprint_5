import pytest
import allure
import requests
from helpers import *
from data.data_list_orders import *
from data.data_url import *


class TestApiV1ListOrdersGet:

    @staticmethod
    def check_keys(data, expected):
        return all(key in data for key in expected)

    @allure.title("Проверка структуры ответа при получения списка заказов")
    def test_register_new_courier(self):
        with allure.step('Создание курьера'):
            courier_id = register_new_courier()
        with allure.step('Создание заказа'):
            track_id = create_order()
        with allure.step('Получение Id заказа'):
            order_id = get_order_id_by_track(track_id)
        with allure.step('Курьер принял заказ'):
            accept_order(order_id, courier_id)

        response = requests.get(f"{api_order}?courierId={courier_id}")
        response_data = response.json()

        with allure.step('Проверка статуса ответа'):
            assert response.status_code == 200, f"Ошибка: ожидается статус 200, получен {response.status_code}"
            if response.status_code == 200:
                with allure.step('Проверка, что структура ответа правильная'):
                    assert self.check_keys(response_data,
                                           expected_keys.keys()), "Некорректная структура: отсутствуют ключи на верхнем уровне"

                    # Проверка наличия ключей в orders
                    assert all(self.check_keys(order, expected_keys['orders']) for order in
                               response_data['orders']), "Некорректная структура: отсутствуют ключи в orders"

                    # Проверка наличия ключей в pageInfo
                    assert self.check_keys(response_data['pageInfo'], expected_keys[
                        'pageInfo']), "Некорректная структура: отсутствуют ключи в pageInfo"

                    # Проверка наличия ключей в availableStations
                    assert all(self.check_keys(station, expected_keys['availableStations']) for station in
                               response_data[
                                   'availableStations']), "Некорректная структура: отсутствуют ключи в availableStations"

        with allure.step('Завершение заказа'):
            finish_order(order_id)
        with allure.step('Удаление курьера'):
            delete_courier(courier_id)
