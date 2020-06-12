# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

# Start the browser and login with standard_user
def login (user, password):
    logging.info('Starting the browser...')

    options = ChromeOptions()
    options.add_argument("--headless") 
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome()

    logging.info('Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')

    logging.info('Logging user in')
    driver.find_element_by_css_selector('input#user-name').send_keys(user)
    driver.find_element_by_css_selector('input#password').send_keys(password)
    driver.find_element_by_css_selector('input[value=LOGIN]').click()

    # Check that login was successful
    product_page = driver.find_element_by_css_selector('#inventory_filter_container > .product_label').text
    assert product_page == 'Products', 'Login is unsuccessful'
    logging.info('Login success: { username: ' + user + ' }')

    logging.info('Adding items to cart')
    inventory_items = driver.find_elements_by_css_selector('.inventory_item')
    for item in inventory_items:
        add_button = 'button.btn_inventory'
        item_name_selector = '.inventory_item_name'
        
        item_name = item.find_element_by_css_selector(item_name_selector).text
        item.find_element_by_css_selector(add_button).click()
        logging.info('Item added: ' + item_name)

    # Check that cart is full
    cart_badge = driver.find_element_by_css_selector('#shopping_cart_container .shopping_cart_badge').text
    assert cart_badge == str(len(inventory_items)), 'The cart has not been filled'
    logging.info('Cart is full')    
        
    logging.info('Navigating to cart page')    
    driver.find_element_by_css_selector('a.shopping_cart_link').click()
    assert '/cart.html' in driver.current_url, 'Cart navigation unsuccessful'

    logging.info('Removing items from cart')
    cart_items = driver.find_elements_by_css_selector('.cart_item')
    for item in cart_items:
        remove_button = 'button.cart_button'
        item_name_selector = '.inventory_item_name'
        
        item_name = item.find_element_by_css_selector(item_name_selector).text
        item.find_element_by_css_selector(remove_button).click()
        logging.info('Item removed: ' + item_name)
    
    # Check that cart is empty 
    cart_badge = driver.find_elements_by_css_selector('#shopping_cart_container .shopping_cart_badge')
    assert len(cart_badge) == 0, 'The cart is not yet empty'
    logging.info('Cart is empty')

login('standard_user', 'secret_sauce')
