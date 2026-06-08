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


@when('The user enters "{password}" in the password field')
def enter_password(context, password):
    context.app.registration_page.enter_password(password)


@when('User enters "{company_website}" in the company website field')
def enter_company_website(context, company_website):
    context.app.registration_page.enter_company_website(company_website)


@then('Verify first and last name field contains "{correct_full_name}"')
def verify_full_name(context, correct_full_name):
    context.app.registration_page.verify_full_name(correct_full_name)


@then('Verify phone number field should contain "{correct_phone_number}"')
def verify_phone_number(context, correct_phone_number):
    context.app.registration_page.verify_phone_number(correct_phone_number)


@then('Verify email field should contain "{correct_email}"')
def verify_email(context, correct_email):
    context.app.registration_page.verify_email(correct_email)


@then('Verify password field should contain "{correct_password}"')
def verify_password(context, correct_password):
    context.app.registration_page.verify_password(correct_password)


@then('Verify company website field should contain "{correct_company_website}"')
def verify_company_website(context, correct_company_website):
    context.app.registration_page.verify_company_website(correct_company_website)