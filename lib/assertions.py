from requests import Response
import json

class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Responce is not in JSON format, response test is '{response.text}'"

        assert name in response_as_dict, f"responce JSON doesn't have key '{name}'"
        assert response_as_dict[name] == expected_value, error_message

    @staticmethod
    def assert_json_has_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Responce is not in JSON format, response test is '{response.text}'"

        assert name in response_as_dict, f"responce JSON doesn't have key '{name}'"


    @staticmethod
    def assert_code_status(response: Response, expected_status_code):
        assert response.status_code == expected_status_code,\
            f"Непредвиденный статус код: {response.status_code}, ожидался: {expected_status_code}"