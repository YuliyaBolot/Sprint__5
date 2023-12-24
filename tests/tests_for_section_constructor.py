from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators

class Test:
    def test_for_section_buns(self, driver):
        driver.find_element(*Locators.BUNS).click()
        buns_lst = driver.find_element(*Locators.BUNS_LST)
        driver.execute_script("arguments[0].scrollIntoView();", buns_lst)
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.BUNS_LST))

    def test_for_section_sauces(self, driver):
        driver.find_element(*Locators.SAUCES).click()
        sauces_lst = driver.find_element(*Locators.SAUCES_LST)
        driver.execute_script("arguments[0].scrollIntoView();", sauces_lst)
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.SAUCES_LST))

    def test_for_section_fillings(self, driver):
        driver.find_element(*Locators.FILLINGS).click()
        fillings_lst = driver.find_element(*Locators.FILLINGS_LST)
        driver.execute_script("arguments[0].scrollIntoView();", fillings_lst)
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.FILLINGS_LST))


