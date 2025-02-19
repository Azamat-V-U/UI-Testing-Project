import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
from utils import expected_conditions
from pages.base_page import BasePage
from pages.locators import eco_friendly_locators as loc
from utils import expected_conditions


class EcoFriendlyPage(BasePage):
    page_url = "/collections/eco-friendly.html"
    items_amount = None
    selected_items_amount = None
    item_details = None
    cart_item_details = None
    pop_up_button = None

    @allure.step("Add the first product on the page item to the compare products list")
    def add_item_to_compare_list(self):
        try:
            wait = WebDriverWait(self.driver, 15, poll_frequency=1)
            selected_item = self.find(loc.selected_item_link_loc)
            self.driver.execute_script("window.scrollBy(0, 700);")
            actions = ActionChains(self.driver)
            add_to_compare_btn = wait.until(EC.presence_of_element_located(
                loc.add_to_compare_loc
            ))
            actions.move_to_element(selected_item)
            actions.move_to_element(add_to_compare_btn)
            actions.perform()
            add_to_compare_btn.click()
        except TimeoutException as e:
            print(f"TimeoutException occurred: {str(e)}")

    @allure.step("Select a size, color and add the product item to the products cart")
    def add_item_to_cart(self):
        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        item_name = wait.until(EC.presence_of_element_located(loc.item_name_loc))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", item_name)
        actions = ActionChains(self.driver)
        add_button = wait.until(EC.presence_of_element_located(loc.item_add_to_cart_loc))
        item_price = self.find(loc.item_price_loc)
        item_size = wait.until(EC.presence_of_element_located(
            loc.item_size_loc
        ))
        item_color = self.find(loc.item_color_loc)
        self.item_details = {
            "name": item_name.text,
            "price": item_price.text,
            "size": item_size.text,
            "color": item_color.get_attribute("option-label")
        }
        print(self.item_details)
        actions.move_to_element(item_name)
        actions.click(item_size)
        actions.click(item_color)
        actions.move_to_element(add_button)
        actions.perform()
        add_button.click()

    @allure.step("Check and delete item from the  products cart")
    def check_item_details_in_cart(self):
        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        # time.sleep(3)
        # wait.until(expected_conditions.text_is_not_empty_in_element(
        #     loc.counter_link_loc
        # ))
        # cart_icon = wait.until(
        #     EC.text_to_be_present_in_element_value(loc.counter_link_loc, "1")
        # )
        cart_icon = wait.until(
            EC.element_to_be_clickable(loc.counter_link_loc)
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(cart_icon).click().perform()
        item_cart_toggle = self.find(loc.item_see_details_loc)
        item_cart_toggle.click()
        item_cart_price = self.find(loc.item_cart_price_loc)
        item_cart_name = self.find(loc.item_cart_link_loc)
        item_cart_size = self.find(loc.item_cart_size_loc)
        item_cart_color = self.find(loc.item_cart_color_loc)
        item_cart_amount = self.find(loc.item_amount_loc)

        self.cart_item_details = {
            "name": item_cart_name.text,
            "price": item_cart_price.text,
            "size": item_cart_size.text,
            "color": item_cart_color.text,
            "amount": item_cart_amount.text
        }
        print(self.cart_item_details)

    @allure.step("Filter products by prise")
    def filter_items_by_price(self):
        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        dropdown_button = wait.until(EC.element_to_be_clickable(
            loc.price_dropdown_loc
        ))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", dropdown_button)
        price_link = self.find(loc.price_link_loc)
        actions = ActionChains(self.driver)
        actions.move_to_element(dropdown_button)
        actions.click(dropdown_button)
        actions.perform()
        parent_element = wait.until(EC.presence_of_element_located(
            loc.price_range_loc
        ))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", parent_element)
        full_text = parent_element.text
        child_element = parent_element.find_element(*loc.price_range_child_loc)
        child_text = child_element.text
        items_amount = full_text.replace(child_text, '').strip()
        self.items_amount = int(items_amount)
        price_link.click()
        wait.until(EC.presence_of_element_located(
            loc.items_list_loc
        ))
        selected_items = self.find_elements(loc.selected_items_loc)
        self.selected_items_amount = len(selected_items)

    @allure.step("Check if the number of products matches to the selected ones")
    def filtered_items_number_verification(self):
        items_amount = self.items_amount
        selected_items = self.selected_items_amount
        assert selected_items == items_amount, \
            f"Expected {items_amount} items, but found {selected_items}"

    @allure.step("Check that the added item matches the item in the shopping cart")
    def added_item_verification(self):
        selected_items = self.item_details
        items_in_cart = self.cart_item_details
        for key in selected_items:
            assert selected_items[key] == items_in_cart[key], f"{key} mismatch: {selected_items[key]} != {items_in_cart[key]}"

    @allure.step("Make sure that the added product item is in the compare products list")
    def compare_products_list_verification(self):
        try:
            self.driver.execute_script("window.scrollBy(0, 700);")
            wait = WebDriverWait(self.driver, 15, poll_frequency=1)
            selected_item = wait.until(EC.presence_of_element_located(
                loc.selected_item_link_loc
            ))
            added_item = wait.until(EC.presence_of_element_located(
                loc.added_item_link_loc
            ))
            assert selected_item.text == added_item.text, f"Selected item: {selected_item.text} != {added_item.text}"
        except TimeoutException as e:
            print(f"TimeoutException occurred: {str(e)}")

    @allure.step("Check that the response message matches the expected one")
    def no_items_message_verification(self, text):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.text_is_not_empty_in_element(loc.item_deleted_message)
        )
        error_message = self.find(loc.item_deleted_message)
        print(error_message.text)
        assert error_message.text == text, f"The text message doesn't match: {text} != {error_message.text}"
