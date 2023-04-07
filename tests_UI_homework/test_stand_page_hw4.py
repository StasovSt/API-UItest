"""Домашнее задание по уроку 4"""
import os
import time

import pytest
from selenium.webdriver import Chrome, Keys
from selenium.webdriver.common.by import By
from lib.functions_UI import login, element_is_present, element_text


@pytest.mark.skip
def test_page_about():
    """Авторизация,
    Заполнение полей о себе - enter
    Проверка наличия элемента и сообщения об успехе"""
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/login?next=about.about_page")
        login(browser)

        browser.find_element(By.NAME, "name").send_keys("qwerty")
        browser.find_element(By.NAME, "surname").send_keys("qwerty")
        browser.find_element(By.ID, "age2").click()
        browser.find_element(By.ID, "lang1").click()
        browser.find_element(By.CSS_SELECTOR, "[id=lvl] :nth-child(2)").click()
        browser.find_element(By.NAME, "surname").send_keys(Keys.ENTER)

        assert element_is_present(browser, By.CSS_SELECTOR, ".is-success"), "Нет элемента об успехе"


def test_upload_file_and_refresh():
    """Авторизация,
    Загрузка файла,
    Проверка наличия элемента и сообщения об успехе
    Рефреш страницы
    Проверка отсутствия элемента об успехе"""
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/upload_file")
        login(browser)

        browser.find_element(By.CSS_SELECTOR, '[type="file"]').send_keys(os.path.join(os.getcwd(), "files", "bwS6557_Xlo.jpg"))
        browser.find_element(By.CSS_SELECTOR, ".button").click()

        assert element_is_present(browser, By.CSS_SELECTOR, ".is-success"), "Нет элемента об успехе"
        assert element_text(browser, By.CSS_SELECTOR, ".is-success") == "Успех", \
            f'Написано другое: {browser.find_element(By.CSS_SELECTOR, ".is-success").text}'

        browser.refresh()
        time.sleep(3)
        assert not element_text(browser, By.CSS_SELECTOR, ".is-success"), \
            f'Написано другое: {browser.find_element(By.CSS_SELECTOR, ".is-success").text}'
