expected_keys = {
        'orders': ['id', 'courierId', 'firstName', 'lastName', 'address', 'metroStation', 'phone', 'rentTime', 'deliveryDate', 'track', 'color', 'comment', 'createdAt', 'updatedAt', 'status'],
        'pageInfo': ['page', 'total', 'limit'],
        'availableStations': ['name', 'number', 'color']
    }

test_cases_for_list_order = {
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
}