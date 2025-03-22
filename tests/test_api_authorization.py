import pytest
import allure
import requests
from helpers import *
from data.data_authorization import *
from data.data_url import *


class TestApiV1CourierLoginPost:

    @pytest.mark.parametrize("test_case, details", test_cases_for_authorization_courier_valid.items())
    @allure.title("{test_case}")
    def test_login_courier_login_password_return_id(self, test_case, details):
        payload = details["request"]
        expected_response = details["response"]
        with allure.step('Проверка статуса ответа'):
            response = requests.post(api_register_courier + "/login", json=payload)
            allure.attach(f"Response: {response.text}")

        with allure.step('Проверка статуса ответа'):
            assert response.status_code == expected_response["status_code"], f"Ошибка: ожидается статус {expected_response['status_code']}, получен {response.status_code}"

        with allure.step('Проверка, что id найден в ответе'):
            assert 'id' in response.json(), "Ошибка: код курьера не найден в ответе"

        with allure.step('Проверка, что id код курьера не пустой'):
            data = response.json()
            courier_code = data['id']
            assert courier_code is not None, "Ошибка: код курьера должен быть не None"


    @pytest.mark.parametrize("test_case, details", test_cases_for_authorization_courier_invalid.items())
    @allure.title("{test_case}")
    def test_login_courier_login_password_return_id(self, test_case, details):
        payload = details["request"]
        expected_response = details["response"]
        with allure.step('Проверка статуса ответа'):
            response = requests.post(api_register_courier + "/login", json=payload)
            allure.attach(f"Response: {response.text}")

        with allure.step('Проверка статуса ответа'):
            assert response.status_code == expected_response["status_code"], f"Ошибка: ожидается статус {expected_response['status_code']}, получен {response.status_code}"

        with allure.step('Проверка сообщения в ответе'):
            assert response.json().get("message") == expected_response["message"], f"Ошибка: ожидается сообщение {expected_response['message']}, получен {response.message}"
