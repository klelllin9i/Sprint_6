import pytest
from selenium import webdriver

BASE_URL = "https://qa-scooter.praktikum-services.ru/"

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()