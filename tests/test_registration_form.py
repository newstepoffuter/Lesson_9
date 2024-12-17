from resources.user_data import new_user
from practice_form.registration_page import RegistrationPage, CheckTable


def fill_registration_form(page, user):
    page.complete_first_name(user.first_name)
    page.complete_last_name(user.last_name)
    page.complete_email(user.user_email)
    page.complete_gender(user.gender)
    page.complete_mobile(user.user_number)
    page.complete_date_of_birth(user.month, user.year, user.day)
    page.complete_subject(user.subjects)
    page.complete_hobby(user.hobbies)
    page.upload_picture(user.images)
    page.complete_current_address(user.current_address)
    page.complete_state(user.state)
    page.complete_city(user.city)
    page.submit_form()


def check_user_registration(table, user):
    table.check_full_name(user.first_name, user.last_name)
    table.check_userEmail(user.user_email)
    table.check_gender(user.gender)
    table.check_userNumber(user.user_number)
    table.check_date_of_birth(user.day, user.month, user.year)
    table.check_subjects(user.subjects)
    table.check_hobbies(user.hobbies)
    table.check_images(user.images)
    table.check_currentAddress(user.current_address)
    table.check_state_and_city(user.state, user.city)


def test_registration_new_user(browser_settings):
    registration_page = RegistrationPage()

    registration_page.open_browser()
    fill_registration_form(registration_page, new_user)

    table_responsive = CheckTable()
    check_user_registration(table_responsive, new_user)
