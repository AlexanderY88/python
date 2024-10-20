
from selenium.webdriver.common.by import By
from POM.pages.base_page import BasePage


class FinishOrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # elements
    STATUS = (By.CSS_SELECTOR, ".header_secondary_container")
    MSG_TXT = (By.CSS_SELECTOR, "[data-test='complete-header']")
    HOME_BTN = (By.CSS_SELECTOR, ".btn_primary")
    SUCCESS_TITLE = (By.CSS_SELECTOR, "#checkout_complete_container > h2")
    SUCCESS_TEXT = (By.CSS_SELECTOR, "#checkout_complete_container > div")
    BACK_HOME_BTN = (By.CSS_SELECTOR,"#back-to-products")

    def message(self):
        message = self.get_text(self.MSG_TXT)
        return message

    def home(self):
        self.click(self.HOME_BTN)

    def get_title(self):
        text = self.get_text(self.SUCCESS_TITLE)
        return text

    def get_link(self):
        link = self.get_url()
        return link

    def get_message_text(self):
        text = self.get_text(self.SUCCESS_TEXT)
        return text

    def back_home_btn(self):
        self.click(self.BACK_HOME_BTN)