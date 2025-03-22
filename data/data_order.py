test_cases_for_order = {
    "Создание заказа с указанием цвета самоката GREY": {
        "request": {
            "firstName": "Sofia",
            "lastName": "Prekarasnaya",
            "address": "Санкт-Петербург, улица А, 142 apt.",
            "metroStation": 9,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2025-03-26",
            "comment": "звоните в домофон",
            "color": [
                "GREY"
            ]
        },
        "response": {
            "status_code": 201
        }
    },
    "Создание заказа с указанием цвета самоката BLACK": {
        "request": {
            "firstName": "Sofia",
            "lastName": "Prekarasnaya",
            "address": "Санкт-Петербург, улица А, 142 apt.",
            "metroStation": 9,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2025-03-26",
            "comment": "звоните в домофон",
            "color": [
                "BLACK"
            ]
        },
        "response": {
            "status_code": 201
        }
    },
    "Создание заказа с указанием обоих цветов самоката": {
        "request": {
            "firstName": "Sofia",
            "lastName": "Prekarasnaya",
            "address": "Санкт-Петербург, улица А, 142 apt.",
            "metroStation": 9,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2025-03-26",
            "comment": "звоните в домофон",
            "color": [
                "BLACK", "GREY"
            ]
        },
        "response": {
            "status_code": 201
        }
    },
    "Создание заказа без указания цвета самоката": {
        "request": {
            "firstName": "Sofia",
            "lastName": "Prekarasnaya",
            "address": "Санкт-Петербург, улица А, 142 apt.",
            "metroStation": 9,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2025-03-26",
            "comment": "звоните в домофон",
            "color": [

            ]
        },
        "response": {
            "status_code": 201
        }
    }
}