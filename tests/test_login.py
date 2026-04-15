from utils.driver_setup import get_driver
from pages.login_page import LoginPage


def test_login_success():
    
    # initialize browser
    driver = get_driver()
    
    # create login object
    login_page = LoginPage(driver)
    
    # open the application
    login_page.open()
    
    # perform login
    login_page.login("standard_user", "secret_sauce")
    
    # check for successful login
    assert "inventory" in driver.current_url
    
    print("Login test passed")
    driver.quit()