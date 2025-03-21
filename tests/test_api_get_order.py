import pytest
from data.data_url import *
import allure
import requests
from helpers import *

class TestApiV1AcceptOrderPut:

    @allure.title("Получение заказа по его номеру")
    def test_get_order_by_track_success(self, fixture_get_order_by_track_success):
        track_id = fixture_get_order_by_track_success

        with allure.step('Получение заказа по track_id'):
            response = requests.get(f"{api_order}/track?t={track_id}")
            allure.attach(f"Response: {response.text}")

        with allure.step('Проверка кода ответа'):
            assert response.status_code == 200, f"Ошибка: Не удалось получить заказ. Статус: {response.status_code}, тело ответа: {response.text}"
            message = f"Заказ {track_id} получен"
            allure.attach(message, name="Результат", attachment_type=allure.attachment_type.TEXT)


    @allure.title("Проверка получения ошибки при запросе заказа без номера")
    def test_get_order_without_id(self):

        with allure.step('Отправка заказа без track_id'):
            response = requests.put(f"{api_order}/track?t=")
            allure.attach(f"Response: {response.text}")

        with allure.step('Проверка кода ответа'):
            assert response.status_code == 400
            message = f"Получен код ответа  {response.status_code}"
            allure.attach(message, name="Результат", attachment_type=allure.attachment_type.TEXT)

        with allure.step('Проверка сообщения в  ответе'):
            assert response.json().get("message") == "Недостаточно данных для поиска"


    @allure.title("Проверка получения ошибки при запросе заказа c несуществующим номером")
    def test_get_order_with_invalid_id(self):

        with allure.step('Отправка заказа c неправильным track_id'):
            response = requests.put(f"{api_order}/track?t=123a")
            allure.attach(f"Response: {response.text}")

        with allure.step('Проверка кода ответа'):
            assert response.status_code == 404
            message = f"Получен код ответа  {response.status_code}"
            allure.attach(message, name="Результат", attachment_type=allure.attachment_type.TEXT)

        with allure.step('Проверка сообщения в  ответе'):
            assert response.json().get("message") == "Недостаточно данных для поиска"
