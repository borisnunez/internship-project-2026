from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class RegistrationPage(Page):

    # ENTER_FULL_NAME = (By.CSS_SELECTOR, 'input[id="Full-Name"]')
    # ENTER_PHONE_NUMBER = (By.CSS_SELECTOR, 'input[id="phone2"]')
    # ENTER_EMAIL = (By.CSS_SELECTOR, 'input[id="Email-3"]')
    # ENTER_PASSWORD = (By.CSS_SELECTOR, 'input[id="field"]')

    ENTER_FULL_NAME = (By.ID, "Full-Name")
    ENTER_PHONE_NUMBER = (By.ID, "phone2")
    ENTER_EMAIL = (By.ID, "Email-3")
    ENTER_PASSWORD = (By.ID, "field")
    ENTER_COMPANY_WEBSITE = (By.ID, "Company-website")

    def open_registration_page(self):
        self.open_url(end_url='sign-up')

    def enter_full_name(self, full_name:str):
        self.input_text(full_name,*self.ENTER_FULL_NAME)

    def enter_phone_number(self, phone_number:str):
        self.input_text(phone_number,*self.ENTER_PHONE_NUMBER)

    def enter_email(self, email: str):
        self.input_text(email, *self.ENTER_EMAIL)

    def enter_password(self, password:str):
        self.input_text(password, *self.ENTER_PASSWORD)

    def enter_company_website(self, company_website:str):
        self.input_text(company_website, *self.ENTER_COMPANY_WEBSITE)

    def verify_full_name(self, correct_full_name:str):
        self.verify_input_text(correct_full_name,*self.ENTER_FULL_NAME)

    def verify_phone_number(self, correct_phone_number:str):
        self.verify_input_text(correct_phone_number,*self.ENTER_PHONE_NUMBER)

    def verify_email(self, correct_email:str):
        self.verify_input_text(correct_email,*self.ENTER_EMAIL)

    def verify_password(self, correct_password:str):
        self.verify_input_text(correct_password,*self.ENTER_PASSWORD)

    def verify_company_website(self, company_website:str):
        self.verify_input_text(company_website,*self.ENTER_COMPANY_WEBSITE)