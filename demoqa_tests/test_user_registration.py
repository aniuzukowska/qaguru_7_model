from demoqa_tests.model.pages import registration_form


def test_submit_student_details(open_and_quit_browser_automation_practice_form):
    registration_form.set_first_name('Maria')
    registration_form.set_last_name('Sklodowska')
    registration_form.set_email('maria-sklodowska@gmail.com')
    registration_form.set_gender('Female')
    registration_form.set_phone_number('1234567890')
    registration_form.set_date_of_birth([7, 'February', '2000'])
    registration_form.set_subject('Physics')
    registration_form.set_hobby('Music')
    registration_form.set_picture('resources/picture.jpg')
    registration_form.set_address('France, Paris')

    registration_form.scroll_to_bottom()
    registration_form.set_state('Haryana')
    registration_form.set_city('Karnal')

    registration_form.click_submit()

    registration_form.should_have_submitted(
            [
                ('Student Name', 'Maria Sklodowska'),
                ('Student Email', 'maria-sklodowska@gmail.com'),
                ('Gender', 'Female'),
                ('Mobile', '1234567890'),
                ('Date of Birth', '07 February,2000'),
                ('Subjects', 'Physics'),
                ('Hobbies', 'Music'),
                ('Picture', 'picture.jpg'),
                ('Address', 'France, Paris'),
                ('State and City', 'Haryana Karnal')
            ],
        )




