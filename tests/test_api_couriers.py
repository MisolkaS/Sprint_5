import pytest
import allure
import requests
from helpers import *
from data.data_couriers_login import *
from data.data_url import *


class TestApiV1CourierPost:

    @pytest.mark.parametrize("test_case, details", test_cases_for_register_new_courier.items())
    @allure.title("{test_case}")
    def test_register_new_courier(self, test_case, details):
        payload = details["request"]
        expected_response = details["response"]
        login = details["request"]["login"]
        password = details["request"]["password"]
        response = requests.post(api_register_courier, json=payload)

        assert response.status_code == expected_response["status_code"], f"Ожидался статус {expected_response['status_code']}, но получен {response.status_code}"

        if response.status_code == 201:
            with allure.step('Успешное создание нового курьера'):
                assert response.json().get("message") == expected_response["message"], f"Ожидалось сообщение {expected_response['message']}, но получено {response.json().get('message')}"

            with allure.step('Удаление созданного курьера'):
                courier_id = find_courier_by_login(login, password)
                delete_courier(courier_id)

        elif response.status_code != expected_response["status_code"]:
            with allure.step(f"Ошибка регистрации курьера"):
                allure.attach(f"Ожидался статус {expected_response['status_code']}, но получен {response.status_code}",
                              name="Ошибка", attachment_type=allure.attachment_type.TEXT)
                assert response.json().get("message") == expected_response["message"], f"Ожидалось сообщение {expected_response['message']}, но получено {response.json().get('message')}"



    first_case = list(test_cases_for_register_new_courier.values())[0]
    @pytest.mark.parametrize("details", [first_case])
    @allure.title("Проверка появления ошибки, если создать пользователя с логином, который уже есть")
    def test_register_new_courier_with_existing_login(self, details):
        payload = details["request"]
        expected_response = details["response"]
        login = payload["login"]
        original_password = payload["password"]
        message = "Этот логин уже используется"
        response = requests.post(api_register_courier, json=payload)
        if response.status_code == 201:
            with allure.step('Успешное создание курьера'):
                new_payload = {
                    "login": login,
                    "password": "77777",
                    "firstName": "Другое Имя"
                }
            with allure.step('Проверка, что повторно курьер не создается'):
                response = requests.post(api_register_courier, json=new_payload)
                assert response.status_code == 409, f"Ожидался статус 409, но получен {response.status_code}"
                allure.attach(f"Полученное сообщение: {response.json().get('message')}, должно быть {message}", name="!!!Ошибка сообщения")

            with allure.step('Удалим созданного курьера'):
                courier_id = find_courier_by_login(login, original_password)
                delete_courier(courier_id)


