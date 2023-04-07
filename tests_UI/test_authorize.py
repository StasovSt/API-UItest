import pytest
from selenium.webdriver import Chrome
from lib.functions_UI import wait_url_to_be, login
from .data import AuthData

@pytest.mark.auth
class TestAuth:
    @pytest.mark.smoke
    def test_authorize_positive(self):
        with Chrome() as browser:
            browser.get("https://qastand.valhalla.pw/login")
            login(browser, "qa_test@test.ru", "!QAZ2wsx")
            assert wait_url_to_be(browser, "https://qastand.valhalla.pw/profile")
            cokkie_dict = browser.get_cookie("session")
            assert cokkie_dict["name"] == "session", "У куки другое наименование"


    @pytest.mark.parametrize("negative_email, negative_password", AuthData.INVALID_AUTH_DATA, ids=AuthData.NEGATIVE_TESTS_IDS)
    def test_authorize_negative(self, negative_email, negative_password):
        with Chrome() as browser:
            browser.get("https://qastand.valhalla.pw/login")
            login(browser, negative_email, negative_password)
            assert wait_url_to_be(browser, "https://qastand.valhalla.pw/login")
