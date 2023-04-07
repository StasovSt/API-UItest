import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from lib.functions_UI import login, wait_until_clicable, wait_until_visible


def test_page_new_tab():
    """Авторизация,
    Проверка что открыта одна вкладка,
    Клик по кнопке новая вкладка,
    Переход по второй вкладке,
    Проверка что открыты две вкладке,
    Кнопка 'Ок' в модалке,
    Проверка что открыта одна вкладка
    """
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/new_window_button")
        login(browser)

        windows = browser.window_handles
        assert len(windows) == 1

        wait_until_clicable(browser, (By.CSS_SELECTOR, '[onclick="myFunction()"]')).click()
        windows = browser.window_handles
        browser.switch_to.window(windows[1])
        assert len(windows) == 2

        wait_until_clicable(browser, (By.CSS_SELECTOR, '[onclick="myFunction()"]')).click()
        allert = browser.switch_to.alert
        assert allert.text == "Успех!", "Wrong text in alert"
        allert.accept()
        time.sleep(0.5)

        windows = browser.window_handles
        assert len(windows) == 1


def test_page_modal_window():
    """Авторизация
    """
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/three_buttons")
        login(browser)
        wait_until_clicable(browser, (By.CSS_SELECTOR, '[onclick="confirm_func()"]')).click()
        browser.switch_to.alert.dismiss()
        time.sleep(2)
        assert wait_until_clicable(browser, (By.ID, 'confirm_text')).text == "Не запускаем", "Wrong text"


def test_page_iframe():
    """Авторизация
    Переход на iframe
    Клик по кнопке 'Подтвердить'
    Переход по алерту - кнопка ОК
    Переключение в контекст основного DOM"""
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/iframe_page")
        login(browser)
        WebDriverWait(browser, 5).until(ec.frame_to_be_available_and_switch_to_it((By.ID, "my_iframe")))

        assert wait_until_visible(browser, (By.CSS_SELECTOR, '[src="/static/sloth.png"]'))

        wait_until_clicable(browser, (By.CSS_SELECTOR, '[onclick="alert_func()"]')).click()
        browser.switch_to.alert.accept()

        browser.switch_to.default_content()







