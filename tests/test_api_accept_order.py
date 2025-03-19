import pytest
from data.data_url import *
import allure
import requests
from helpers import *

class TestApiV1AcceptOrderPut:

    @allure.title("Проверка, что курьер может принять заказ")
    def test_accept_order_courierId_orderId_success(self):

        with allure.step('Создание курьера'):
            courier_id = register_new_courier()
        with allure.step('Создание заказа'):
            track_id = create_order()
        with allure.step('Получение Id заказа'):
            order_id = get_order_id_by_track(track_id)

        response = requests.put(f"{api_order}/accept/{order_id}?courierId={courier_id}")

        with allure.step('Проверка кода ответа'):
            assert response.status_code == 200, f"Ошибка: Не удалось принять заказ {order_id}. Статус: {response.status_code}, тело ответа: {response.text}"
            message = f"Заказ {order_id} принят {courier_id}."
            allure.attach(message, name="Результат", attachment_type=allure.attachment_type.TEXT)
        with allure.step('Проверка сообщения в  ответе'):
            assert response.json().get('ok') == True
        with allure.step('Завершение заказа'):
            finish_order(order_id)
        with allure.step('Удаление курьера'):
            delete_courier(courier_id)

    @allure.title("Проверка, появления ошибки при запросе без id курьера")
    def test_error_on_request_without_courier_id(self):

        with allure.step('Создание заказа'):
            track_id = create_order()
        with allure.step('Получение Id заказа'):
            order_id = get_order_id_by_track(track_id)

        response = requests.put(f"{api_order}/accept/{order_id}?courierId=")

        with allure.step('Проверка кода ответа'):
            assert response.status_code == 400
            message = f"Заказ {order_id} не принят без Id курьера."
            allure.attach(message, name="Результат", attachment_type=allure.attachment_type.TEXT)
        with allure.step('Проверка сообщения в  ответе'):
            assert response.json().get("message") == "Недостаточно данных для поиска"
        with allure.step('Отмена заказа'):
            cancel_order(track_id)

    @allure.title("Проверка, появления ошибки при запросе с неверным id курьера")
    def test_error_on_request_invalid_courier_id(self):
        with allure.step('Создание заказа'):
            track_id = create_order()
        with allure.step('Получение Id заказа'):
            order_id = get_order_id_by_track(track_id)
        with allure.step('Создание курьера'):
            courier_id = register_new_courier()
        with allure.step('Удаление курьера'):
            delete_courier(courier_id)

        response = requests.put(f"{api_order}/accept/{order_id}?courierId={courier_id}")

        with allure.step('Проверка кода ответа'):
            assert response.status_code == 404
            message = f"Заказ {order_id} не принят без Id."
            allure.attach(message, name="Результат", attachment_type=allure.attachment_type.TEXT)
        with allure.step('Проверка сообщения в  ответе'):
            assert response.json().get("message") == "Курьера с таким id не существует"

        with allure.step('Отмена заказа'):
            cancel_order(track_id)

    @allure.title("Проверка, появления ошибки при запросе с пустым id заказа")
    def test_error_on_request_with_empty_order_id(self):

        with allure.step('Создание курьера'):
            courier_id = register_new_courier()

        response = requests.put(f"{api_order}/accept/?courierId={courier_id}")

        with allure.step('Проверка кода ответа'):
            assert response.status_code == 400
            message = f"Заказ {order_id} не принят без Id заказа."
            allure.attach(message, name="Результат", attachment_type=allure.attachment_type.TEXT)
        with allure.step('Проверка сообщения в  ответе'):
            assert response.json().get("message") == "Недостаточно данных для поиска"

        with allure.step('Удаление курьера'):
            delete_courier(courier_id)

    @allure.title("Проверка, появления ошибки при запросе с несуществующим id заказа")
    def test_error_on_request_with_empty_order_id(self):
        with allure.step('Создание курьера'):
            courier_id = register_new_courier()

        response = requests.put(f"{api_order}/accept/1234a?courierId={courier_id}")

        with allure.step('Проверка кода ответа'):
            assert response.status_code == 404
            message = f"Заказ {order_id} не принят c несуществующим Id заказа."
            allure.attach(message, name="Результат", attachment_type=allure.attachment_type.TEXT)
        with allure.step('Проверка сообщения в  ответе'):
            assert response.json().get("message") == "Заказа с таким id не существует"

        with allure.step('Удаление курьера'):
            delete_courier(courier_id)
