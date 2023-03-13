import pytest
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserAuth(BaseCase):
    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]

    def setup(self):
        data = {
            "email": "tester@example.ru",
            "password": "12345"
        }
        responce1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

        self.auth_sid = self.get_cookie(responce1, "auth_sid")
        self.token = self.get_header(responce1, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(responce1, "user_id")

    def test_auth_user(self):
        response2 = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            headers={self.token},
            cookies={self.auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response2,
            "user_id",
            self.user_id_from_auth_method,
            "There is no user_id in the second responce"
        )
