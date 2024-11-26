import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import MoveTargetOutOfBoundsException
from pages.locators import login_creation_locators as loc
from pages.locators import base_locators as lc
from utils import expected_conditions


class BasePage:
    base_url = "https://magento.softwaretestingboard.com"
    page_url = None
    pop_up_button = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step("Open the webpage")
    def open_page(self):
        if self.page_url:
            self.driver.get(f"{self.base_url}{self.page_url}")
        else:
            raise NotImplementedError("Page can not be opened for this url")

    # def find(self, locator: tuple):
    #     return self.driver.find_element(*locator)

    def find(self, locator: tuple, wait=False, timeout=10):
        if wait:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(*locator))
        return self.driver.find_element(*locator)

    def find_elements(self, locator: tuple):
        return self.driver.find_elements(*locator)

    @allure.step("Check that the response message matches the expected one")
    def message_verification(self, text):
        self.driver.execute_script("window.scrollBy(0, 700);")
        WebDriverWait(self.driver, 10).until(
            expected_conditions.text_is_not_empty_in_element(loc.text_message)
        )
        message = self.find(loc.text_message)
        print(message.text)
        assert message.text == text, f"The text message doesn't match: {text} != {message.text}"

    @allure.step("Delete the added product item from the compare products list")
    def delete_item_from_compare_list(self):
        try:
            self.driver.execute_script("window.scrollBy(0, 700);")
            wait = WebDriverWait(self.driver, 15, poll_frequency=1)
            item = wait.until(EC.element_to_be_clickable(lc.remove_item_loc))
            item.click()
            self.pop_up_button = wait.until(EC.presence_of_element_located(
                lc.pop_up_ok_button_loc
            ))
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});", self.pop_up_button
            )

            wait.until(EC.element_to_be_clickable(lc.pop_up_ok_button_loc))
            self.driver.execute_script("arguments[0].click();", self.pop_up_button)
        except MoveTargetOutOfBoundsException:
            print("Move target out of bounds. Trying alternative interaction methods.")
            self.driver.execute_script("arguments[0].click();", self.pop_up_button)

    @allure.step("Delete the item from the cart")
    def delete_item_from_cart(self):
        try:
            wait = WebDriverWait(self.driver, 10, poll_frequency=1)
            delete_icon = self.find(lc.delete_item_icon_loc)
            delete_icon.click()
            pop_up_button = wait.until(EC.presence_of_element_located(
                lc.pop_up_ok_button_loc
            ))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", pop_up_button)
            wait.until(EC.element_to_be_clickable(lc.pop_up_ok_button_loc))
            self.driver.execute_script("arguments[0].click();", pop_up_button)
        except MoveTargetOutOfBoundsException:
            print("Move target out of bounds. Trying alternative interaction methods.")
            self.driver.execute_script("arguments[0].click();", self.pop_up_button)
