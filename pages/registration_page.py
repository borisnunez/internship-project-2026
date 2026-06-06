import driver
from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class RegistrationPage(Page):

    ENTER_FULL_NAME = (By.CSS_SELECTOR, 'input[id="Full-Name"]')
    ENTER_PHONE_NUMBER = (By.CSS_SELECTOR, 'input[id="phone2"]')
    ENTER_EMAIL = (By.CSS_SELECTOR, 'input[id="Email-3"]')

    def open_registration_page(self):
        self.driver.get('https://soft.reelly.io/sign-up')
        #self.open_url(end_url='sign-up')


    def enter_full_name(self, full_name:str):
        self.input_text(full_name,*self.ENTER_FULL_NAME)
        #sleep(2)

    def enter_phone_number(self, phone_number:str):
        self.input_text(phone_number,*self.ENTER_PHONE_NUMBER)

    def enter_email(self, email: str):
        self.input_text(email, *self.ENTER_EMAIL)

    def verify_full_name(self, correct_full_name:str):
        self.verify_input_text(correct_full_name,*self.ENTER_FULL_NAME)

    def verify_phone_number(self, correct_phone_number:str):
        self.verify_input_text(correct_phone_number,*self.ENTER_PHONE_NUMBER)

    def verify_email(self, correct_email:str):
        self.verify_input_text(correct_email,*self.ENTER_EMAIL)