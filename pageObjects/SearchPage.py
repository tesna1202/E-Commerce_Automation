from selenium.webdriver.common.by import By

class SearchPage():
    input_search_name = "search"
    button_search_css = "button.btn[type='button']"
    result_product_css = "div[class='product-thumb']"
    msg_noresult_xpath = "//p[normalize-space()='There is no product that matches the search criteria.']"

    def __init__(self, driver):
        self.driver = driver

    def enterSearchTerm(self, term):
        self.driver.find_element(By.NAME, self.input_search_name).clear()
        self.driver.find_element(By.NAME, self.input_search_name).send_keys(term)

    def clickSearchButton(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_search_css).click()

    def getProductCount(self):
        results = self.driver.find_elements(By.CSS_SELECTOR, self.result_product_css)
        return len(results)

    def getNoResultMessage(self):
        try:
            msg = self.driver.find_element(By.XPATH, self.msg_noresult_xpath)
            if msg.is_displayed():
                return True
        except:
            return False