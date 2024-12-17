import os
from selene import browser, by, have


class RegistrationPage:

    def open_browser(self):
        browser.open('/automation-practice-form')
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    def complete_first_name(self, value):
        browser.element('#firstName').type(value)

    def complete_last_name(self, value):
        browser.element('#lastName').type(value)

    def complete_email(self, value):
        browser.element('#userEmail').type(value)

    def complete_mobile(self, value):
        browser.element('#userNumber').type(value)

    def complete_gender(self, value):
        browser.element('#genterWrapper').element(by.text(value)).click()

    def complete_date_of_birth(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.element('.react-datepicker__month-select').click().element(by.text(f"{year}")).click()
        browser.element('.react-datepicker__year-select').click().element(by.text(f"{month}")).click()
        browser.element(by.text(f"{day}")).click()

    def complete_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def complete_hobby(self, value):
        browser.element('#hobbiesWrapper').element(by.text(value)).click()

    def upload_picture(self, path):
        browser.element("#uploadPicture").send_keys(os.path.abspath(f"../resources/file/123.png"))

    def complete_current_address(self, value):
        browser.element('#currentAddress').type(value)

    def complete_state(self, value):
        browser.element('#state').click().element(by.text(value)).click()

    def complete_city(self, value):
        browser.element('#city').click().element(by.text(value)).click()

    def submit_form(self):
        browser.element('#submit').click()


class CheckTable:

    def check_full_name(self, firstName, lastName):
        browser.element('.table-responsive').should(have.text(f'{firstName} {lastName}'))

    def check_userEmail(self, userEmail):
        browser.element('.table-responsive').should(have.text(userEmail))

    def check_gender(self, gender):
        browser.element('.table-responsive').should(have.text(gender))

    def check_userNumber(self, userNumber):
        browser.element('.table-responsive').should(have.text(userNumber))

    def check_date_of_birth(self, day, month, year):
        browser.element('.table-responsive').should(have.text(f'{day} {month},{year}'))

    def check_subjects(self, subjects):
        browser.element('.table-responsive').should(have.text(subjects))

    def check_hobbies(self, hobbies):
        browser.element('.table-responsive').should(have.text(hobbies))

    def check_images(self, images):
        browser.element('.table-responsive').should(have.text(images))

    def check_currentAddress(self, currentAddress):
        browser.element('.table-responsive').should(have.text(currentAddress))

    def check_state_and_city(self, state, city):
        browser.element('.table-responsive').should(have.text(f'{state} {city}'))
