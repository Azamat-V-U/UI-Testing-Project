import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.create_new_customer_account_page import CustomerNewAccount
from pages.login_page import LoginPage
from pages.eco_friendly_page import EcoFriendlyPage
from pages.sale_page import SalePage

EMAIL = None
PASSWORD = None


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('--ignore-certificate-errors')
    chrome_driver = webdriver.Chrome(options=options)
    # chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(3)
    yield chrome_driver
    # chrome_driver.save_screenshot(f"{str(random.randint(100, 10000))}.png")


@pytest.fixture()
def create_new_account_page(driver):
    return CustomerNewAccount(driver)


@pytest.fixture()
def eco_friendly_page(driver):
    return EcoFriendlyPage(driver)


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)


@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture()
def logged_in_user(driver):
    account = LoginPage(driver)
    account.open_page()
    # account.accept_cookies()
    account.log_in_valid_data("Christoph@gmail.com", "Wp60_ce#6R")
    account.log_in_valid_data(EMAIL, PASSWORD)
