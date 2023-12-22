import random

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

# Ввести данные для регистрации
registration_fields = driver.find_elements(By.XPATH, ".//fieldset[@class = 'Auth_fieldset__1QzWN mb-6']//input[@class = 'text input__textfield text_type_main-default']")

new_login = f"YuliaBolotskikh4{random.randint(100, 999)}@yandex.ru"

new_password = f"{random.randint(0, 99999)}"

registration_fields[0].send_keys("Юлия")
registration_fields[1].send_keys(new_login)

# Ввести пароль меньше 6 символов
try:
    registration_fields[2].send_keys(new_password)
    registration_button = driver.find_element(By.XPATH, ".//form//button[text()='Зарегистрироваться']")
    registration_button.click()
    raise Exception('Некорректный пароль. Минимальный пароль — шесть символов.')
except Exception as e:
    print(e)

driver.quit()
