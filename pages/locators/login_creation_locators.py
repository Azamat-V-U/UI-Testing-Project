from selenium.webdriver.common.by import By


first_name_loc = (By.ID, 'firstname')
last_name_loc = (By.ID, 'lastname')
email_field_loc = (By.ID, 'email_address')
password_field_loc = (By.ID, 'password')
password_confirmation_field_loc = (By.ID, 'password-confirmation')
submit_button_loc = (By.XPATH, "(//button[@title='Create an Account'])")
# text_message = (By.XPATH, "(//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)'])")
text_message = (By.CSS_SELECTOR, ".messages div[data-bind='html: $parent.prepareMessageForHtml(message.text)']")
invalid_email_message_loc = (By.ID, "email_address-error")
# invalid_password_message_loc = (By.XPATH, "(//div[@for='password'])")
invalid_password_message_loc = (By.ID, "password-error")
invalid_password_confirmation_message_loc = (By.ID, "password-confirmation-error")
