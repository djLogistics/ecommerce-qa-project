from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()

# ignores password and security popups
options.add_argument("--disable notifications")
options.add_argument("--disable-save-password-bubble")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")

options.add_experimental_option("prefs", { 
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False
})

driver = webdriver.Chrome(options = options)

driver.get("https://saucedemo.com/")

driver.maximize_window()

driver.find_element(By.ID, "user-name").send_keys("standard_user")

driver.find_element(By.ID, "password").send_keys("secret_sauce")

driver.find_element(By.ID, "login-button"). click()

time.sleep(2)

if "inventory" in driver.current_url:
    print("Test passed, login successful")
    
else:
    print("Test failed: login unsuccessful")
    
time.sleep(2)

driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

cart_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))

cart_button.click()

time.sleep(2)

cart_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")

if len(cart_items) > 0:
    print("Test passed: inventory item in cart")
    
else:
    print("Test failed: no inventory items in cart")


driver.quit()
