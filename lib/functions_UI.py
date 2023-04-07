from typing import Tuple
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from lib.locators import AuthLocators


def wait_until_visible(driver, locator: Tuple, timeout: int = 5) -> WebElement:
    """Ожидание пока элемент станет видимым"""
    return WebDriverWait(driver, timeout).until(ec.visibility_of_element_located(locator))


def wait_url_to_be(driver, url: str, timeout: int = 5):
    """Ожидание пока url станет равным"""
    return WebDriverWait(driver, timeout).until(ec.url_to_be(url))


def wait_until_clicable(driver, locator: Tuple, timeout: int = 5) -> WebElement:
    """Ожидание пока элемент станет кликабельным"""
    return WebDriverWait(driver, timeout).until(ec.element_to_be_clickable(locator))


def wait_until_present(driver, locator: Tuple, timeout: int = 5) -> WebElement:
    """Ожидание пока элемент не появится в DOM"""
    return WebDriverWait(driver, timeout).until(ec.presence_of_element_located(locator))


def wait_text_in_element(driver, locator: Tuple, text: str, timeout: int = 15) -> bool:
    """Ожидание пока текст не появится в элементе"""
    return WebDriverWait(driver, timeout).until(ec.text_to_be_present_in_element(locator, text))


def element_is_present(driver, locator: Tuple, timeout: int = 5) -> bool:
    """Проверка на наличие элемента с ожиданием"""
    try:
        wait_until_present(driver, locator, timeout)
        return True
    except TimeoutException:
        return False


def element_text(driver, locator: Tuple, timeout: int = 5):
    try:
        return wait_until_visible(driver, locator, timeout).text
    except TimeoutException:
        return None


def login(browser, login_value: str, password_value: str):
    wait_until_clicable(browser, AuthLocators.EMAIL_ELEMENT).send_keys(login_value)
    wait_until_clicable(browser, AuthLocators.PASSWORD_ELEMENT).send_keys(password_value)
    wait_until_clicable(browser, AuthLocators.REMEMBER_ME_CHECKBOX).click()
    wait_until_clicable(browser, AuthLocators.BUTTON_ENTRY).click()


def check_alert_is_present(driver, timeout=5) -> None:
    alert = WebDriverWait(driver, timeout).until(ec.alert_is_present())
    assert "Успех!" in alert.text
