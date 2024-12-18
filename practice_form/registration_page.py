import os
from selene import browser, by, have
from selene.support.conditions import be


class RegistrationPage:

    def open_browser(self):
        browser.open('/automation-practice-form')
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    def create_new_user(self, User):
        browser.element('#firstName').should(be.visible).type(User.first_name)
        browser.element('#lastName').should(be.visible).type(User.last_name)
        browser.element('#userEmail').should(be.visible).type(User.user_email)
        browser.element('#userNumber').should(be.visible).type(User.user_number)
        gender_element = browser.element('#genterWrapper').element(by.text(User.gender))
        gender_element.should(be.visible).click()
        browser.element("#dateOfBirthInput").click()
        browser.element('.react-datepicker__month-select').should(be.visible).click()
        browser.element(by.text(User.month)).should(be.visible).click()
        browser.element('.react-datepicker__year-select').should(be.visible).click()
        browser.element(by.text(User.year)).should(be.visible).click()
        browser.element(by.text(User.day)).should(be.visible).click()
        browser.element('#subjectsInput').should(be.visible).type(User.subjects).press_enter()
        browser.element('#hobbiesWrapper').element(by.text(User.hobbies)).should(be.visible).click()
        browser.element("#uploadPicture").send_keys(os.path.abspath(f"../resources/file/123.png"))
        browser.element('#currentAddress').should(be.visible).type(User.current_address)
        browser.element('#state').click()
        browser.element(by.text(User.state)).should(be.visible).click()
        browser.element('#city').click()
        browser.element(by.text(User.city)).should(be.visible).click()
        browser.element('#submit').click()


class CheckTable:

    def check_submited_table(self, User):
        browser.element('.table-responsive').should(have.text(f'{User.first_name} {User.last_name}'))
        browser.element('.table-responsive').should(have.text(User.user_email))
        browser.element('.table-responsive').should(have.text(User.gender))
        browser.element('.table-responsive').should(have.text(User.user_number))
        browser.element('.table-responsive').should(have.text(f'{User.day} {User.month},{User.year}'))
        browser.element('.table-responsive').should(have.text(User.subjects))
        browser.element('.table-responsive').should(have.text(User.hobbies))
        browser.element('.table-responsive').should(have.text(User.images))
        browser.element('.table-responsive').should(have.text(User.current_address))
        browser.element('.table-responsive').should(have.text(f'{User.state} {User.city}'))
