

from selenium.webdriver.common.by import By


class AccountRegistrationPage():
    txt_firstname_name = "firstname"
    txt_lastname_name = "lastname"
    txt_email_name = "email"
    txt_password_name = "password"
    button_privacy_name = "agree"
    button_cont_css="button[type='submit']"
    text_msg_conf_xpath="//h1[normalize-space()='Your Account Has Been Created!']"
    text_msgconf_css = "div[id='content'] h1"

    def __init__(self, driver):
        self.driver = driver

    def setFirstName(self,firstname):
      self.driver.find_element(By.NAME,self.txt_firstname_name).send_keys(firstname)

    def setLastName(self,lastname):
        self.driver.find_element(By.NAME,self.txt_lastname_name).send_keys(lastname)

    def setEmail(self,email):
        self.driver.find_element(By.NAME,self.txt_email_name).send_keys(email)


    def setPassword(self,pwd):
        self.driver.find_element(By.NAME,self.txt_password_name).send_keys(pwd)

    def setPrivacyPolicy(self):
        self.driver.find_element(By.NAME,self.button_privacy_name).click()


    def clickContinue(self):
        self.driver.find_element(By.CSS_SELECTOR,self.button_cont_css).click()

    def getconfirmationmsg(self):
        try:
            return  self.driver.find_element(By.CSS_SELECTOR,self.text_msgconf_css).text
        except:
            None