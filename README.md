# Sprint__5

В файле locators.py описаны все используемые локаторы в проекте.
В файле conftest.py описаны фикструры.
В файле constants.py описаны используемые константы.

Тесты по регистрации находятся в файле tests_registration.py:

1. Тест по успешной регистрации - test_successful_registration.
2. Тест по ошибке некорректного пароля - test_registration_with_incorrect_password.

Тесты по входу в личный кабинет находятся в файле tests_login_to_account.py:
1. Тест входа по кнопке «Войти в аккаунт» на главной странице - test_login_through_account_button_on_main_page.
2. Тест входа через кнопку «Личный кабинет» - test_login_through_private_office_button.
3. Тест входа через кнопку в форме регистрации - test_login_through_registration_form.
4. Тест входа через кнопку в форме восстановления пароля - test_login_through_regeneration_password_form.

Тесты по работе в личном кабинете находятся в файле tests_work_in_private_account.py:
1. Тест по переходу в личный кабинет - test_move_to_private_account.
2. Тест по переходу из личного кабинета в конструктор - test_move_from_private_account_to_constructor.
3. Тест по переходу из личного кабинета на логотип Stellar Burgers - test_move_from_private_account_to_logo.
4. Тест выхода из аккаунта - test_exit_from_private_account.

Тесты по Конструктору находятся в файле tests_for_section_constructor.py:
1. Тест по переходу к разделу «Булки» - test_for_section_buns.
2. Тест по переходу к разделу «Соусы» - test_for_section_sauces.
3. Тест по переходу к разделу «Начинки» - test_for_section_fillings.

