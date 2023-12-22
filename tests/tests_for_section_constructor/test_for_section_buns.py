from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://stellarburgers.nomoreparties.site')

# Дождаться загрузки страницы Конструктора
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "BurgerIngredients_ingredients__1N8v2")))

# Найти кнопку «Начинки» и кликнуть по ней
driver.find_element(By.XPATH, ".//div[@style = 'display: flex;']//span[text() = 'Начинки']").click()

# Прокрутить страницу до начинок
burger_ingredients = driver.find_elements(By.XPATH, ".//div[@class = 'BurgerIngredients_ingredients__menuContainer__Xu3Mo']/ul[@class = 'BurgerIngredients_ingredients__list__2A-mT']")
driver.execute_script("arguments[0].scrollIntoView();", burger_ingredients[2])

# Найти кнопку «Булки» и кликнуть по ней
driver.find_element(By.XPATH, ".//div[@style = 'display: flex;']/div[@class = 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']").click()

# Прокрутить страницу до булок
burger_ingredients = driver.find_elements(By.XPATH, ".//div[@class = 'BurgerIngredients_ingredients__menuContainer__Xu3Mo']/ul[@class = 'BurgerIngredients_ingredients__list__2A-mT']")
driver.execute_script("arguments[0].scrollIntoView();", burger_ingredients[0])

driver.quit()
