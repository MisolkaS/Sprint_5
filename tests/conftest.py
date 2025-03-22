import pytest
import allure
import requests
from helpers import *
from data.data_couriers_login import *
from data.data_duplicate_courier import *
from data.data_order import *

@pytest.fixture
def fixture_delete_exist_courier():
    with allure.step('Создание курьера'):
        courier_id = register_new_courier()

    yield courier_id




@pytest.fixture
def fixture_delete_nonexistent_courier():
    with allure.step('Создание курьера'):
        courier_id = register_new_courier()
    with allure.step('Удаление курьера'):
        delete_courier(courier_id)

    yield courier_id

@pytest.fixture
def fixture_check_answer_structure():
    with allure.step('Создание курьера'):
        courier_id = register_new_courier()
    with allure.step('Создание заказа'):
        track_id = create_order()
    with allure.step('Получение Id заказа'):
        order_id = get_order_id_by_track(track_id)
    with allure.step('Курьер принимает заказ'):
        accept_order(order_id, courier_id)

    yield courier_id

    with allure.step('Завершение заказа'):
        finish_order(order_id)
    with allure.step('Удаление курьера'):
        delete_courier(courier_id)


@pytest.fixture(params=test_cases_for_order.items())
def fixture_order_cancel(request):
    title, case_data = request.param
    context = {'track_code': None}

    yield case_data, title, context

    if context["track_code"]:
        with allure.step(f'Удаление созданного заказа {context["track_code"]}'):
            cancel_order(context["track_code"])


@pytest.fixture
def fixture_register_and_delete_courier(request):
    #Фикстура для создания и удаления курьера после теста.
    payload = request.param
    login = payload["login"]
    password = payload["password"]

    with allure.step(f'Создание курьера {login} и {password}'):
        create_new_courier_with_login_password(login, password)

    yield payload

    courier_id = find_courier_by_login(payload["login"], payload["password"])
    if courier_id:
        with allure.step('Удаление созданного курьера'):
            delete_courier(courier_id)

@pytest.fixture
def fixture_get_order_by_track_success():
    #Фикстура для создания и удаления заказа по track_id
    track_id = create_order()
    yield track_id
    with allure.step('Отмена заказа'):
        cancel_order(track_id)

@pytest.fixture(params=test_cases_for_register_new_courier.items())
def fixture_register_new_courier(request):
    # Фикстура для удаления курьера после теста.
    title, case_data = request.param
    r_code = {'response_code': None}
    yield case_data, title, r_code

    login = case_data["request"]["login"]
    password = case_data["request"]["password"]

    if r_code['response_code'] == 201:
        with allure.step(f'Удаление созданного курьера {login} и {password}'):
            courier_id = find_courier_by_login(login, password)
            delete_courier(courier_id)

@pytest.fixture(params=test_cases_for_register_duplicate_courier)
def fixture_register_new_courier_with_existing_login(request):
    # Фикстура для удаления курьера после теста на поиск дубликата.
    details = request.param
    login = details["login"]
    password = details["password"]
    with allure.step(f'Создание курьера {login} и {password}'):
        create_new_courier_with_login_password(login, password)

    yield login

    with allure.step(f'Удаление созданного курьера {login} и {password}'):
        courier_id = find_courier_by_login(login, password)
        delete_courier(courier_id)

@pytest.fixture
def fixture_accept_order_courierId_orderId_success():
    with allure.step('Создание курьера'):
        courier_id = register_new_courier()
    with allure.step('Создание заказа'):
        track_id = create_order()
    with allure.step('Получение Id заказа'):
        order_id = get_order_id_by_track(track_id)

    yield order_id, courier_id

    with allure.step('Завершение заказа'):
        finish_order(order_id)

    with allure.step('Удаление курьера'):
        delete_courier(courier_id)


@pytest.fixture
def fixture_error_on_request_without_courier_id():
    with allure.step('Создание заказа'):
        track_id = create_order()
    with allure.step('Получение Id заказа'):
        order_id = get_order_id_by_track(track_id)

    yield order_id

    with allure.step('Отмена заказа'):
        cancel_order(track_id)

@pytest.fixture
def fixture_error_on_request_invalid_courier_id():
    with allure.step('Создание заказа'):
        track_id = create_order()
    with allure.step('Получение Id заказа'):
        order_id = get_order_id_by_track(track_id)
    with allure.step('Создание курьера'):
        courier_id = register_new_courier()
    with allure.step('Удаление курьера'):
        delete_courier(courier_id)

    yield order_id, courier_id

    with allure.step('Отмена заказа'):
        cancel_order(track_id)

@pytest.fixture
def fixture_error_on_request_with_empty_order_id():
    with allure.step('Создание курьера'):
        courier_id = register_new_courier()

    yield courier_id

    with allure.step('Удаление курьера'):
        delete_courier(courier_id)