from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://stellarburgers.nomoreparties.site')

# Найти кнопку «Личный кабинет» и кликнуть по ней
driver.find_element(By.XPATH, ".//a[@class='AppHeader_header__link__3D_hX']/p[text()='Личный Кабинет']").click()

# Дождаться загрузки страницы личного кабинета
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))

driver.quit()
