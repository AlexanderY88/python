from selenium.webdriver.common.by import By

from POM.pages.base_page import BasePage


class Wizard3(BasePage):
    #product age
    def __init__(self, driver):
        super().__init__(driver)

    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "#add-to-cart")
    BACK_TO_PRODUCTS = (By.CSS_SELECTOR, "#back-to-products")
    CART_BTN = (By.CSS_SELECTOR, ".shopping_cart_link")

    def add_to_cart (self):
        self.click(self.ADD_TO_CART_BTN)

    def back_to_products_page(self):
        self.click(self.BACK_TO_PRODUCTS)

    def click_on_cart(self):
        self.click(self.CART_BTN)