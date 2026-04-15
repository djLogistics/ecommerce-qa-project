from selenium import webdriver

def get_driver():
    options = webdriver.ChromeOptions()
    
    # disable popups
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    
    # disable chrome's password manager
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False})
    
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver