import pytest
from data.data_url import *
import allure
import requests
from helpers import *


class TestApiV1DeleteCourier:
    #Тестирование ручки удаление курьера
    @allure.title("Удаление курьера")
    def test_delete_exist_courier(self, fixture_delete_exist_courier):
        courier_id = fixture_delete_exist_courier

        with allure.step(f"Удаление курьера с ID: {courier_id}"):
            response = requests.delete(f'{api_register_courier}/{courier_id}')
            allure.attach(f"Response: {response.text}")

        with allure.step('Проверка кода ответа'):
            assert response.status_code == 200, f"Ошибка: ожидался статус 200, получен {response.status_code}"

        with allure.step('Проверка успешности удаления'):
            assert response.json().get('ok') is True, "Ошибка: не удалось удалить курьера"

    @allure.title("Удаление курьера с несуществующим ID")
    def test_delete_nonexistent_courier(self, fixture_delete_nonexistent_courier):
        courier_id = fixture_delete_nonexistent_courier

        with allure.step(f"Удаление курьера с несуществующим ID: {courier_id}"):
            response = requests.delete(f'{api_register_courier}/{courier_id}')
            allure.attach(f"Response: {response.text}")

        with allure.step('Проверка кода ответа для несуществующего курьера'):
            assert response.status_code == 404, f"Ошибка: ожидался статус 404, получен {response.status_code}"

        with allure.step('Проверка сообщения об ошибке'):
            assert response.json().get('message') == "Курьера с таким id нет.", "Ошибка: сообщение не совпадает"

    @allure.title("Удаление курьера с пустым ID")
    def test_delete_courier_without_id(self):
        with allure.step(f"Удаление курьера с пустым ID"):
            response = requests.delete(f'{api_register_courier}')
            allure.attach(f"Response: {response.text}")

        with allure.step('Проверка кода ответа для пустого ID'):
            assert response.status_code == 400, f"Ошибка: ожидался статус 400, получен {response.status_code}"

        with allure.step('Проверка сообщения об ошибке'):
            assert response.json().get(
                'message') == "Недостаточно данных для удаления курьера", "Ошибка: сообщение не совпадает"
