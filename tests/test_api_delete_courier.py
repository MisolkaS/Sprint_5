import pytest
from data.data_url import *
import allure
import requests
from helpers import *


class TestApiV1DeleteCourier:
    @allure.title("Удаление курьера")
    def test_delete_exist_courier(self):
        with allure.step('Создание курьера'):
            courier_id = register_new_courier()

        with allure.step(f"Удаление курьера с ID: {courier_id}"):
            response = requests.delete(f'{api_register_courier}/{courier_id}')

            assert response.status_code == 200
            assert response.json().get('ok') == True


    @allure.title("Удаление курьера c несуществующим ID")
    def test_delete_exist_courier(self):
        with allure.step('Создание курьера'):
            courier_id = register_new_courier()
        with allure.step('Удаление курьера'):
            delete_courier(courier_id)

        with allure.step(f"Удаление курьера с несуществующим ID: {courier_id}"):
            response = requests.delete(f'{api_register_courier}/{courier_id}')

            assert response.status_code == 404
            assert response.json().get('message') == "Курьера с таким id нет."

    @allure.title("Удаление курьера c пустым ID")
    def test_delete_courier_without_id(self):

        with allure.step(f"Удаление курьера с пустым ID"):
            response = requests.delete(f'{api_register_courier}')

            assert response.status_code == 400
            assert response.json().get('message') == "Недостаточно данных для удаления курьера"
