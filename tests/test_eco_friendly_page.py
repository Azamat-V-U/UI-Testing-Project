import pytest
import allure


@allure.feature("Eco Friendly page")
@allure.story("Eco Friendly page functionality verification")
@allure.title("Compare products list: Adding and removing a product item.")
@pytest.mark.critical
def test_compare_products_list(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.add_item_to_compare_list()
    eco_friendly_page.message_verification(
        "You added product Ana Running Short to the comparison list."
    )
    eco_friendly_page.compare_products_list_verification()
    eco_friendly_page.delete_item_from_compare_list()
    eco_friendly_page.message_verification(
        "You removed product Ana Running Short from the comparison list."
    )


@allure.feature("Eco Friendly page")
@allure.story("Eco Friendly page functionality verification")
@allure.title("Products cart: Adding and deleting an item from the products cart")
@pytest.mark.medium
def test_item_in_products_cart(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.add_item_to_cart()
    eco_friendly_page.message_verification(
        "You added Fiona Fitness Short to your shopping cart."
    )
    eco_friendly_page.check_item_details_in_cart()
    eco_friendly_page.added_item_verification()
    eco_friendly_page.delete_item_from_cart()
    eco_friendly_page.no_items_message_verification(
        "You have no items in your shopping cart."
    )


@allure.feature("Eco Friendly page")
@allure.story("Eco Friendly page functionality verification")
@allure.title("Filtering products by price")
@pytest.mark.low
def test_filter_items_by_price(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.filter_items_by_price()
    eco_friendly_page.filtered_items_number_verification()
