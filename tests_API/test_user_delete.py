from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests



class TestUserDelete(BaseCase):
    """Проверка метода delete"""

    def test_delete_user_userid2(self):
        """Негативный тест
        Авторизация под пользователем с id 2
        Попытка удалить его"""

        # LOGIN
        login_data = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }

        response1 = MyRequests.post("user/login", data=login_data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id = self.get_json_value(response1, "user_id")

        # DELETE
        response2 = MyRequests.delete(f"user/{user_id}", headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})

        Assertions.assert_code_status(response2, 400)
        assert response2.content.decode("utf-8") == f"Please, do not delete test users with ID 1, 2, 3, 4 or 5.", \
            f"Непредвиденный контент: {response2.content}"

    def test_delete_user(self):
        """Позитивный тест
        Регистрация юзера
        Авторизация
        Удаление
        Проверка того что юзер удален"""

        # REGISTER  USER

        register_data = self.prepare_registration_data()
        email = register_data["email"]
        password = register_data["password"]

        response1 = MyRequests.post("user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            "email": email,
            "password": password
        }

        response2 = MyRequests.post("user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # DELETE
        response3 = MyRequests.delete(f"user/{user_id}", headers={"x-csrf-token": token},
                                      cookies={"auth_sid": auth_sid})

        Assertions.assert_code_status(response3, 200)

        #GET USER WAS DELETED
        response4 = MyRequests.get(
            f"user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response4, 404)
        assert response4.content.decode("utf-8") == f"User not found", \
            f"Непредвиденный контент: {response4.content}"


    def test_delete_user_auth_other_user(self):
        """Негативный тест
        Авторизация под пользователем с id 2
        Попытка удалить юзера с другим id"""

        # LOGIN
        login_data = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }

        response1 = MyRequests.post("user/login", data=login_data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        print(auth_sid)
        token = self.get_header(response1, "x-csrf-token")
        print(token)
        user_id = self.get_json_value(response1, "user_id")

        # DELETE
        response2 = MyRequests.delete(f"user/{user_id}", headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid}, data={"user_id": 1000})

        print(response2.status_code)
        print(response2.content)

        # Assertions.assert_code_status(response2, 400)
        # assert response2.content.decode("utf-8") == f"Please, do not delete test users with ID 1, 2, 3, 4 or 5.", \
        #     f"Непредвиденный контент: {response2.content}"