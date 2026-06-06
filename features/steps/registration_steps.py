from behave import given, when, then


@given('Open the registration page')
def open_registration_page(context):
    context.app.registration_page.open_registration_page()


@when('The user enters "{full_name}" in the First and Last Name field')
def enter_full_name(context, full_name):
    context.app.registration_page.enter_full_name(full_name)


@when('User enters "{phone_number}" in the phone number field')
def enter_phone_number(context, phone_number):
    context.app.registration_page.enter_phone_number(phone_number)


@when('The user enters "{email}" in the email field')
def enter_email(context, email):
    context.app.registration_page.enter_email(email)


@then('Verify first and last name field contains "{correct_full_name}"')
def verify_full_name(context, correct_full_name):
    context.app.registration_page.verify_full_name(correct_full_name)


@then('Verify phone number field should contain "{correct_phone_number}"')
def verify_phone_number(context, correct_phone_number):
    context.app.registration_page.verify_phone_number(correct_phone_number)


@then('Verify email field should contain "{correct_email}"')
def verify_email(context, correct_email):
    context.app.registration_page.verify_email(correct_email)