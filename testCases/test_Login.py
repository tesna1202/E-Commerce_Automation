from pageObjects.HomePage import Homepage
from pageObjects.LoginPage import Loginpage
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc


class Test_Login():
    logger = LogGen.loggen()

    def test_login(self):
        self.logger.info("Starting login")
        self.driver = uc.Chrome()
        self.driver.get("https://demo.opencart.com/")
        self.driver.maximize_window()

        # explicit wait
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.LINK_TEXT, "My Account"))
        )

        self.hp = Homepage(self.driver)
        self.hp.myaccount()
        self.hp.login()

        self.lp = Loginpage(self.driver)
        self.lp.setEmail(ReadConfig.getUserEmail())
        self.lp.setPassword(ReadConfig.getUserPassword())
        self.lp.clickLogin()

       
        assert self.lp.isMyAccountPageExists(), "Login failed — My Account page not found"

        self.driver.close()
        self.logger.info("End of login")
