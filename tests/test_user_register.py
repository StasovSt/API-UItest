import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


class TestUserRegister(BaseCase):
    def test_create_user_successfully(self):
        """Позитивный тест
        Запрос на регистрацию юзера валидными данными
        Чек статус-кода и корректного ответа"""
        data = self.prepare_registration_data()

        response = MyRequests.post("user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_user_with_existing_email(self):
        """Негативный тест
        Запрос на регистрацию юзера с существующим в системе 'email'
        Чек статус-кода и корректного ответа"""

        email = "learnQa@examplee.comm"
        data = self.prepare_registration_data(email)

        response = MyRequests.post("user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", \
            f"Непредвиденный контент: {response.content}"

    def test_user_without_simbol_in_email(self):
        """Негативный тест
        Запрос на регистрацию юзера с неккоректным 'email' (отсутствует '@')
        Чек статус-кода и корректного ответа"""

        email = "learnQaexamplee.comm"
        data = self.prepare_registration_data(email)

        response = MyRequests.post("user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Invalid email format", \
            f"Successfully registered with email {email}"

    @pytest.mark.parametrize("parameter", ["email", "password", "firstName", "lastName", "username"])
    def test_user_without_one_parameters(self, parameter):
        """Негативный тест
        Поочередный прогон запросов на регистрацию юзера с неккоректным body запроса
        (отсутствует один из парметров из списка 'parameter')
        Чек статус-кода и корректного ответа"""

        data = self.prepare_registration_data_without_one_parameter(parameter)
        response = MyRequests.post("user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The following required params are missed: {parameter}", \
            f"Successfully registered without {parameter}"

    def test_user_with_short_username(self):
        """Негативный тест
        Регистрация юзера с username == 1 символ
        Чек статус-кода и корректного ответа"""

        data = self.prepare_registration_data(username_lenght=1)

        response = MyRequests.post("user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'username' field is too short", \
            f"Непредвиденный контент: {response.content}"

    def test_user_with_long_username(self):
        """Негативный тест
        Регистрация юзера с username == 251 символов
        Чек статус-кода и корректного ответа"""

        data = self.prepare_registration_data(username_lenght=251)

        response = MyRequests.post("user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'username' field is too long", \
            f"Непредвиденный контент: {response.content}"
