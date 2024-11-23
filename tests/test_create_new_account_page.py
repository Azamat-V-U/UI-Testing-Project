import pytest
import allure
import creds
from faker import Faker

fake = Faker()


@allure.feature("Create New Customer account page")
@allure.story("Creating a new customer account")
@allure.title("Create a new customer account with valid data")
@pytest.mark.critical
@pytest.mark.smoke
def test_new_user_account_valid_data(create_new_account_page_page):
    create_new_account_page_page.open_page()
    create_new_account_page_page.fill_login_form(
        fake.name(), fake.last_name(), fake.email(), creds.correct_password, creds.correct_password
    )
    create_new_account_page_page.message_verification(
        "Thank you for registering with Main Website Store."
    )


@allure.feature("Create New Customer account page")
@allure.story("Creating a new customer account")
@allure.title("Create a new customer account with an existing email address")
@pytest.mark.medium
@pytest.mark.regression
def test_create_new_user_account_with_existing_data(create_new_account_page_page):
    create_new_account_page_page.open_page()
    create_new_account_page_page.fill_login_form(
        creds.existing_user_name, creds.existing_user_last_name, creds.existing_user_email,
        creds.existing_user_password, creds.existing_user_password
    )
    create_new_account_page_page.message_verification(
        "There is already an account with this email address. "
        "If you are sure that it is your email address, click here to get your password and access your account."
    )


@allure.feature("Create New Customer account page")
@allure.story("Creating a new customer account")
@allure.title("Create a new customer account with an invalid email address")
@pytest.mark.medium
@pytest.mark.extended
def test_create_account_with_incorrect_email(create_new_account_page_page):
    create_new_account_page_page.open_page()
    create_new_account_page_page.fill_login_form(fake.name(), fake.last_name(), creds.invalid_email,
                                                 creds.correct_password, creds.correct_password
                                                 )
    create_new_account_page_page.invalid_email_message_verification(
        "Please enter a valid email address (Ex: johndoe@domain.com)."
    )


@allure.feature("Create New Customer account page")
@allure.story("Creating a new customer account")
@allure.title("Create a new customer account with an invalid password length")
@pytest.mark.medium
@pytest.mark.low
def test_create_account_with_incorrect_email(create_new_account_page_page):
    create_new_account_page_page.open_page()
    create_new_account_page_page.fill_login_form(
        fake.name(), fake.last_name(), fake.email(), creds.invalid_password, creds.invalid_password
    )
    create_new_account_page_page.invalid_password_message_verification(
        "Minimum length of this field must be equal or greater than 8 symbols. "
        "Leading and trailing spaces will be ignored."
    )