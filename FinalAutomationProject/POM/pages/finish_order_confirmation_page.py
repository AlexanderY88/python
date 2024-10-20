import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from POM.pages.base_page import BasePage


class FinishOrderConfirmationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # elements
    FINISH_BTN = (By.CSS_SELECTOR, "#finish")
    CANCEL_BTN = (By.CSS_SELECTOR, "#cancel")
    TITLE = (By.CSS_SELECTOR, "#checkout_complete_container > h2")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#item_0_title_link")

    def finish_order(self):
        self.click(self.FINISH_BTN)

    def cancel_order(self):
        self.click(self.CANCEL_BTN)

    def get_link(self):
        time.sleep(1)
        link = self.get_url()
        return link

    def get_title(self):
        title = self.get_text(self.TITLE)
        return title

    def get_product_name(self) -> str:
        try:
            product_name = self.get_text(self.PRODUCT_NAME)
            return product_name
        except NoSuchElementException:
            return ""