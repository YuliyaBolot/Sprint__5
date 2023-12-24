from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators

class Test:
    def test_login_through_account_button_on_main_page(self, driver):
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_PAGE))
        assert driver.current_url == Constants.URL_LOGIN

    def test_login_through_private_office_button(self, driver):
        driver.find_element(*Locators.PRIVATE_OFFICE_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_PAGE))
        assert driver.current_url == Constants.URL_LOGIN

    def test_login_through_regeneration_password_form(self, driver):
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_PAGE))
        driver.find_element(*Locators.RESTORE_PASSWORD_LINK).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.RESTORE_PASSWORD_PAGE))
        assert driver.current_url == Constants.URL_RESTORE_PASSWORD

    def test_login_through_registration_form(self, driver):
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_PAGE))
        driver.find_element(*Locators.REG_LINK).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.REG_PAGE))
        assert driver.current_url == Constants.URL_REG



