import pytest
import allure
import requests
from helpers import *
from data.data_url import *

class TestApiV1OrdersPost:
    # тестирование ручки Создание заказа, тестируем параметры Самоката
    def test_login_courier_login_password_return_id(self, fixture_order_cancel):
        case_data, title, context = fixture_order_cancel
        allure.dynamic.title(title)
        payload = case_data["request"]
        expected_response = case_data["response"]

        with allure.step('Создание заказа'):
            response = requests.post(api_order, json=payload)
            allure.attach(f"Response: {response.text}")
            data = response.json()
            context['track_code'] = data.get('track')
            track_code = data.get('track')


        with allure.step('Проверка статуса ответа'):
            assert response.status_code == expected_response[
                "status_code"], f"Ошибка: ожидается статус {expected_response['status_code']}, получен {response.status_code}"

        with allure.step('Проверка, что track найден в ответе'):
            assert 'track' in response.json(), "Ошибка: код трека не найден в ответе"

        with allure.step('Проверка, что track не пустой'):
            assert track_code is not None, "Ошибка: трек должен быть не None"
            allure.attach(f"track {track_code}", name="Номер трека", attachment_type=allure.attachment_type.TEXT)
