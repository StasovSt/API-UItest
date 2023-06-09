import pytest
from selenium.webdriver import Chrome


@pytest.fixture()
def browser():
    """Вызывается объект класса Chrome (открывается браузер)"""
    browser = Chrome()
    yield browser
    browser.quit()



def pytest_configure(config):
    """Регристрация маркеров для запуска отмаркированных тестов"""
    config.addinivalue_line(
        "markers", "smoke: tests for smoke testing"
    )
    config.addinivalue_line(
        "markers", "auth: tests for authorization testing"
    )

