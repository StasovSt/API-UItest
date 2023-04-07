import pytest
from selenium.webdriver import Chrome
from lib.functions_UI import wait_url_to_be, login
from .data import AuthData, URL

@pytest.mark.auth
class TestAuth:
    @pytest.mark.smoke
    def test_authorize_positive(self, browser):
        browser.get(URL.LOGIN_URL)
        login(browser, AuthData.VALID_AUTH_DATA["login"], AuthData.VALID_AUTH_DATA["password"])
        assert wait_url_to_be(browser, URL.MAIN_URL)
        cokkie_dict = browser.get_cookie("session")
        assert cokkie_dict["name"] == "session", "У куки другое наименование"


    @pytest.mark.parametrize("negative_email, negative_password", AuthData.INVALID_AUTH_DATA, ids=AuthData.NEGATIVE_TESTS_IDS)
    def test_authorize_negative(self, browser, negative_email, negative_password):
        with Chrome() as browser:
            browser.get(URL.LOGIN_URL)
            login(browser, negative_email, negative_password)
            assert wait_url_to_be(browser, URL.LOGIN_URL)
