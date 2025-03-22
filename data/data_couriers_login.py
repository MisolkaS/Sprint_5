from helpers import *
test_cases_for_register_new_courier = {
    "Успешное добавление курьера с валидным логином и паролем и заполненным именем курьера русскими буквами": {
        "request": {
            "login": generate_random_string(5),
            "password": "1234",
            "firstName": "АЛина"
        },
        "response": {
            "status_code": 201,
            "message": {"ok": True}
        }
    },
    "Успешное добавление курьера с валидным логином и паролем и пустым именем курьера": {
        "request": {
            "login": generate_random_string(5),
            "password": "1234",
            "firstName": ""
        },
        "response": {
            "status_code": 201,
            "message": {"ok": True}
        }
    },
    "Успешное добавление курьера с валидным логином и паролем и именем курьера английскими буквами": {
        "request": {
            "login": generate_random_string(5),
            "password": "1234",
            "firstName": "ALiNАААA"
        },
        "response": {
            "status_code": 201,
            "message": {"ok": True}
        }
    },
    "Успешное добавление курьера с валидным логином и паролем и незаполненным именем курьера": {
        "request": {
            "login": generate_random_string(5),
            "password": "1234"
        },
        "response": {
            "status_code": 201,
            "message": {"ok": True}
        }
    },
    "Успешное добавление курьера с валидным логином из 2 символов и паролем и заполненным именем курьера": {
        "request": {
            "login": generate_random_string(2),
            "password": "1234",
            "firstName": "Алина"
        },
        "response": {
            "status_code": 201,
            "message": {"ok": True}
        }
    },
    "Успешное добавление курьера с валидным логином из 3 символов и паролем и заполненным именем курьера": {
        "request": {
            "login": generate_random_string(3),
            "password": "1234",
            "firstName": "Алина"
        },
        "response": {
            "status_code": 201,
            "message": {"ok": True}
        }
    },
    "Успешное добавление курьера с валидным логином из 9 символов и паролем и заполненным именем курьера": {
        "request": {
            "login": generate_random_string(9),
            "password": "1234",
            "firstName": "Алина"
        },
        "response": {
            "status_code": 201,
            "message": {"ok": True}
        }
    },
    "Успешное добавление курьера с валидным логином из 10 символов и паролем и заполненным именем курьера": {
        "request": {
            "login": generate_random_string(10),
            "password": "1234",
            "firstName": "Алина"
        },
        "response": {
            "status_code": 201,
            "message": {"ok": True}
        }
    },
    "Ошибка валидации при добавлении курьера с логином из 1 символа": {
        "request": {
            "login": generate_random_string(1),
            "password": "1234",
            "firstName": "Alina"
        },
        "response": {
            "status_code": 400,
            "message": "Недостаточно данных для создания учетной записи"

        }
    },
    "Ошибка валидации при добавлении курьера с логином из 11 символов": {
        "request": {
            "login": generate_random_string(11),
            "password": "1234",
            "firstName": "Alina"
        },
        "response": {
            "status_code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }
    },
    "Ошибка валидации при добавлении курьера с логином из русских букв": {
        "request": {
            "login": generate_random_string(5, 'russian'),
            "password": "1234",
            "firstName": "Alina"
        },
        "response": {
            "status_code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }
    },
    "Ошибка валидации при добавлении курьера с пустым логином": {
        "request": {
            "login": "",
            "password": "1234",
            "firstName": "Alina"
        },
        "response": {
            "status_code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }
    },
    "Ошибка валидации при добавлении курьера без логина": {
        "request": {
            "password": "1234",
            "firstName": "Alina"
        },
        "response": {
            "status_code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }
    },
    "Ошибка валидации при добавлении курьера с None в логине": {
        "request": {
            "login": None,
            "password": "1234",
            "firstName": "Alina"
        },
        "response": {
            "status_code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }
    },
    "Ошибка валидации при добавлении курьера с числом в логине": {
        "request": {
            "login": 124,
            "password": "1234",
            "firstName": "Alina"
        },
        "response": {
            "status_code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }
    },
    "Ошибка валидации при добавлении курьера, где число в строке в логине": {
        "request": {
            "login": "123",
            "password": "1234",
            "firstName": "Alina"
        },
        "response": {
            "status_code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }
    },
    "Ошибка валидации при добавлении курьера, где спецсимволы в строке в логине": {
        "request": {
            "login": generate_random_string(5) + "%$",
            "password": "1234",
            "firstName": "Alina"
        },
        "response": {
            "status_code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }
    },
    "Ошибка валидации при добавлении курьера, где математические символы в строке в логине": {
        "request": {
            "login": generate_random_string(5) + "+",
            "password": "1234",
            "firstName": "Alina"
        },
        "response": {
            "status_code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }
    },
    "Ошибка валидации при добавлении курьера, где строке есть пробелы в логине": {
        "request": {
            "login": generate_random_string(5) + " na ",
            "password": "1234",
            "firstName": "Alina"
        },
        "response": {
            "status_code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }
    },
    "Успешное добавление курьера с паролем из 4 цифр, и валидными логином и заполненным именем курьера": {
        "request": {
            "login": "AlinaS",
            "password": "0000",
            "firstName": "Алина"
        },
        "response": {
            "status_code": 201,
            "message": {"ok": True}
        }
    },
    "Ошибка валидации при добавлении курьера с паролем из 3 символов": {
        "request": {
            "login": generate_random_string(5),
            "password": "123",
            "firstName": "Alina"
        },
        "response": {
            "status_code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }
    },
    "Ошибка валидации при добавлении курьера c пустым паролем": {
        "request": {
            "login": generate_random_string(5),
            "password": None,
            "firstName": "Alina"
        },
        "response": {
            "status_code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }
    },
    "Ошибка валидации при добавлении курьера c незаполненным паролем": {
        "request": {
            "login": generate_random_string(5),
            "password": "",
            "firstName": "Alina"
        },
        "response": {
            "status_code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }
    },
    "Ошибка валидации при добавлении курьера без пароля": {
        "request": {
            "login": generate_random_string(5),
            "firstName": "Alina"
        },
        "response": {
            "status_code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }
    },
    "Ошибка валидации при добавлении курьера с None в пароле": {
        "request": {
            "login": generate_random_string(5),
            "password": None,
            "firstName": "Alina"
        },
        "response": {
            "status_code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }
    },
    "Ошибка валидации при добавлении курьера с числом в пароле": {
        "request": {
            "login": generate_random_string(5),
            "password": 1234,
            "firstName": "Alina"
        },
        "response": {
            "status_code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }
    },
    "Ошибка валидации при добавлении курьера, где в пароле буквы": {
        "request": {
            "login": generate_random_string(5),
            "password": "Aaaa",
            "firstName": "Alina"
        },
        "response": {
            "status_code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }
    },
    "Ошибка валидации при добавлении курьера, где в пароле спецсимволы в строке": {
        "request": {
            "login": generate_random_string(5),
            "password": "12?4",
            "firstName": "Alina"
        },
        "response": {
            "status_code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }
    },
    "Ошибка валидации при добавлении курьера, где в пароле математические символы в строке": {
        "request": {
            "login": generate_random_string(5),
            "password": "1+34",
            "firstName": "Alina"
        },
        "response": {
            "status_code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }
    },
    "Ошибка валидации при добавлении курьера, где в пароле есть пробелы": {
        "request": {
            "login": generate_random_string(5),
            "password": "12 4",
            "firstName": "Alina"
        },
        "response": {
            "status_code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }
    },
    "Успешное добавление курьера с валидным логином и паролем, и именем курьера английскими буквами из 4 букв": {
        "request": {
            "login": generate_random_string(5),
            "password": "1234",
            "firstName": "ALiN"
        },
        "response": {
            "status_code": 201,
            "message": {
                "ok": True
            }
        }
    },
    "Успешное добавление курьера с валидным логином и паролем, и именем курьера английскими буквами из 5 букв": {
        "request": {
            "login": generate_random_string(5),
            "password": "1234",
            "firstName": "ALiNА"
        },
        "response": {
            "status_code": 201,
            "message": {
                "ok": True
            }
        }
    },
    "Успешное добавление курьера с валидным логином и паролем, и именем курьера английскими буквами из 9 букв": {
        "request": {
            "login": generate_random_string(5),
            "password": "1234",
            "firstName": "ALiNALiN"
        },
        "response": {
            "status_code": 201,
            "message": {
                "ok": True
            }
        }
    },
    "Успешное добавление курьера с валидным логином и паролем, и именем курьера английскими буквами из 10 букв": {
        "request": {
            "login": generate_random_string(5),
            "password": "1234",
            "firstName": "АЛИНААЛИНА"
        },
        "response": {
            "status_code": 201,
            "message": {
                "ok": True
            }
        }
    },
    "Ошибка валидации при добавлении курьера с None в имене курьера": {
        "request": {
            "login": generate_random_string(5),
            "password": "1234",
            "firstName": None
        },
        "response": {
            "status_code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }
    },
    "Ошибка валидации при добавлении курьера с именем курьера менее 2 символов": {
        "request": {
            "login": generate_random_string(5),
            "password": "1234",
            "firstName": "A"
        },
        "response": {
            "status_code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }
    },
    "Ошибка валидации при добавлении курьера с именем курьера из 11 символов": {
        "request": {
            "login": generate_random_string(5),
            "password": "1234",
            "firstName": "AlinaAlinas"
        },
        "response": {
            "status_code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }
    },
    "Ошибка валидации при добавлении курьера с числом в имени курьера": {
        "request": {
            "login": generate_random_string(5),
            "password": "1234",
            "firstName": "1234453"
        },
        "response": {
            "status_code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }
    },
    "Ошибка валидации при добавлении курьера, где число в имени курьера": {
        "request": {
            "login": generate_random_string(5),
            "password": "1234",
            "firstName": 12345
        },
        "response": {
            "status_code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }
    },
    "Ошибка валидации при добавлении курьера, где спецсимволы в строке в имени курьера": {
        "request": {
            "login": generate_random_string(5),
            "password": "1234",
            "firstName": "Alina%"
        },
        "response": {
            "status_code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }
    },
    "Ошибка валидации при добавлении курьера, где математические символы в строке в имени курьера": {
        "request": {
            "login": generate_random_string(5),
            "password": "1234",
            "firstName": "Alina+"
        },
        "response": {
            "status_code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }
    },
    "Ошибка валидации при добавлении курьера, где строке есть пробелы в имени курьера": {
        "request": {
            "login": generate_random_string(5),
            "password": "1234",
            "firstName": " Aliа na "
        },
        "response": {
            "status_code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }
    }
}