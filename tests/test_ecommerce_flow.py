from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()

# ignores password and security popups
options.add_argument("--disable-notifications")
options.add_argument("--disable-save-password-bubble")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")

options.add_experimental_option("prefs", { 
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False
})

# Initializes WebDriver and explicit wait
driver = webdriver.Chrome(options = options)
wait = WebDriverWait(driver, 10)

# Step 1: navigate to the web browser
driver.get("https://saucedemo.com/")
driver.maximize_window()

# Step 2: Enter credentials and click login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
driver.save_screenshot("login.png")


# Step 3: Validate successful login by checking url
if "inventory" in driver.current_url:
    print("Test passed, login successful")
else:
    print("Test failed: login unsuccessful")
    
# step 5: Add item to cart, while waiting for button to be clickable
add_to_cart = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
add_to_cart.click()
driver.save_screenshot("item-added-to-cart.png")


# Step 6: Navigate to cart, while waiting for button to be clickable
cart_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
cart_button.click()

# Step 7: Validate item is present in cart
cart_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
if len(cart_items) > 0:
    print("Test passed: inventory item in cart")
else:
    print("Test failed: no inventory items in cart")
driver.save_screenshot("cart-validation.png")

driver.quit()
