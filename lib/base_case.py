from datetime import datetime
from requests import Response
import json.decoder
from lib.helper import generate_random_string
from lib.my_requests import MyRequests


class BaseCase:
    """Реализованные методы"""
    def get_cookie(self, response: Response, cookie_name):
        """Метод по получению куки-данных"""
        assert cookie_name in response.cookies, f"Cannot find cookie with name {cookie_name} in the last response"
        return response.cookies[cookie_name]

    def get_header(self, response: Response, header_name):
        assert header_name in response.headers, f"Cannot find header with name {header_name} in the last response"
        return response.headers[header_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"response is not JSON format, response text is '{response.text}'"

        assert name in response_as_dict, f"response JSON doesn't have key '{name}'"

        return response_as_dict[name]

    def prepare_registration_data(self, email=None, username_lenght=10):
        username = generate_random_string(username_lenght)
        if email is None:
            base_part = "learnQa"
            domain = "examplee.comm"
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"{base_part}{random_part}@{domain}"

        return {
            "password": "12345",
            "username": username,
            "firstName": "learnQaaa",
            "lastName": "learnQaaa",
            "email": email
        }

    def prepare_registration_data_without_one_parameter(self, parameter):
        if parameter == "email":
            return {"password": "12345", "username": "learnQaaa", "firstName": "learnQaaa", "lastName": "learnQaaa"}
        elif parameter == "password":
            return {"email": "learnQa@examplee.comm", "username": "learnQaaa", "firstName": "learnQaaa", "lastName": "learnQaaa"}
        elif parameter == "firstName":
            return {"email": "learnQa@examplee.comm", "username": "learnQaaa", "password": "12345", "lastName": "learnQaaa"}
        elif parameter == "lastName":
            return {"email": "learnQa@examplee.comm", "username": "learnQaaa", "password": "12345", "firstName": "learnQaaa"}
        elif parameter == "username":
            return {"email": "learnQa@examplee.comm", "firstName": "learnQaaa", "password": "12345", "lastName": "learnQaaa"}
        else:
            assert False, "Не указан параметр без которого будет отправляться запрос"
