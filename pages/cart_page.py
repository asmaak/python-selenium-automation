from pages.base_page import Page
from selenium.webdriver.common.by import By

class CartPage(Page):
    CART_MESSAGE=(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
    def cart_empty(self,expected_result):
        actual_result = self.driver.find_element(*self.CART_MESSAGE).text
        assert expected_result == actual_result, f'Expected {expected_result} did not match actual {actual_result}'