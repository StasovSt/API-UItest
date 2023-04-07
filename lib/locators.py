from selenium.webdriver.common.by import By

class AuthLocators:
    EMAIL_ELEMENT = (By.NAME, "email")
    PASSWORD_ELEMENT = (By.NAME, "password")
    BUTTON_ENTRY = (By.CLASS_NAME, "button")
    REMEMBER_ME_CHECKBOX = (By.CSS_SELECTOR, '[type="checkbox"]')
