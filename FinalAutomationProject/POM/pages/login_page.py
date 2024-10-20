from selenium.webdriver.common.by import By
from POM.pages.base_page import BasePage


class LoginPage(BasePage):
    # elements
    USER_NAME = (By.CSS_SELECTOR, "#user-name")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN_BTN = (By.CSS_SELECTOR, "#login-button")
    ERROR_MSG = (By.CSS_SELECTOR, "div.error-message-container.error")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        """Perform login with given username and password."""
        self.fill_text(self.USER_NAME, username)
        self.fill_text(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def return_current_url(self):
        return self.get_url()

    def get_error_message(self):
        return self.get_text(self.ERROR_MSG)

    def standard_user_login(self):
        self.login("standard_user", "secret_sauce")

