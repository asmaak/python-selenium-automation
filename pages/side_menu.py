from selenium.webdriver.common.by import By

from pages.base_page import Page


class SideMenu(Page):
    SIGN_IN_SIDE=(By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
    def navigate_to_side_menu(self):
        self.click(*self.SIGN_IN_SIDE)

