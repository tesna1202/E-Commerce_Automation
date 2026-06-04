from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Homepage:
    button_myaccount_linktext = "My Account"
    button_register_linktext = "Register"
    button_login_linktext = "Login"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def myaccount(self):
        # Wait and click on 'My Account'
        my_account = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, self.button_myaccount_linktext)))
        my_account.click()

    def register(self):
        # Wait until the dropdown is visible and click 'Register'
        self.driver.find_element(By.LINK_TEXT, self.button_register_linktext).click()

    def login(self):
        # Wait until the dropdown is visible and click 'Login'
        self.driver.find_element(By.LINK_TEXT, self.button_login_linktext).click()

