
from typing import Tuple
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def login(browser):
    wait_until_clicable(browser, (By.NAME, "email")).send_keys("qa_test@test.ru")
    wait_until_clicable(browser, (By.NAME, "password")).send_keys("!QAZ2wsx")
    wait_until_clicable(browser, (By.CLASS_NAME, "button")).click()


def wait_until_visible(driver, locator: Tuple, timeout: int = 5) -> WebElement:
    return WebDriverWait(driver, timeout).until(ec.visibility_of_element_located(locator))


def wait_url_to_be(driver, url:str, timeout: int = 5):
    return WebDriverWait(driver, timeout).until(ec.url_to_be(url))


def wait_until_clicable(driver, locator: Tuple, timeout: int = 5) -> WebElement:
    return WebDriverWait(driver, timeout).until(ec.element_to_be_clickable(locator))


def wait_until_present(driver, locator: Tuple, timeout: int = 5) -> WebElement:
    return WebDriverWait(driver, timeout).until(ec.presence_of_element_located(locator))


def wait_text_in_element(driver, locator: Tuple, text: str, timeout: int = 15) -> bool:
    return WebDriverWait(driver, timeout).until(ec.text_to_be_present_in_element(locator, text))


def element_is_present(driver, locator: Tuple, timeout: int = 5) -> bool:
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


def check_alert_is_present(driver, timeout=5) -> None:
   alert = WebDriverWait(driver, timeout).until(ec.alert_is_present())
   assert "Успех!" in alert.text
