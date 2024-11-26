from selenium.webdriver.common.by import By


item_name_loc = (By.XPATH, "(//a[@class='product-item-link'])[2]")
# add_to_compare_loc = (By.XPATH, "(//a[@class='action tocompare'])[1]")
add_to_compare_loc = (By.CSS_SELECTOR, ".item.product-item:first-child .tocompare")

# selected_item_link_loc = (By.XPATH, "(//a[@class='product-item-link'])[1]")
selected_item_link_loc = (By.CSS_SELECTOR, ".item.product-item:first-child .product-item-link")
# added_item_link_loc = (By.XPATH, "(//a[@data-bind='attr: {href: product_url}, html: name'])")
added_item_link_loc = (By.CSS_SELECTOR, ".product-item-name a[data-bind='attr: {href: product_url}, html: name']")

item_price_loc = (By.ID, "product-price-1919")
item_size_loc = (By.XPATH, "(//div[@option-label='30'])[1]")
item_color_loc = (By.XPATH, "(//div[@option-label='Green'])[1]")
item_add_to_cart_loc = (By.XPATH, "(//button[@title='Add to Cart'])[2]")

cart_icon_link_loc = (By.XPATH, "(//a[@class='action showcart'])")
counter_link_loc = (By.XPATH, "(//span[@class='counter-number'])")
item_see_details_loc = (By.XPATH, "(//span[@class='toggle'])")
item_cart_link_loc = (By.XPATH, "(//a[@data-bind='attr: {href: product_url}, html: product_name'])")
item_cart_size_loc = (By.XPATH, "(//span[@data-bind='text: option.value'])[1]")
item_cart_color_loc = (By.XPATH, "(//span[@data-bind='text: option.value'])[2]")
item_cart_price_loc = (By.CLASS_NAME, "minicart-price")
item_amount_loc = (By.XPATH, "(//span[@data-bind=\"text: getCartParam('summary_count')\"])")
item_deleted_message = (By.XPATH, "(//strong[@class='subtitle empty'])")

price_dropdown_loc = (By.XPATH, "(//div[@data-role='collapsible'])[14]")
price_link_loc = (
    By.XPATH, "(//a[@href='https://magento.softwaretestingboard.com/collections/eco-friendly.html?price=20-30'])"
)
price_range_loc = (By.XPATH, "(//div[@class='filter-options-item allow active']//span[@class='count'])[2]")
price_range_child_loc = (By.XPATH, ".//span[@class='filter-count-label']")

items_list_loc = (By.XPATH, "(//ol[@class='products list items product-items'])")
selected_items_loc = (By.XPATH, "(//li[@class='item product product-item'])")
