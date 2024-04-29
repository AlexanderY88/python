import time

from selenium.webdriver.common.by import By

from POM.pageobjects.base_page import BasePage


class NewTabPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    NEW_LIST_BTN = (By.CSS_SELECTOR, ".mtt-tabs-new-button")
    NEW_LIST_TITLE = (By.CSS_SELECTOR, "#modalTextInput")
    NEW_LIST_TITLE_OK_BTN = (By.CSS_SELECTOR, "#btnModalOk")
    NEW_LIST_TITLE_CANCEL_BTN = (By.CSS_SELECTOR, "#btnModalCancel")
    NUMBER_OF_TASKS = (By.CSS_SELECTOR, "#total")
    TASKS_TITLE = (By.CSS_SELECTOR, ".task-title")
    def new_list(self):
        self.click(self.NEW_LIST_BTN)

    def new_list_name(self, txt):
        self.fill_text(self.NEW_LIST_TITLE, txt)

    def click_ok(self):
        self.click(self.NEW_LIST_TITLE_OK_BTN)

    def new_list_create(self, txt):
        self.new_list()
        self.new_list_name(txt)
        self.click_ok()

    def number_of_tasks(self):
        time.sleep(1)
        title = len(self.TASKS_TITLE)
        header = self.get_text(self.NUMBER_OF_TASKS)
        if int(title) == int(header):
            return("Number of tasks in the tab: ", title)
        else:
            return("There is an error with counting the tasks")
