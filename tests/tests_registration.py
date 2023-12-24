import random

from faker import Faker
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators

faker = Faker()

class TestRegistration:
    def test_successful_registration(self, driver):
        name = faker.name()
        email = faker.email()
        password = f"{random.randint(100000, 1000000)}"
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REG_LINK).click()
        driver.find_element(*Locators.NAME_FIELD).send_keys(name)
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*Locators.REG_BUTTON).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.LOGIN_PAGE))
        assert driver.current_url == Constants.URL_LOGIN

    def test_registration_with_incorrect_password(self, driver):
        name = faker.name()
        email = faker.email()
        password = f"{random.randint(0, 99999)}"
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REG_LINK).click()
        driver.find_element(*Locators.NAME_FIELD).send_keys(name)
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*Locators.REG_BUTTON).click()
        failed_text = WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.FAILED_REG_TEXT)).text
        assert failed_text == "Некорректный пароль"


