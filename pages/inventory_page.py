from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Inventory_page:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def add_backpack_to_cart(self):
        # wait until button is clickable, then click
        self.wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
        
    def open_cart(self):
        # wait until button is clickable, then click
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()
        
    def get_cart_items(self):
        return self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        