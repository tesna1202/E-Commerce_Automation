from pageObjects.HomePage import Homepage
from pageObjects.LoginPage import Loginpage
from Utilities.customLogger import LogGen
import time
import undetected_chromedriver as uc


class Test_Login():
    logger = LogGen.loggen()

    def test_login(self):
        self.logger.info("******* Starting login **********")
        self.driver = uc.Chrome()  # No need to set PATH 

        self.driver.get("https://demo.opencart.com/")
        self.driver.maximize_window()
        time.sleep(8)

        self.hp=Homepage(self.driver)
        self.hp.myaccount()
        self.hp.login()

        self.lp = Loginpage(self.driver)
        self.lp.setEmail("tesna1202@gmail.com")
        self.lp.setPassword("Tesna@1202")
        self.lp.clickLogin()


        self.driver.close()
        self.logger.info("******* End of login **********")
