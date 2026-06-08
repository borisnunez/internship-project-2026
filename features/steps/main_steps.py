from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given("Open Reely's main page")
def open_main(context):
    context.app.main_page.open_main()