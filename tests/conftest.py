import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(Constants.URL)
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.EMAIL_FIELD).send_keys(Constants.TEST_EMAIL)
    driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.TEST_PASSWORD)
    driver.find_element(*Locators.ENTER_BUTTON).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.SITE_PAGE))
    return driver

