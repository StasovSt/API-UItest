from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def login(browser):
    browser.find_element(By.NAME, "email").send_keys("qa_test@test.ru")
    browser.find_element(By.NAME, "password").send_keys("!QAZ2wsx")
    browser.find_element(By.CLASS_NAME, "button").click()


def element_is_present(browser, by, value):
    try:
        browser.find_element(by, value)
        return True
    except NoSuchElementException:
        return False


def element_text(browser, by, value):
    try:
        browser.find_element(by, value)
        return browser.find_element(by, value).text
    except NoSuchElementException:
        return None
