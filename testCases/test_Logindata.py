# Data driven testing — login with inputs read from Excel file

from pageObjects.HomePage import Homepage
from pageObjects.LoginPage import Loginpage
from pageObjects.MyAccountPage import MyAccountPage
from Utilities import XLUtils
from Utilities.customLogger import LogGen
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import undetected_chromedriver as uc


class Test_Login_DDT():
    logger = LogGen.loggen()

    path = os.path.abspath(os.curdir) + "\\TestData\\Opencart_LoginData.xlsx"

    def test_login_ddt(self):
        self.logger.info("Starting login DDT")
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        lst_status = []

        self.driver = uc.Chrome()
        self.driver.get("https://demo.opencart.com/")
        self.driver.maximize_window()

        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.LINK_TEXT, "My Account"))
        )

        self.hp = Homepage(self.driver)
        self.lp = Loginpage(self.driver)
        self.ma = MyAccountPage(self.driver)

        for r in range(2, self.rows + 1):
            self.hp.myaccount()
            self.hp.login()

            self.email = XLUtils.readData(self.path, "Sheet1", r, 1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)

            self.lp.setEmail(self.email)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()

            import time
            time.sleep(2)

            self.targetpage = self.lp.isMyAccountPageExists()

            if self.exp == 'Valid':
                if self.targetpage == True:
                    lst_status.append('Pass')
                    self.ma.clickLogout()
                    
                    WebDriverWait(self.driver, 15).until(
                        EC.presence_of_element_located((By.LINK_TEXT, "My Account"))
                    )
                else:
                    lst_status.append('Fail')
            elif self.exp == 'Invalid':
                if self.targetpage == True:
                    lst_status.append('Fail')
                else:
                    lst_status.append('Pass')

        self.driver.close()

        if "Fail" not in lst_status:
            assert True
        else:
            assert False, f"Some login attempts failed: {lst_status}"

        self.logger.info("End of login_Data")
