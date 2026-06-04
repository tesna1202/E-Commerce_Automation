import pytest
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pageObjects.HomePage import Homepage
from pageObjects.SearchPage import SearchPage
from Utilities.customLogger import LogGen


class Test_Search:
    logger = LogGen.loggen()

    def test_search_valid_product(self):
        self.logger.info("Test: Search with valid product name")
        self.driver = uc.Chrome()
        self.driver.get("https://demo.opencart.com/")
        self.driver.maximize_window()

        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.LINK_TEXT, "My Account"))
        )

        self.sp = SearchPage(self.driver)
        self.sp.enterSearchTerm("Mac")
        self.sp.clickSearchButton()

        count = self.sp.getProductCount()
        self.driver.close()

        assert count > 0, "Expected products but got none"
        self.logger.info("test_search_valid_product PASSED")

    def test_search_invalid_product(self):
        self.logger.info("Test: Search with invalid product name")
        self.driver = uc.Chrome()
        self.driver.get("https://demo.opencart.com/")
        self.driver.maximize_window()

        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.LINK_TEXT, "My Account"))
        )

        self.sp = SearchPage(self.driver)
        self.sp.enterSearchTerm("abcxyz123notaproduct")
        self.sp.clickSearchButton()

        result = self.sp.getNoResultMessage()
        self.driver.close()

        assert result == True, "Expected no-result message but it wasn't shown"
        self.logger.info("test_search_invalid_product PASSED")