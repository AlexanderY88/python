from selenium.webdriver.common.by import By

from POM.pages.base_page import BasePage


class OrderFormPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    FIRST_NAME = (By.CSS_SELECTOR, "#first-name")
    LAST_NAME = (By.CSS_SELECTOR, "#last-name")
    POSTAL_CODE = (By.CSS_SELECTOR, "#postal-code")
    CONTINUE_BTN = (By.CSS_SELECTOR, ".submit-button")
    CANCEL_BTN = (By.CSS_SELECTOR, ".cart_cancel_link")
    ERROR_TEXT = (By.CSS_SELECTOR, " div.error-message-container.error > h3")
    def fill_form(self, first_name, last_name, postal_code):
        self.fill_text(self.FIRST_NAME, first_name)
        self.fill_text(self.LAST_NAME, last_name)
        self.fill_text(self.POSTAL_CODE, postal_code)
        self.click(self.CONTINUE_BTN)

    def cancel_btn(self):
        self.click(self.CANCEL_BTN)

    def get_current_url(self):
        link = self.get_url()
        return link

    def error_text(self):
        try:
            text = self.get_text(self.ERROR_TEXT)
            return text
        except:
            text = ""
            return text

    def click_continue_btn(self):
        self.click(self.CONTINUE_BTN)

