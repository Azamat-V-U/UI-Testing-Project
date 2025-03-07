import allure
from pages.base_page import BasePage
from pages.locators import login_creation_locators as loc


class CustomerNewAccount(BasePage):

    page_url = "/customer/account/create/"

    @allure.step("Fill the login form")
    def fill_login_form(self, name, surname, email, password, password_confirmation):
        self.driver.execute_script("window.scrollBy(0, 800);")
        first_name = self.find(loc.first_name_loc)
        last_name = self.find(loc.last_name_loc)
        email_field = self.find(loc.email_field_loc)
        password_field = self.find(loc.password_field_loc)
        password_confirm_field = self.find(loc.password_confirmation_field_loc)
        create_account_button = self.find(loc.submit_button_loc)
        first_name.send_keys(name)
        last_name.send_keys(surname)
        email_field.send_keys(email)
        password_field.send_keys(password)
        password_confirm_field.send_keys(password_confirmation)
        create_account_button.click()

    @allure.step("Check that the reply message matches the expected one")
    def invalid_email_message_verification(self, text):
        error_message = self.find(loc.invalid_email_message_loc)
        print(error_message.text)
        assert error_message.text == text

    def invalid_password_message_verification(self, text):
        error_message = self.find(loc.invalid_password_message_loc)
        print(error_message.text)
        assert error_message.text == text

    def invalid_password_confirmation_message_verification(self, text):
        error_message = self.find(loc.invalid_password_confirmation_message_loc)
        print(error_message.text)
        assert error_message.text == text

    def first_last_name_required_field_message_verification(self, text):
        first_name_message = None
        last_name_message = None

        try:
            first_name_message = self.find(loc.first_name_required_field_message_loc, wait=True)
        except:
            pass

        try:
            last_name_message = self.find(loc.last_name_required_field_message_loc, wait=True)
        except:
            pass

        if first_name_message and first_name_message.is_displayed():
            assert first_name_message.text == text, "First name error message does not match"
        elif last_name_message and last_name_message.is_displayed():
            assert last_name_message.text == text, "Last name error message does not match"
        else:
            raise AssertionError("Neither first name nor last name error messages were found.")
