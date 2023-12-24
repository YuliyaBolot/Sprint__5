from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators

class Test:
    def test_move_to_private_account(self, login):
        login.find_element(*Locators.PRIVATE_OFFICE_BUTTON).click()
        WebDriverWait(login, 10).until(expected_conditions.visibility_of_element_located(Locators.PRIVATE_OFFICE_PAGE))
        assert login.current_url == Constants.URL_PROFILE

    def test_exit_from_private_account(self, login):
        login.find_element(*Locators.PRIVATE_OFFICE_BUTTON).click()
        WebDriverWait(login, 10).until(expected_conditions.visibility_of_element_located(Locators.PRIVATE_OFFICE_PAGE))
        login.find_element(*Locators.EXIT_BUTTON).click()
        WebDriverWait(login, 10).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_PAGE))
        assert login.current_url == Constants.URL_LOGIN

    def test_move_from_private_account_to_constructor(self, login):
        login.find_element(*Locators.PRIVATE_OFFICE_BUTTON).click()
        WebDriverWait(login, 10).until(expected_conditions.visibility_of_element_located(Locators.PRIVATE_OFFICE_PAGE))
        login.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(login, 10).until(expected_conditions.visibility_of_element_located(Locators.SITE_PAGE))
        assert login.current_url == Constants.URL

    def test_move_from_private_account_to_logo(self, login):
        login.find_element(*Locators.PRIVATE_OFFICE_BUTTON).click()
        WebDriverWait(login, 10).until(expected_conditions.visibility_of_element_located(Locators.PRIVATE_OFFICE_PAGE))
        login.find_element(*Locators.LOGO).click()
        WebDriverWait(login, 10).until(expected_conditions.visibility_of_element_located(Locators.SITE_PAGE))
        assert login.current_url == Constants.URL










