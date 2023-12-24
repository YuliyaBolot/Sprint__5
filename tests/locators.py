from selenium.webdriver.common.by import By

class Locators:

    # Страница сайта
    SITE_PAGE = (By.XPATH, ".//main[@class = 'App_componentContainer__2JC2W']")

    # Логотип Stellar Burgers
    LOGO = (By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2")

    # ЛИЧНЫЙ КАБИНЕТ:

    # Кнопка входа в «Личный кабинет»
    PRIVATE_OFFICE_BUTTON = (By.XPATH, ".//a[@class='AppHeader_header__link__3D_hX']/p[text()='Личный Кабинет']")

    # Страница входа в личный кабинет
    LOGIN_PAGE = (By.XPATH, ".//main//h2[text() = 'Вход']")

    # Страница личного кабинета
    PRIVATE_OFFICE_PAGE = (By.CLASS_NAME, "Profile_profile__3dzvr")

    # Страница восстановления пароля
    RESTORE_PASSWORD_PAGE = (By.XPATH, ".//main//h2[text() = 'Восстановление пароля']")

    # Кнопка «Войти в аккаунт»
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")

    # Кнопка «Войти» для входа в аккаунт
    ENTER_BUTTON = (By.XPATH, ".//form/button[text() = 'Войти']")

    # Кнопка «Выйти» из аккаунта
    EXIT_BUTTON = (By.XPATH, ".//ul[@class = 'Account_list__3KQQf mb-20']//button[text() = 'Выход']")

    # Ссылка «Восстановить пароль»
    RESTORE_PASSWORD_LINK = (By.XPATH, ".//div//a[text() = 'Восстановить пароль']")


    # РЕГИСТРАЦИЯ:

    # Страница регистрации
    REG_PAGE = (By.XPATH, ".//main//h2[text() = 'Регистрация']")

    # Поля ввода для регистрации
    NAME_FIELD = (By.XPATH, ".//label[text()='Имя']/following-sibling::input[@name='name']")
    EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']/following-sibling::input[@name='name']")
    PASSWORD_FIELD = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input[@name='Пароль']")

    # Ссылка «Зарегистрироваться»
    REG_LINK = (By.CLASS_NAME, "Auth_link__1fOlj")

    # Кнопка «Зарегистрироваться»
    REG_BUTTON = (By.XPATH, ".//form//button[text()='Зарегистрироваться']")

    # Сообщение о некорректном пароле
    FAILED_REG_TEXT = (By.XPATH, ".//p[text() = 'Некорректный пароль']")

    # КОНСТРУКТОР:

    # Кнопка «Конструктор»
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//ul[@class = 'AppHeader_header__list__3oKJj']//a[@class = 'AppHeader_header__link__3D_hX']")

    # Кнопка «Булки»
    BUNS = (By.XPATH, ".//div[@style = 'display: flex;']//span[text() = 'Булки']")

    # Список булок
    BUNS_LST = (By.XPATH, ".//h2[text() = 'Булки']/following-sibling::ul[@class = 'BurgerIngredients_ingredients__list__2A-mT']")

    # Кнопка «Соусы»
    SAUCES = (By.XPATH, ".//div[@style = 'display: flex;']//span[text() = 'Соусы']")

    # Список соусов
    SAUCES_LST = (By.XPATH, ".//h2[text() = 'Соусы']/following-sibling::ul[@class = 'BurgerIngredients_ingredients__list__2A-mT']")

    # Кнопка «Начинки»
    FILLINGS = (By.XPATH, ".//div[@style = 'display: flex;']//span[text() = 'Начинки']")

    # Список начинок
    FILLINGS_LST = (By.XPATH, ".//h2[text() = 'Начинки']/following-sibling::ul[@class = 'BurgerIngredients_ingredients__list__2A-mT']")









