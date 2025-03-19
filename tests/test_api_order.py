import pytest
import allure
import requests
from helpers import *
from data.data_order import *
from data.data_url import *


class TestApiV1OrdersPost:
    @pytest.mark.parametrize("test_case, details", test_cases_for_order.items())
    @allure.title("{test_case}")
    def test_login_courier_login_password_return_id(self, test_case, details):
        payload = details["request"]
        expected_response = details["response"]
        response = requests.post(api_order, json=payload)
        with allure.step('Проверка статуса ответа'):
            assert response.status_code == expected_response["status_code"], f"Ошибка: ожидается статус {expected_response['status_code']}, получен {response.status_code}"
        if response.status_code==201:
            with allure.step('Проверка, что track найден в ответе'):
                assert 'track' in response.json(), "Ошибка: код трека не найден в ответе"

            with allure.step('Проверка, что track не пустой'):
                data = response.json()
                track_code = data['track']
                assert track_code is not None, "Ошибка: трек должен быть не None"
                allure.attach(f"track {track_code}",  name="Номер трека", attachment_type=allure.attachment_type.TEXT)


            with allure.step('Удаление созданного заказа'):
                cancel_order(track_code)