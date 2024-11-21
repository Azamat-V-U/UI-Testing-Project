from selenium.webdriver.common.by import By

# remove_item_loc = (By.XPATH, "(//a[@title='Remove This Item'])")
remove_item_loc = (By.CSS_SELECTOR, ".product-item.odd:first-child .delete")
# pop_up_ok_button_loc = (By.XPATH, "(//button[@class='action-primary action-accept'])")
pop_up_ok_button_loc = (By.CSS_SELECTOR, ".action-accept")
delete_item_icon_loc = (By.XPATH, "(//a[@class='action delete'])")
email_field_loc = (By.XPATH, "(//input[@name='login[username]'])")
password_field_loc = (By.XPATH, "(//input[@name='login[password]'])")
sign_in_button_loc = (By.XPATH, "(//button[@class='action login primary'])")

menu_button_loc = (By.XPATH, "(//button[@data-action='customer-menu-toggle'])[1]")
sign_out_loc = (By.LINK_TEXT, "Sign Out")
logged_in_loc = (By.XPATH, "(//span[@class='logged-in'])[1]")
