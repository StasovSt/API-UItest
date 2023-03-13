import json
import pytest
import requests
from requests import Response


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