"""Домашнее задание по уроку 3"""
import time

import pytest
from selenium.webdriver import Chrome
from functions import login, element_is_present, element_text
from selenium.webdriver.common.by import By


def test_word_field_entry_and_button():
    """Авторизация,
     Поиск кнопки с уникальным атрибутом,
     Ввод произвольного текста,
     Проверка наличия элемента и сообщения об успехе"""
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/login?next=inputs.inputs_page")
        login(browser)
        browser.find_element(By.NAME, "test").send_keys("qwerty")
        browser.find_element(By.CSS_SELECTOR, '[method="POST"] .button').click()
        assert element_is_present(browser, By.CSS_SELECTOR, ".is-success"), "Нет элемента об успехе"
        assert element_text(By.CSS_SELECTOR, ".is-success") == "Верно", \
            f'Написано другое: {browser.find_element(By.CSS_SELECTOR, ".is-success").text}'


def test_my_pet_positiv():
    """Авторизация,
    Заполнение всех полей для ввода произвольным текстом,
    Проверка наличия элемента и сообщения об успехе"""
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/my_pet")
        login(browser)
        inputs = browser.find_elements(By.CSS_SELECTOR, ".input")
        for inp in inputs:
            inp.send_keys("qwerty")

        browser.find_element(By.CSS_SELECTOR, ".button").click()

        assert element_is_present(browser, By.CSS_SELECTOR, ".is-success"), "Нет элемента об успехе"

        assert element_text(browser, By.CSS_SELECTOR, ".is-success") == "Успех.", \
            f'Написано другое: {browser.find_element(By.CSS_SELECTOR, ".is-success").text}'


def test_my_pet_negativ():
    """Авторизация,
    Заполнение первого поля для ввода произвольным текстом,
    Проверка наличия элемента и сообщения об ошибке,
    Проверка отсутствия сообщения об успехе"""
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/my_pet")
        login(browser)
        browser.find_element(By.CSS_SELECTOR, ".input").send_keys("qwerty")

        browser.find_element(By.CSS_SELECTOR, ".button").click()

        assert element_is_present(browser, By.CSS_SELECTOR, ".is-danger"), "Нет элемента об ошибке"

        assert element_text(browser, By.CSS_SELECTOR, ".is-danger") == "Заполнены не все поля.", \
            f'Написано другое: {browser.find_element(By.CSS_SELECTOR, ".is-danger")}'

        assert not element_text(browser, By.CSS_SELECTOR, ".is-success") == "Успех.", \
            f'Написано другое: {element_text(browser, By.CSS_SELECTOR, ".is-success")}'


def test_check_sidebar_name():
    """Авторизация,
    Проверка корректности наименований в боковом меню"""
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/login")

        login(browser)
        time.sleep(5)
        exp_names = ["Поля ввода и кнопки", "Мой питомец", "О себе", "Загрузка файла", "Ожидание", "Медленная загрузка", "Модальные окна", "Новая вкладка", "iframe", "Drag-and-drop"]

        names = browser.find_elements(By.CSS_SELECTOR, ".menu-list .navbar-item")
        for i in range(len(names)):
            assert names[i].text == exp_names[i], "Наименование не соответствует"