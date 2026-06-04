from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Loginpage():
    txt_email_name = "email"
    txt_pwd_name = "password"
    txt_login_css = "button[type='submit']"
  
    msg_myaccount_xpath = "//h2[normalize-space()='My Account']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def setEmail(self, email):
        self.driver.find_element(By.NAME, self.txt_email_name).send_keys(email)

    def setPassword(self, pwd):
        self.driver.find_element(By.NAME, self.txt_pwd_name).send_keys(pwd)

    def clickLogin(self):
        self.driver.find_element(By.CSS_SELECTOR, self.txt_login_css).click()

    def isMyAccountPageExists(self):
        try:
            
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, self.msg_myaccount_xpath))
            )
            return self.driver.find_element(By.XPATH, self.msg_myaccount_xpath).is_displayed()
        except:
            return False