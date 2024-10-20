from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from POM.pages.base_page import BasePage


class ProductPage(BasePage):
    # product page
    def __init__(self, driver):
        super().__init__(driver)

    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "#add-to-cart")
    BACK_TO_PRODUCTS = (By.CSS_SELECTOR, "#back-to-products")
    CART_BTN = (By.CSS_SELECTOR, ".shopping_cart_link")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".inventory_details_name")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".inventory_details_price")
    ITEMS_IN_CART = (By.CSS_SELECTOR, "#shopping_cart_container > a > span")
    REMOVE_BTN = (By.CSS_SELECTOR, "#remove")
    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BTN)

    def back_to_products_page(self):
        self.click(self.BACK_TO_PRODUCTS)

    def click_on_cart(self):
        self.click(self.CART_BTN)

    def get_product_name(self) -> str:
        try:
            product_name = self.get_text(self.PRODUCT_NAME)
            return product_name
        except NoSuchElementException:
            return ""

    def get_product_price(self) -> str:
        try:
            product_price = self.get_text(self.PRODUCT_PRICE)
            return product_price
        except NoSuchElementException:
            return ""

    def get_link(self):
        link = self.get_url()
        return link

    def items_in_cart(self):
        try:
            num = self.get_text(self.ITEMS_IN_CART)
            return num
        except:
            num = ""
            return num

    def click_remove_btn(self):
        try:
            self.click(self.REMOVE_BTN)
        except Exception as e:  #
            return f"Error clicking remove button: {str(e)}"

