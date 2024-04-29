from selenium.webdriver.common.by import By

from POM.pages.base_page import BasePage


class Wizard7(BasePage):

    def __init(self, driver):
        super().__init__(driver)

    # elements
    STATUS = (By.CSS_SELECTOR, ".header_secondary_container")
    MSG_TXT = (By.CSS_SELECTOR, "[data-test='complete-header']")
    HOME_BTN = (By.CSS_SELECTOR, ".btn_primary")


    def message(self):
        message = self.get_text(self.MSG_TXT)
        return message

    def home(self):
        self.click(self.HOME_BTN)
