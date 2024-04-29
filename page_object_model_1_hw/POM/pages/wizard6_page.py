from selenium.webdriver.common.by import By

from POM.pages.base_page import BasePage


class Wizard6(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # elements
    FINISH_BTN = (By.CSS_SELECTOR, ".cart_button")
    CANCEL_BTN = (By.CSS_SELECTOR, ".cart_cancel_link")

    def finish_order(self):
        self.click(self.FINISH_BTN)

    def cancel_order(self):
        self.click(self.CANCEL_BTN)

