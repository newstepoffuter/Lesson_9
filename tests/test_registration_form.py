from practice_form.registration_page import RegistrationPage, CheckTable
from resources.user_data import new_user


def test_registers_user(browser_settings):
    registration_page = RegistrationPage()
    registration_page.open_browser()
    registration_page.create_new_user(new_user)

    table_responsive = CheckTable()
    table_responsive.check_submited_table(new_user)