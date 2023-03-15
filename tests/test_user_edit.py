import time
import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.helper import user
from lib.my_requests import MyRequests


class TestUserEdit(BaseCase):
    """Проверка put-метода изменения данных юзера"""

    @pytest.fixture(scope="class", autouse=True)
    def setup(self):
        # REGISTER ONE USER

        register_data = self.prepare_registration_data()

        email = register_data["email"]
        first_name = register_data["firstName"]
        password = register_data["password"]
        username = register_data["username"]

        user["email"] = email
        user["first_name"] = first_name
        user["password"] = password
        user["username"] = username

        response1 = MyRequests.post("user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        user_id = self.get_json_value(response1, "id")
        user["user_id"] = user_id


    def test_edit_just_created_user(self):
        """Позитивный тест
        Использование зарегистрированного юзера (в setup методе)
        Авторизация юзера
        Изменение данных (firstName)
        Проверка, что данные изменились"""

        email = user["email"]
        password = user["password"]
        user_id = user['user_id']

        # LOGIN
        login_data = {
            "email": email,
            "password": password
        }
        print(login_data)

        response2 = MyRequests.post("user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # EDIT
        new_name = "Changed Name"
        response3 = MyRequests.put(f"user/{user_id}", headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid}, data={"firstName": new_name})

        Assertions.assert_code_status(response3, 200)

        # GET
        response4 = MyRequests.get(
            f"user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response4, 200)
        Assertions.assert_json_value_by_name(response4, "firstName", new_name, "Какое то левое Имя")

    def test_edit_user_no_auth(self):
        """Негативный тест
        Регистрация нового юзера (вынесено в setup) без авторизации
        Изменение данных (firstName)
        Проверка того, что при попытке изменения данных приходит ошибка"""

        # EDIT
        user_id = user['user_id']
        new_name = "Changed Name"

        response2 = MyRequests.put(
            f"user/{user_id}",
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response2, 400)
        assert response2.content.decode("utf-8") == f"Auth token not supplied", \
            f"Непредвиденный контент: {response2.content}"

    def test_edit_user_auth_by_other_user(self):
        """Негативный тест
        Регистрация первого юзера (вынесено в setup)
        Регистрация второго юзера - получение sid юзера
        Авторизация второго юзера
        Изменение данных первого юзера (firstName)
        Проверка того, что при попытке изменения данных приходит ошибка"""

        # DATA FIRST USER
        user_id1 = user['user_id']
        username1 = user['username']

        # REGISTER SECOND USER
        register_data2 = self.prepare_registration_data()
        email2 = register_data2["email"]
        password2 = register_data2["password"]

        response2 = MyRequests.post("user/", data=register_data2)

        Assertions.assert_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, "id")

        # LOGIN SECOND USER
        login_data = {
            "email": email2,
            "password": password2
        }

        response2 = MyRequests.post("user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # EDIT
        new_name = "Changed Name"

        response3 = MyRequests.put(
            f"user/{user_id1}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"username": new_name}
        )

        Assertions.assert_code_status(response2, 200)
        print(response3.content)
        assert response3.content.decode("utf-8") == "", \
            f"Непредвиденный контент: {response3.content}"

        # GET
        response4 = MyRequests.get(
            f"user/{user_id1}"
        )
        Assertions.assert_json_has_not_key(response4, username1)


