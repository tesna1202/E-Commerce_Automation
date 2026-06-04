import undetected_chromedriver as uc
from pageObjects.HomePage import Homepage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from Utilities.randomString import random_string
from Utilities.customLogger import LogGen
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


class TestLogin:

    logger = LogGen.loggen()

    def test_login(self):
        self.logger.info("Test Account Registration started")
        self.driver = uc.Chrome()
        self.driver.get("https://demo.opencart.com/")
        self.driver.maximize_window()

        # Explicit wait
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.LINK_TEXT, "My Account"))
        )

        self.hp = Homepage(self.driver)
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

        # getconfirmationmsg() waits internally
        self.conf_msg = self.arp.getconfirmationmsg()

        if self.conf_msg == "Your Account Has Been Created!":
            assert True
        else:
            # Added .png extension
            self.driver.save_screenshot(
                os.path.abspath(os.curdir) + "\\Screenshots\\" + "test_login.png"
            )
            self.driver.close()
            assert False, f"Expected success message but got: '{self.conf_msg}'"

        self.driver.close()
        self.logger.info("Test Account Registration finished")
