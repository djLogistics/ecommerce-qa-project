from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.inventory_page import Inventory_page

def test_add_item_to_cart():
    driver = get_driver()
    
    # Step 1: login
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    
    # Step 2: interact with inventory
    inventory = Inventory_page(driver)
    inventory.add_backpack_to_cart()
    inventory.open_cart()
    
    # Step 3: validate cart
    items = inventory.get_cart_items()
    assert len(items) > 0
    
    driver.quit()