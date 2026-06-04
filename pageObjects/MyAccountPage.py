#Logout page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MyAccountPage():

    lnk_logout_lnktxt = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def clickLogout(self):
        logout = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, self.lnk_logout_lnktxt))
        )
        # Scroll element into center of viewport to avoid overlapping elements
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", logout)
        # Use JS click to bypass any intercepting element
        self.driver.execute_script("arguments[0].click();", logout)