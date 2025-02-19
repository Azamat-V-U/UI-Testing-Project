import pytest
import allure


@allure.feature("Login page")
@allure.story("Login page functionality verification")
@allure.title("Login with valid credentials")
@pytest.mark.critical
@pytest.mark.smoke
def test_login_with_valid_data(login_page):
    login_page.open_page()
    # login_page.accept_cookies()
    login_page.log_in_valid_data("Christoph1@gmail.com", "Wp60_ce#9!")
