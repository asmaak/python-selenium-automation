from pages.base_page import Page
from selenium.webdriver.common.by import By

class CartPage(Page):
    SUBTOTAL_CART = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")

    CART_EMPTY_MSG=(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
    def open(self):
        self.open_url(f'{self.base_url}cart')
    def cart_empty(self):
        self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)

    def verify_cart_page_opens(self):
        self.verify_url(f'{self.base_url}cart')  # 'https://www.target.com/' + 'cart'

    def verify_cart_has_items(self,amount):
       self.verify_partial_text(amount,*self. SUBTOTAL_CART)
