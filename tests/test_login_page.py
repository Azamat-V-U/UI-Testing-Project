import pytest
import allure
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


@allure.feature("Login page")
@allure.story("Login page functionality verification")
@allure.title("Login with valid credentials")
@pytest.mark.critical
@pytest.mark.smoke
def test_login_with_valid_data(login_page):
    login_page.open_page()
    # login_page.accept_cookies()
    login_page.log_in_valid_data(EMAIL, PASSWORD)
