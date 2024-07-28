from selenium.webdriver.common.by import By


hoodies_and_sweatshirts_link_loc = (By.XPATH, "(//li[@class='item'])[1]")
item_link_loc = (By.XPATH, "(//a[@class='product-item-link'])[1]")
item_element_loc = (By.XPATH, "(//a[@class='product-item-link'])[2]")
add_to_compare_loc = (By.XPATH, "(//a[@class='action tocompare'])")
selected_item_loc = (
    By.XPATH,
    "(//a[@href='https://magento.softwaretestingboard.com/men/tops-men/hoodies-and-sweatshirts-men.html'])[2]"
)
item_add_to_cart_loc = (By.XPATH, "(//button[@title='Add to Cart'])[2]")
item_price_loc = (By.ID, "product-price-238")
item_size_loc = (By.XPATH, "(//div[@option-label='XL'])[2]")
item_color_loc = (By.XPATH, "(//div[@option-label='Red'])[1]")
gear_link_list_loc = (By.XPATH, "(//ul[@class='items'])[3]//li/a")
