#Data driven testing, To login with the inputs read from excel file

import time
from pageObjects.HomePage import Homepage
from pageObjects.LoginPage import Loginpage
from pageObjects.MyAccountPage import MyAccountPage
from Utilities import XLUtils
from Utilities.customLogger import LogGen
import os
import undetected_chromedriver as uc

class Test_Login_DDT():
    logger = LogGen.loggen()  # Logger

    path = os.path.abspath(os.curdir)+"\\TestData\\Opencart_LoginData.xlsx"

    def test_login_ddt(self):
        self.logger.info(" Starting login")
        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        lst_status=[]
        self.driver = uc.Chrome()  # No need to set PATH 

        self.driver.get("https://demo.opencart.com/")
        self.driver.maximize_window()
        time.sleep(9)

        self.hp = Homepage(self.driver)  # HomePage Page Object Class
        self.lp = Loginpage(self.driver)  # LoginPage Page Object Class
        self.ma = MyAccountPage(self.driver)  # MyAccount Page Object class

        for r in range(2,self.rows+1):
            self.hp.myaccount()
            self.hp.login()

            self.email=XLUtils.readData(self.path,"Sheet1",r,1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)
            self.lp.setEmail(self.email)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(6)
            print("Successful so far..............................................")
            self.targetpage=self.lp.isMyAccountPageExists()
            print("Successful  no 2 so far..............................................")

            if self.exp=='Valid':
                if self.targetpage==True:
                    lst_status.append('Pass')
                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(5)
                    self.ma.clickLogout()
                else:
                    lst_status.append('Fail')
            elif self.exp=='Invalid':
                if self.targetpage == True:
                    lst_status.append('Fail')
                    time.sleep(5)
                else:
                    lst_status.append('Pass')
        self.driver.close()
        # final validation
        if "Fail" not in lst_status:
            assert True
        else:
            assert False
        print(lst_status)
        self.logger.info("******* End of test_003_login_Datadriven **********")
