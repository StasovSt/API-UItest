import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from functions import login, wait_text_in_element, wait_until_clicable, check_alert_is_present, wait_until_visible, element_is_present, wait_url_to_be


def test_page_with_timer():
    """Авторизация,
    Ожидание кликабельности кнопки 'Отправить'
    Ожидание что значение равно 100
    Клик на кнопку отправить
    Проверка алерта об Успехе"""
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/wait")
        login(browser)

        button = wait_until_clicable(browser, (By.CSS_SELECTOR, '[onclick="check_value()"]'))
        wait_text_in_element(browser, (By.ID, "demo"), "100")
        button.click()

        check_alert_is_present(browser)


def test_page_slow_loading():
    """Авторизация,
    Ожидание кликабельности кнопки 'Отправить'
    Ожидание что значение равно 100
    Клик на кнопку отправить
    Проверка алерта об Успехе"""
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/slow_load")
        login(browser)

        wait_until_visible(browser, (By.ID, "text_input"))
        wait_until_clicable(browser, (By.ID, "text_input")).send_keys("qwerty")
        wait_until_clicable(browser, (By.ID, "button")).click()

        assert element_is_present(browser, (By.CSS_SELECTOR, ".is-success")), "Нет элемента об успехе"

        browser.refresh()

        assert not element_is_present(browser, (By.CSS_SELECTOR, ".is-success")), "Есть элемент об успехе"

def test_page_navigate():
    """tyjyku,imtehnyr"""
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/profile")
        login(browser)
        wait_until_clicable(browser, (By.CSS_SELECTOR, '[href="/my_pet"]')).click()

        new_url = "https://qastand.valhalla.pw/my_pet"

        assert wait_url_to_be(browser, new_url), "Oncorret URL"




