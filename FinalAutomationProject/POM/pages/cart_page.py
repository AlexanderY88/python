from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from POM.pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    CHECKOUT_BTN = (By.CSS_SELECTOR, ".checkout_button")
    BACK_BTN = (By.CSS_SELECTOR, ".back")
    FIRST_REMOVE_CART_BTN = (By.CSS_SELECTOR, ".btn_small")
    FIRST_ITEM = (By.CSS_SELECTOR, ".cart_item_label")
    PRODUCT_ITEMS = (By.CSS_SELECTOR, "inventory_item_name")
    CONTINUE_SHOPPING_BTN = (By.ID, "continue-shopping")
    CART_ITEMS = (By.CSS_SELECTOR, "#cart_contents_container > div > div.cart_list > div.cart_item")

    def checkout(self):
        self.click(self.CHECKOUT_BTN)

    def remove_first_product(self):
        self.click(self.FIRST_REMOVE_CART_BTN)

    def back_btn(self):
        self.click(self.BACK_BTN)

    def is_cart_empty(self) -> bool:
        # Check if any cart items are present
        try:
            cart_items = self.driver.find_elements(*self.CART_ITEMS)
            if len(cart_items) == 0:
                return True
            elif len(cart_items) != 0:
                return False
        except:
            return True  # element not found because there is no products in the cart

    def get_product_quantity(self) -> int:
        product_items = self.driver.find_elements(*self.PRODUCT_ITEMS)
        return len(product_items)

    def is_displayed(self, locator) -> bool:
        is_displayed = True
        try:
            self.driver.find_element(*locator).is_displayed()
            return True
        except NoSuchElementException:
            # If element is not found, return False
            return False

    def checkout_btn_is_displayed(self) -> bool:
        return self.is_displayed(self.CHECKOUT_BTN)

    def continue_shopping_is_displayed(self) -> bool:
        return self.is_displayed(self.CONTINUE_SHOPPING_BTN)

    def cart_navigation_buttons(self) -> bool:
        return self.checkout_btn_is_displayed() and self.continue_shopping_is_displayed()
