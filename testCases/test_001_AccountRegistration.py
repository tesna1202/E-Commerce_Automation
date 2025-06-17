
import undetected_chromedriver as uc
from pageObjects.HomePage import Homepage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from Utilities.randomString import random_string
import time
import os
from Utilities.customLogger import LogGen            #For logging

class TestLogin:

    logger = LogGen.loggen()         #For logs

    def test_login(self):
        self.logger.info("Test Account Registration started..........")
        self.driver = uc.Chrome() 

        self.driver.get("https://demo.opencart.com/")
        self.driver.maximize_window()
        time.sleep(8)

        self.hp = Homepage(self.driver)         #Object of class Homepage
        self.hp.myaccount()
        self.hp.register()

        self.arp = AccountRegistrationPage(self.driver)
        self.arp.setFirstName("qerna")
        self.arp.setLastName("ijyjiv")
        self.email = random_string() + "@gmail.com"
        self.arp.setEmail(self.email)
        self.arp.setPassword("nihhj9403")
        self.arp.setPrivacyPolicy()
        self.arp.clickContinue()
        self.conf_msg = self.arp.getconfirmationmsg()                     #To get screenshot if registration is not successful
        if self.conf_msg == "Your Account Has Been Created!":
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\Screenshots\\"+"test_login")  
            self.driver.close()
            assert False  

        print("Test completed")
        time.sleep(5)
        self.driver.close()
        self.logger.info("Test Account Registration finished..........")
