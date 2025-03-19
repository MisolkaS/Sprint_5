import random
import string
import requests
import allure
import json
from data.data_url import *
from data.data_list_orders import *

def create_order():
    with allure.step(f"Создание заказа"):
        payload = test_cases_for_list_order["request"]
        response = requests.post(api_order, json=payload)
        data = response.json()

        if response.status_code == 201:
            track_code = data['track']
            allure.attach(f"Создан заказ: {track_code}", name="Заказ",
                          attachment_type=allure.attachment_type.TEXT)
            return track_code
        else:
            allure.attach(f"Ошибка при создании заказа: статус {response.status_code}", name="Ошибка",
                          attachment_type=allure.attachment_type.TEXT)
            return None


def register_new_courier():
    login = generate_random_string(5)
    password = generate_random_string(5)
    payload = {
        "login": login,
        "password": password,
        "firstName": "Другое Имя"
    }
    response = requests.post(api_register_courier, json=payload)
    if response.status_code == 201:
        courier_id = find_courier_by_login(login, password)
        return courier_id
    else:
        allure.attach(f"Ошибка при создании курьера: статус {response.status_code}", name="Ошибка поиска",
                      attachment_type=allure.attachment_type.TEXT)
        return None

def find_courier_by_login(login, password):

    payload = {
        "login": login,
        "password": password
    }

    with allure.step(f"Поиск курьера с логином: {login}"):
        response = requests.post(api_register_courier+"/login", json=payload)

        if response.status_code == 200:
            data = response.json()
            if "id" in data:
                allure.attach(f"Курьер найден: ID = {data['id']}", name="Результат поиска",
                              attachment_type=allure.attachment_type.TEXT)
                return data["id"]
            else:
                allure.attach("Курьер не найден", name="Результат поиска", attachment_type=allure.attachment_type.TEXT)
                return None
        else:
            allure.attach(f"Ошибка при поиске курьера: статус {response.status_code}", name="Ошибка поиска",
                          attachment_type=allure.attachment_type.TEXT)
            return None


def delete_courier(courier_id):
    with allure.step(f"Удаление курьера с ID: {courier_id}"):
        response = requests.delete(f'{api_register_courier}/{courier_id}')

        if response.status_code == 200:
            allure.attach(f"Курьер с ID {courier_id} успешно удален", name="Результат удаления",
                          attachment_type=allure.attachment_type.TEXT)
            return True
        else:
            allure.attach(f"Ошибка при удалении курьера: статус {response.status_code}", name="Ошибка удаления",
                          attachment_type=allure.attachment_type.TEXT)
            return False

def cancel_order(track_id):
    with allure.step(f"Отмена заказа с track: {track_id}"):
        response = requests.put(api_order + f"/cancel?track={track_id}")
        print(f"Ответ сервера: {response.status_code}, тело: {response.text}")
        if response.status_code == 200:
            allure.attach(f"Заказ с track {track_id} успешно отменен", name="Результат отмены",
                          attachment_type=allure.attachment_type.TEXT)
            return True
        else:
            allure.attach(f"Ошибка при отмене заказа: статус {response.status_code}", name="Ошибка отмены",
                          attachment_type=allure.attachment_type.TEXT)

            return False


def finish_order(order_id):
    with allure.step(f"Завершение заказа с id: {order_id}"):
        response = requests.put(api_order + f"/finish/{order_id}")
        if response.status_code == 200:
            allure.attach(f"Заказ с track {order_id} успешно завершен", name="Результат",
                          attachment_type=allure.attachment_type.TEXT)
            return True
        else:
            allure.attach(f"Ошибка при завершении заказа: статус {response.status_code}", name="Ошибка",
                          attachment_type=allure.attachment_type.TEXT)
            return False

def accept_order(order_id, courier_id):
    response = requests.put(f"{api_order}/accept/{order_id}?courierId={courier_id}")
    if response.status_code == 200:
        message = f"Заказ {order_id} принят {courier_id}."
        allure.attach(message, name="Результат", attachment_type=allure.attachment_type.TEXT)
        return True
    else:
        error_message = f"{courier_id} Не удалось принять заказ {order_id}. Статус: {response.status_code}, тело ответа: {response.text}"
        allure.attach(error_message, name="Ошибка", attachment_type=allure.attachment_type.TEXT)
        return False

def get_order_id_by_track(track_id):
    response = requests.get(f"{api_order}/track?t={track_id}")
    if response.status_code == 200:
        data = json.loads(response.text)

        order_id = data['order']['id']

        if order_id is not None:
            message = f"Идентификатор заказа: {order_id}"
            allure.attach(message, name="Результат", attachment_type=allure.attachment_type.TEXT)
            return order_id
        else:
            error_message = "Идентификатор заказа отсутствует в ответе."
            allure.attach(error_message, name="Ошибка", attachment_type=allure.attachment_type.TEXT)
            return None
    else:
        error_message = f"Ошибка при получении заказа. Статус: {response.status_code}, тело ответа: {response.text}"
        allure.attach(error_message, name="Ошибка", attachment_type=allure.attachment_type.TEXT)
        return None

def generate_random_string(length, language='english'):
    if language == 'english':
        letters = string.ascii_lowercase
    elif language == 'russian':
        letters = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string
