import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AccountRegistrationPage():
    txt_firstname_name = "firstname"
    txt_lastname_name = "lastname"
    txt_email_name = "email"
    txt_password_name = "password"
    button_privacy_name = "agree"
    button_cont_css = "button[type='submit']"
    text_msgconf_css = "div[id='content'] h1"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def setFirstName(self, firstname):
        self.driver.find_element(By.NAME, self.txt_firstname_name).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element(By.NAME, self.txt_lastname_name).send_keys(lastname)

    def setEmail(self, email):
        self.driver.find_element(By.NAME, self.txt_email_name).send_keys(email)

    def setPassword(self, pwd):
        self.driver.find_element(By.NAME, self.txt_password_name).send_keys(pwd)

    def setPrivacyPolicy(self):
        element = self.driver.find_element(By.NAME, self.button_privacy_name)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)
        if not element.is_selected():
            self.driver.execute_script("arguments[0].click();", element)
        time.sleep(1)

    def clickContinue(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.button_cont_css)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def getconfirmationmsg(self):
        try:
            # FIX: wait for the success page h1 before reading it
            self.wait.until(
                EC.text_to_be_present_in_element(
                    (By.CSS_SELECTOR, self.text_msgconf_css),
                    "Your Account Has Been Created!"
                )
            )
            return self.driver.find_element(By.CSS_SELECTOR, self.text_msgconf_css).text
        except Exception as e:
            # FIX: was "None" without return — now returns None properly with error info
            print(f"Confirmation message not found: {e}")
            return None