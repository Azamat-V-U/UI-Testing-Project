import pytest
import allure
from faker import Faker

fake = Faker()


@allure.feature("Create New Customer account page")
@allure.story("Creating a new customer account")
@allure.title("Create a new customer account with valid data")
@pytest.mark.critical
@pytest.mark.smoke
def test_new_user_account_valid_data(create_new_account_page):
    create_new_account_page.open_page()
    create_new_account_page.fill_login_form(
        fake.name(), fake.last_name(), fake.email(), "Wp60_ce#9!", "Wp60_ce#9!"
    )
    create_new_account_page.message_verification(
        "Thank you for registering with Main Website Store."
    )


@allure.feature("Create New Customer account page")
@allure.story("Creating a new customer account")
@allure.title("Create a new customer account with an existing email address")
@pytest.mark.medium
@pytest.mark.regression
def test_create_new_user_account_existing_data(create_new_account_page):
    create_new_account_page.open_page()
    create_new_account_page.fill_login_form(
        "Skyla", "Kemmer", "Laurence95@yahoo.com",
        "VShbp3hR3zjTdAy", "VShbp3hR3zjTdAy"
    )
    create_new_account_page.message_verification(
        "There is already an account with this email address. "
        "If you are sure that it is your email address, click here to get your password and access your account."
    )


@allure.feature("Create New Customer account page")
@allure.story("Creating a new customer account")
@allure.title("Create a new customer account with an invalid email address")
@pytest.mark.medium
@pytest.mark.regression
def test_create_account_incorrect_email(create_new_account_page):
    create_new_account_page.open_page()
    create_new_account_page.fill_login_form(fake.name(), fake.last_name(), "Christoph1gmail.com",
                                            "Wp60_ce#9!", "Wp60_ce#9!"
                                            )
    create_new_account_page.invalid_email_message_verification(
        "Please enter a valid email address (Ex: johndoe@domain.com)."
    )


@allure.feature("Create New Customer account page")
@allure.story("Creating a new customer account")
@allure.title("Create a new customer account with an invalid password length")
@pytest.mark.low
@pytest.mark.regression
def test_create_account_incorrect_password(create_new_account_page):
    create_new_account_page.open_page()
    create_new_account_page.fill_login_form(
        fake.name(), fake.last_name(), fake.email(), "SLcef", "SLcef"
    )
    create_new_account_page.invalid_password_message_verification(
        "Minimum length of this field must be equal or greater than 8 symbols. "
        "Leading and trailing spaces will be ignored."
    )


@allure.feature("Create New Customer account page")
@allure.story("Creating a new customer account")
@allure.title("Create a new customer account with an incorrect password confirmation data")
@pytest.mark.medium
@pytest.mark.regression
def test_create_account_incorrect_password_confirmation_data(create_new_account_page):
    create_new_account_page.open_page()
    create_new_account_page.fill_login_form(
        fake.name(), fake.last_name(), fake.email(), "Wp60_ce#9!", "Wp60_ce#9!Tvo"
    )
    create_new_account_page.invalid_password_confirmation_message_verification(
        "Please enter the same value again."
    )


@allure.feature("Create New Customer account page")
@allure.story("Creating a new customer account")
@allure.title("Create a new customer account with empty first name field")
@pytest.mark.medium
@pytest.mark.extended
def test_create_account_empty_first_name_field(create_new_account_page):
    create_new_account_page.open_page()
    create_new_account_page.fill_login_form(
        "", fake.last_name(), fake.email(), "Wp60_ce#9!", "Wp60_ce#9!"
    )
    create_new_account_page.first_last_name_required_field_message_verification(
        "This is a required field."
    )


@allure.feature("Create New Customer account page")
@allure.story("Creating a new customer account")
@allure.title("Create a new customer account with empty last name field")
@pytest.mark.medium
@pytest.mark.extended
def test_create_account_empty_first_name_field(create_new_account_page):
    create_new_account_page.open_page()
    create_new_account_page.fill_login_form(
        fake.name(), "", fake.email(), "Wp60_ce#9!", "Wp60_ce#9!"
    )
    create_new_account_page.first_last_name_required_field_message_verification(
        "This is a required field."
    )
