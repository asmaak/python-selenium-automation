from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
    ADD_CART_BUTTON = (By.CSS_SELECTOR, "[id*='addToCartButton']")

    def verify_search_results(self,expected_text):
        self.verify_partial_text(expected_text, *self.SEARCH_RESULTS_TEXT)

    def verify_cart_page_opens(self):
        self.verify_url(f'{self.base_url}cart')  # 'https://www.target.com/' + 'cart'
    def click_add_to_cart_button(self):
        sleep(5)
        self.click(*self.ADD_CART_BUTTON)
