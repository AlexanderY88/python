from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from POM.pages.base_page import BasePage


# burger menu
class Menu(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # elements
    MENU_BTN = (By.CSS_SELECTOR, "#react-burger-menu-btn")
    ALL_ITEMS = (By.CSS_SELECTOR, "#inventory_sidebar_link")
    ABOUT = (By.CSS_SELECTOR, "#about_sidebar_link")
    LOGOUT = (By.CSS_SELECTOR, "#logout_sidebar_link")
    RESET_APP_STATE = (By.CSS_SELECTOR, "#reset_sidebar_link")
    CLOSE_MENU_BTN = (By.CSS_SELECTOR, "#react-burger-cross-btn")
    MENU_LIST = (By.CSS_SELECTOR, "bm-item-list")

    def open_menu(self):
        self.click(self.MENU_BTN)

    def click_all_items(self):
        self.click(self.ALL_ITEMS)

    def click_about(self):
        self.click(self.click_about())

    def click_logout(self):
        self.click(self.LOGOUT)

    def click_reset_app_state(self):
        self.click(self.RESET_APP_STATE)

    def close_menu(self):
        self.click(self.CLOSE_MENU_BTN)

    def get_link(self):
        link = self.get_url()
        return link