test_cases_for_authorization_courier_valid = {
    "Успешная_авторизация курьера": {
        "request": {
            "login": "Tester_Alina",
            "password": "1234"
        },
        "response": {
            "status_code": 200,
            "courier_code": 485450
        }
    }
}
test_cases_for_authorization_courier_invalid = {
    "Проверка, что приходит ошибка при авторизации с неправильным паролем": {
        "request": {
            "login": "Tester_Alina",
            "password": "4545"
        },
        "response": {
            "status_code": 404,
            "message": "Учетная запись не найдена"
        }
    },
    "Проверка, что приходит ошибка при авторизации с несуществующим логином": {
        "request": {
            "login": "ХрумХрум",
            "password": "1234"
        },
        "response": {
            "status_code": 404,
            "message": "Учетная запись не найдена"
        }
    },
    "Проверка, что приходит ошибка при авторизации с незаполненным логином": {
        "request": {
            "password": "1234"
        },
        "response": {
            "status_code": 400,
            "message":  "Недостаточно данных для входа"
        }
    },
    "Проверка, что приходит ошибка при авторизации с незаполненным паролем": {
        "request": {
            "login": "Tester_Alina"
        },
        "response": {
            "status_code": 400,
            "message":  "Недостаточно данных для входа"
        }
    }
}