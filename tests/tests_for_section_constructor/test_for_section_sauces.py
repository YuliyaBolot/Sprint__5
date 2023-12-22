from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://stellarburgers.nomoreparties.site')

# Дождаться загрузки страницы Конструктора
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "BurgerIngredients_ingredients__1N8v2")))

# Найти кнопку «Соусы» и кликнуть по ней
driver.find_element(By.XPATH, ".//div[@style = 'display: flex;']//span[text() = 'Соусы']").click()

# Прокрутить страницу до соусов
burger_ingredients = driver.find_elements(By.XPATH, ".//div[@class = 'BurgerIngredients_ingredients__menuContainer__Xu3Mo']/ul[@class = 'BurgerIngredients_ingredients__list__2A-mT']")
driver.execute_script("arguments[0].scrollIntoView();", burger_ingredients[1])

driver.quit()
