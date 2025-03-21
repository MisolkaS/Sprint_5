import pytest
import allure
import requests
from helpers import *
from data.data_couriers_login import *
from data.data_url import *


class TestApiV1CourierPost:
    # тестирование ручки Создание Курьера
    def test_register_new_courier(self, fixture_register_new_courier):
        case_data, title, r_code = fixture_register_new_courier
        allure.dynamic.title(title)
        payload = case_data["request"]
        expected_response = case_data["response"]

        with allure.step('Создание курьера'):
            response = requests.post(api_register_courier, json=payload)
            allure.attach(f"Response: {response.text}")
            r_code['response_code'] = response.status_code

        with allure.step('Проверка кода ответа'):
            assert response.status_code == expected_response[
            "status_code"], f"Ожидался статус {expected_response['status_code']}, но получен {response.status_code}"
            allure.attach(f"Ожидался статус {expected_response['status_code']}, получен {response.status_code}")

        with allure.step('Проверка текста сообщения'):
            assert response.json().get("message") == expected_response[
                     "message"], f"Ожидалось сообщение {expected_response['message']}, но получено {response.json().get('message')}"
            allure.attach(f"Ожидалось сообщение {expected_response['message']}, получено {response.json().get('message')}")



    @allure.title("Проверка появления ошибки при создании пользователя с логином, который уже есть")
    def test_register_new_courier_with_existing_login(self, fixture_register_new_courier_with_existing_login):
        login = fixture_register_new_courier_with_existing_login
        new_payload = {
            "login": login,
            "password": "77777",
            "firstName": "Другое Имя"
        }
        message = 'Этот логин уже используется'
        with allure.step('Проверка, что повторно курьер не создается'):
            response = requests.post(api_register_courier, json=new_payload)
            allure.attach(f"Response: {response.text}")

        with allure.step('Проверка кода ответа'):
            assert response.status_code == 409, f"Ожидался статус 409, но получен {response.status_code}"
            allure.attach(f"Ожидался статус 409, получен {response.status_code}")

        with allure.step('Проверка текста сообщения'):
            assert response.json().get("message") == message, f"Ожидалось сообщение {message}, но получено {response.json().get('message')}"
            allure.attach(f"Ожидалось сообщение {message}, получено {response.json().get('message')}")




