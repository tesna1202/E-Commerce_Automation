#Logout page
from selenium.webdriver.common.by import By

class MyAccountPage():

    lnk_logout_lnktxt = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_logout_lnktxt).click()
