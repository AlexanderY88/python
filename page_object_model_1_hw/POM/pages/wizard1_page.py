import time

from selenium.webdriver.common.by import By
from POM.pages.base_page import BasePage


class Wizard1(BasePage):
    # elements
    USER_NAME = (By.CSS_SELECTOR, "#user-name")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN_BTN = (By.CSS_SELECTOR, "#login-button")
    ERROR_MSG = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.fill_text(self.USER_NAME, username)
        self.fill_text(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)
        try:
            error_msg = self.get_text(self.ERROR_MSG)
            return error_msg
        except:
            error_msg = "No Errors"
            return error_msg

    def return_current_url(self):
        return self.get_url()
