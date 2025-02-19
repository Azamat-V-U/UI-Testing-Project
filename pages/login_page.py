import allure
from pages.base_page import BasePage
from pages.locators import base_locators as loc


class LoginPage(BasePage):
    page_url = "/customer/account"

    @allure.step("Login with valid credentials")
    def log_in_valid_data(self, email, password):
        self.driver.execute_script("window.scrollBy(0, 700);")
        email_field = self.find(loc.email_field_loc)
        password_field = self.find(loc.password_field_loc)
        sign_in_button = self.find(loc.sign_in_button_loc)
        email_field.send_keys(email)
        password_field.send_keys(password)
        sign_in_button.click()

    @allure.step("Login with invalid credentials")
    def log_in_invalid_data(self, email, password):
        self.driver.execute_script("window.scrollBy(0, 700);")
        email_field = self.find(loc.email_field_loc)
        password_field = self.find(loc.password_field_loc)
        sign_in_button = self.find(loc.sign_in_button_loc)
        email_field.send_keys(email)
        password_field.send_keys(password)
        sign_in_button.click()
