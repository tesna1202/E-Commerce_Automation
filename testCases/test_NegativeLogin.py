import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from pageObjects.HomePage import Homepage
from pageObjects.LoginPage import Loginpage
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_NegativeLogin():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    def test_login_with_wrong_password(self):
        self.logger.info("Negative login test started")
        self.driver = uc.Chrome()
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(8)

        self.hp = Homepage(self.driver)
        self.hp.myaccount()
        self.hp.login()

        self.lp = Loginpage(self.driver)
        self.lp.setEmail(ReadConfig.getUserEmail())
        self.lp.setPassword("wrongpassword123")
        self.lp.clickLogin()
        time.sleep(3)

        # Verify login failed 
        try:
            self.driver.find_element(By.XPATH, "//h2[normalize-space()='My Account']")
            on_account_page = True
        except:
            on_account_page = False

        self.driver.close()

        assert on_account_page == False, "Login should have failed but reached My Account page"
        self.logger.info("Negative login test passed")
