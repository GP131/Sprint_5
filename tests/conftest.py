import pytest

from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()

@pytest.fixture
def credentials():
    return {
        "email": "georgypomytkin13987@yandex.ru",
        "password": "1234567"
    }

