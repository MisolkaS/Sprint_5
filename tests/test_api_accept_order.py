import pytest
from data.data_url import *
import allure
import requests
from helpers import *

class TestApiV1AcceptOrderPut:

    @allure.title("Проверка, что курьер может принять заказ")
    def test_accept_order_courierId_orderId_success(self, fixture_accept_order_courierId_orderId_success):
        order_id, courier_id = fixture_accept_order_courierId_orderId_success
        with allure.step('Прием заказа'):
            response = requests.put(f"{api_order}/accept/{order_id}?courierId={courier_id}")
            allure.attach(f"Response: {response.text}")

        with allure.step('Проверка кода ответа'):
            assert response.status_code == 200, f"Ошибка: Не удалось принять заказ {order_id}. Статус: {response.status_code}, тело ответа: {response.text}"
            message = f"Заказ {order_id} принят курьером {courier_id}."
            allure.attach(message, name="Результат", attachment_type=allure.attachment_type.TEXT)
        with allure.step('Проверка сообщения в  ответе'):
            assert response.json().get('ok') == True


    @allure.title("Проверка, появления ошибки при запросе без id курьера")
    def test_error_on_request_without_courier_id(self, fixture_error_on_request_without_courier_id):

        order_id = fixture_error_on_request_without_courier_id

        with allure.step('Прием заказа'):
            response = requests.put(f"{api_order}/accept/{order_id}?courierId=")
            allure.attach(f"Response: {response.text}")

        with allure.step('Проверка кода ответа'):
            assert response.status_code == 400

        with allure.step('Проверка сообщения в  ответе'):
            assert response.json().get("message") == "Недостаточно данных для поиска"


    @allure.title("Проверка, появления ошибки при запросе с неверным id курьера")
    def test_error_on_request_invalid_courier_id(self, fixture_error_on_request_invalid_courier_id):
        order_id, courier_id = fixture_error_on_request_invalid_courier_id

        with allure.step('Прием заказа'):
            response = requests.put(f"{api_order}/accept/{order_id}?courierId={courier_id}")
            allure.attach(f"Response: {response.text}")

        with allure.step('Проверка кода ответа'):
            assert response.status_code == 404

        with allure.step('Проверка сообщения в  ответе'):
            assert response.json().get("message") == "Курьера с таким id не существует"



    @allure.title("Проверка, появления ошибки при запросе с пустым id заказа")
    def test_error_on_request_with_empty_order_id(self, fixture_error_on_request_with_empty_order_id):
        courier_id = fixture_error_on_request_with_empty_order_id

        with allure.step('Прием заказа'):
            response = requests.put(f"{api_order}/accept/?courierId={courier_id}")
            allure.attach(f"Response: {response.text}")

        with allure.step('Проверка кода ответа'):
            assert response.status_code == 400

        with allure.step('Проверка сообщения в  ответе'):
            assert response.json().get("message") == "Недостаточно данных для поиска"



    @allure.title("Проверка, появления ошибки при запросе с несуществующим id заказа")
    def test_error_on_request_with_empty_order_id(self, fixture_error_on_request_with_empty_order_id):
        courier_id = fixture_error_on_request_with_empty_order_id

        with allure.step('Прием заказа'):
            response = requests.put(f"{api_order}/accept/1234a?courierId={courier_id}")
            allure.attach(f"Response: {response.text}")

        with allure.step('Проверка кода ответа'):
            assert response.status_code == 404

        with allure.step('Проверка сообщения в  ответе'):
            assert response.json().get("message") == "Заказа с таким id не существует"


