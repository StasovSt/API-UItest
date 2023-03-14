from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


class TestUserGet(BaseCase):

    def test_get_user_details_not_auth(self):
        """Запрос на получение данных неавторизованным юзером
        Проверка того, что в теле ответа присутствует username
        Проверка того, что в теле ответа отсутствуют email, lastName, firstName"""

        response = MyRequests.get("user/65408")

        unexpected_fields = ["email", "lastName", "firstName"]
        Assertions.assert_json_has_key(response, "username")
        Assertions.assert_json_has_not_keys(response, unexpected_fields)

    def test_get_user_details_auth_as_same_user(self):
        """Запрос на получение данных авторизованным юзером
        Проверка того, что в теле ответа присутствуют username, email, lastName, firstName"""

        data = {
            "email": "tester@example.ru",
            "password": "12345"
        }
        response1 = MyRequests.post("user/login", data=data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        response2 = MyRequests.get(
            f"user/{user_id_from_auth_method}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        expected_fields = ["username", "email", "lastName", "firstName"]
        Assertions.assert_json_has_keys(response2, expected_fields)

    def test_get_one_user_details_auth_as_others_user(self):
        """Запрос на получение данных одного юзера авторизованным другим юзером
        Проверка того, что в теле ответа присутствует username
        Проверка того, что в теле ответа отсутствуют email, lastName, firstName"""

        data = {
            "email": "tester@example.ru",
            "password": "12345"
        }
        response1 = MyRequests.post("user/login", data=data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")

        response2 = MyRequests.get(
            f"user/2",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        unexpected_fields = ["email", "lastName", "firstName"]
        Assertions.assert_json_has_key(response2, "username")
        Assertions.assert_json_has_not_keys(response2, unexpected_fields)