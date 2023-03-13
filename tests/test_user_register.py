from datetime import datetime
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserRegister(BaseCase):
    def setup_method(self):
        base_part = "learnQa"
        domain = "examplee.comm"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        self.email = f"{base_part}{random_part}@{domain}"

    def test_create_user_successfully(self):
        data = {
            "password": "123",
            "username": "learnQa",
            "firstName": "learnQa",
            "lastName": "learnQa",
            "email": self.email
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")


    def test_user_with_existing_email(self):
        email = "learnQa@examplee.comm"
        data = {
            "password": "123",
            "username": "learnQa",
            "firstName": "learnQa",
            "lastName": "learnQa",
            "email": email
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", \
            f"Непредвиденный контент: {response.content}"



