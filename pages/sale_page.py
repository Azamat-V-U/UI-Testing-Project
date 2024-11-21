import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import sale_page_locators as loc


class SalePage(BasePage):
    page_url = "/sale.html"
    item_details = None
    link_names_list = None
    page_titles_list = None

    @allure.step("Add item to the products compare list in another tab")
    def add_item_to_compare_list_in_another_tab(self):
        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        selected_items = wait.until(EC.element_to_be_clickable(
           loc.hoodies_and_sweatshirts_link_loc
        ))
        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL).click(selected_items).key_up(Keys.CONTROL).perform()
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        selected_item = wait.until(EC.presence_of_element_located(
            loc.item_link_loc
        ))
        add_to_compare_btn = wait.until(EC.presence_of_element_located(
            loc.add_to_compare_loc
        ))
        actions.move_to_element(selected_item)
        actions.move_to_element(add_to_compare_btn)
        actions.perform()
        add_to_compare_btn.click()
        self.driver.close()
        self.driver.switch_to.window(handles[0])
        self.driver.refresh()

    @allure.step("Select and add item to the shopping cart in another tab")
    def add_product_to_cart(self):
        self.driver.execute_script("window.scrollBy(0, 500);")
        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        selected_items = wait.until(EC.element_to_be_clickable(
            loc.selected_item_loc
        ))
        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL).click(selected_items).key_up(Keys.CONTROL).perform()
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        selected_item = wait.until(EC.presence_of_element_located(loc.item_element_loc))
        actions = ActionChains(self.driver)
        add_button = wait.until(EC.presence_of_element_located(loc.item_add_to_cart_loc))
        item_price = self.find(loc.item_price_loc)
        item_size = wait.until(EC.presence_of_element_located(
            loc.item_size_loc
        ))
        item_color = wait.until(EC.presence_of_element_located(
            loc.item_color_loc
        ))
        self.item_details = {
            "name": selected_item.text,
            "price": item_price.text,
            "size": item_size.text,
            "color": item_color.get_attribute("option-label")
        }
        actions.move_to_element(selected_item)
        actions.click(item_size)
        actions.click(item_color)
        actions.move_to_element(add_button)
        actions.perform()
        add_button.click()
        self.driver.close()
        self.driver.switch_to.window(handles[0])
        self.driver.refresh()
        print(self.item_details)

    @allure.step("Open 'Mens's Deals' links in another tab")
    def click_on_links(self):
        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        actions = ActionChains(self.driver)
        wait.until(EC.presence_of_element_located(loc.gear_link_list_loc))
        link_list = self.find_elements(loc.gear_link_list_loc)
        self.link_names_list = []
        self.page_titles_list = []
        for link in link_list:
            if link:
                link = wait.until(EC.element_to_be_clickable(link))
                link_text = link.text.strip()
                self.link_names_list.append(link_text)
                actions.key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
                handles = self.driver.window_handles
                self.driver.switch_to.window(handles[1])
                wait.until(EC.presence_of_element_located((By.TAG_NAME, "head")))
                title = self.driver.title.strip()
                self.page_titles_list.append(title)
                self.driver.close()
                self.driver.switch_to.window(handles[0])
        print(self.link_names_list)
        print(self.page_titles_list)

    @allure.step("Check the link names and the opened page titles.")
    def link_names_verification(self):
        link_names_list = self.link_names_list
        page_titles_list = self.page_titles_list
        for link in link_names_list:
            assert any(link in title for title in page_titles_list), f"Link name: {link} not found in page titles list"
