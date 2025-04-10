from selenium.webdriver.common.by import By

from pages.base_page import Page

class SignIn(Page):

   SIGN_IN_TEXT=(By.CSS_SELECTOR, "h1[class*='styles_fontSize1__i0fbt']")
   def verify_sign_in_page_opened(self):
       self.verify_text('Sign in or create account',*self.SIGN_IN_TEXT)


