import pytest
from selenium import webdriver
from pages.create_new_customer_account_page import CustomerNewAccount
from pages.login_page import LoginPage
from pages.eco_friendly_page import EcoFriendlyPage
from pages.sale_page import SalePage


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(3)
    yield chrome_driver


@pytest.fixture()
def create_new_account_page_page(driver):
    return CustomerNewAccount(driver)


@pytest.fixture()
def eco_friendly_page(driver):
    return EcoFriendlyPage(driver)


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)


@pytest.fixture()
def logged_in_user(driver):
    account = LoginPage(driver)
    account.open_page()
    account.log_in("Laurence95@yahoo.com", "VShbp3hR3zjTdAy")