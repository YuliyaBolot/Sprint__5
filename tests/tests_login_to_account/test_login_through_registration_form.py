from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://stellarburgers.nomoreparties.site')

# Найти кнопку «Войти в аккаунт» и кликнуть по ней
driver.find_element(By.XPATH, ".//div[@class = 'BurgerConstructor_basket__container__2fUl3 mt-10']/button[text() = 'Войти в аккаунт']").click()

# Найти ссылку "Зарегистрироваться" и кликнуть по ней
driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click()

# Дождаться повления формы регистрации
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//main//form[@class = 'Auth_form__3qKeq mb-20']")))

driver.quit()

