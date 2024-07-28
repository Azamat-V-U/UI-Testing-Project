import pytest
import allure


@allure.feature("Sale page")
@allure.story("Sale page functionality verification")
@allure.title("Compare product list: Adding and removing an item as a logged-in user")
@pytest.mark.critical
def test_item_in_compare_products_list(sale_page, logged_in_user):
    sale_page.open_page()
    sale_page.add_item_to_compare_list_in_another_tab()
    sale_page.delete_item_from_compare_list()
    sale_page.message_verification(
        "You removed product Circe Hooded Ice Fleece from the comparison list."
    )


@allure.feature("Sale page")
@allure.story("Sale page functionality verification")
@allure.title("Product cart: Adding and removing an item as a logged-in user")
@pytest.mark.medium
def test_item_in_cart(sale_page, eco_friendly_page, logged_in_user):
    sale_page.open_page()
    sale_page.add_product_to_cart()
    eco_friendly_page.check_item_details_in_cart()
    sale_page.delete_item_from_cart()


@allure.feature("Sale page")
@allure.story("Sale page functionality verification")
@allure.title("Mens's Deals block: Links verification")
@pytest.mark.medium
def test_links_verification(sale_page):
    sale_page.open_page()
    sale_page.click_on_links()
    sale_page.link_names_verification()
