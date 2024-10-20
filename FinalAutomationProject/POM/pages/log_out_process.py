from selenium.webdriver.common.by import By

from POM.pages.base_page import BasePage


class LogOutProcess(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    MENU_BTN = (By.CSS_SELECTOR, "#react-burger-menu-btn")
    LOGOUT_BTN = (By.CSS_SELECTOR, "#logout_sidebar_link")

    def logout(self):
        self.click(self.MENU_BTN)
        self.click(self.LOGOUT_BTN)
        print("Logout successfully")
