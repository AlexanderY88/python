from selenium.webdriver.common.by import By

from POM.pages.base_page import BasePage


# products page
class Wizard2(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    product_1 = (By.CSS_SELECTOR, "#item_0_title_link")
    product_2 = (By.CSS_SELECTOR, "#item_1_title_link")
    product_3 = (By.CSS_SELECTOR, "#item_2_title_link")
    product_4 = (By.CSS_SELECTOR, "#item_3_title_link")
    product_5 = (By.CSS_SELECTOR, "#item_4_title_link")
    product_6 = (By.CSS_SELECTOR, "#item_5_title_link")
    CART_BTN = (By.CSS_SELECTOR, ".shopping_cart_link")
    def click_on_product(self, option):
        match option:
            case 1:
                self.click(self.product_1)
            case 2:
                self.click(self.product_2)
            case 3:
                self.click(self.product_3)
            case 4:
                self.click(self.product_4)
            case 5:
                self.click(self.product_5)
            case 6:
                self.click(self.product_6)
            case _:
                print("No product chosen")

    def click_on_cart(self):
        self.click(self.CART_BTN)

