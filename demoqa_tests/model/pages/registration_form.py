from selene import command
from selene.support.conditions import have
from selene.support.shared.jquery_style import s

import files
from demoqa_tests.model.controls import dropdown, date_controls


def set_first_name(first_name):
    s('#firstName').type(first_name)


def set_last_name(last_name):
    s('#lastName').type(last_name)


def set_email(email):
    s('#userEmail').type(email)


def set_gender(gender):
    if gender == 'Male':
        s('.custom-control-label[for="gender-radio-1"]').click()
    elif gender == 'Female':
        s('.custom-control-label[for="gender-radio-2"]').click()
    elif gender == 'Other':
        s('.custom-control-label[for="gender-radio-3"]').click()


def set_phone_number(number):
    s('#userNumber').type(number)


def set_date_of_birth(date):
    s('#dateOfBirthInput').click()
    date_controls.select_month(date[1])
    date_controls.select_year(date[2])
    date_controls.select_day(date[1], date[0])


def set_subject(value):
    s('#subjectsInput').type(value).press_enter()


def set_hobby(hobby):
    if hobby == 'Sports':
        s('.custom-control-label[for="hobbies-checkbox-1"]').click()
    elif hobby == 'Reading':
        s('.custom-control-label[for="hobbies-checkbox-2"]').click()
    elif hobby == 'Music':
        s('.custom-control-label[for="hobbies-checkbox-3"]').click()


def set_picture(path):
    s('#uploadPicture').send_keys(files.abs_path_from_project_root(path))


def set_address(address):
    s('#currentAddress').type(address)


def set_state(value: str):
    dropdown.select(s('#state'), value)


def set_city(value: str):
    dropdown.select(s('#city'), value)


def click_submit():
    s('#submit').perform(command.js.click)


def scroll_to_bottom():
    s('#state').perform(command.js.scroll_into_view)


def should_have_submitted(data):
    rows = s('.modal-content').all('tbody tr')
    for row, value in data:
        rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))









