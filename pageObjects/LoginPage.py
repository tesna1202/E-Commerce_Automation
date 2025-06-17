from selenium.webdriver.common.by import By


class Loginpage():
    txt_email_name = "email"
    txt_pwd_name = "password"
    txt_login_css = "button[type='submit']"
    msg_myaccount_css = "body > main:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > h2:nth-child(3)"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.NAME,self.txt_email_name).send_keys(email)

    def setPassword(self, pwd):
        self.driver.find_element(By.NAME,self.txt_pwd_name).send_keys(pwd)

    def clickLogin(self):
        self.driver.find_element(By.CSS_SELECTOR,self.txt_login_css).click()

    def isMyAccountPageExists(self):
        try:
            if self.driver.find_element(By.CSS_SELECTOR,self.msg_myaccount_css).is_displayed():
                return True
        except:
            return False
        