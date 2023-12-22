from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://stellarburgers.nomoreparties.site')

# Найти кнопку «Войти в аккаунт» и кликнуть по ней
driver.find_element(By.XPATH, ".//div[@class = 'BurgerConstructor_basket__container__2fUl3 mt-10']/button[text() = 'Войти в аккаунт']").click()

# Ввести почту и пароль
registration_fields = driver.find_elements(By.XPATH, ".//fieldset[@class = 'Auth_fieldset__1QzWN mb-6']//input[@class = 'text input__textfield text_type_main-default']")

registration_fields[0].send_keys("YuliyaBolotskikh4992@yandex.ru")
registration_fields[1].send_keys("Kotya1")

# Найти кнопку «Войти» и кликнуть по ней
enter_button = driver.find_element(By.XPATH, ".//form[@class = 'Auth_form__3qKeq mb-20']/button[text() = 'Войти']")
enter_button.click()

# Дождаться загрузки главной страницы
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.TAG_NAME, "main")))

# Зайти в «Личный кабинет»
private_office_buttons = driver.find_element(By.XPATH, ".//a[@class='AppHeader_header__link__3D_hX']/p[text()='Личный Кабинет']").click()

# Дождаться загрузки страницы личного кабинета
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Account_account__vgk_w")))

driver.quit()
