from selenium.webdriver.common.by import By

from POM.pages.base_page import BasePage


class Wizard4(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    CHECKOUT_BTN = (By.CSS_SELECTOR, ".checkout_button")
    BACK_BTN = (By.CSS_SELECTOR, ".back")
    FIRST_REMOVE_CART_BTN = (By.CSS_SELECTOR, ".btn_small")

    def checkout (self):
        self.click(self.CHECKOUT_BTN)

    def remove_first_product(self):
        self.click(self.FIRST_REMOVE_CART_BTN)

    def back_btn(self):
        self.click(self.BACK_BTN)