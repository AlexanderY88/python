import time

from selenium.webdriver.common.by import By

from POM.pageobjects.base_page import BasePage


class TasksPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # elements
    TABS_LIST = (By.CSS_SELECTOR, ".mtt-tab")
    taskField = (By.CSS_SELECTOR, "#task")
    addTaskBtn = (By.CSS_SELECTOR, "#newtask_submit")
    NEW_LIST = (By.CSS_SELECTOR, "[title='New list']")
    NEW_LIST_NAME = (By.CSS_SELECTOR, "modalTextInput")
    NEW_TASK_BTN = (By.CSS_SELECTOR, "#newtask_adv")
    SEARCH_FIELD = (By.CSS_SELECTOR, "#search")
    TASKS_TOTAL = (By.CSS_SELECTOR, "#total")
    # new task elements
    PRIORITY = (By.CSS_SELECTOR, "[name='prio']")
    DUE = (By.CSS_SELECTOR, "#duedate")
    TASK = (By.CSS_SELECTOR, "div > div:nth-child(3) > input")
    NOTE = (By.CSS_SELECTOR, "[name='note']")
    TAGS = (By.CSS_SELECTOR, "#edittags")
    SHOW_ALL_LINK = (By.CSS_SELECTOR, "#alltags_show")
    SAVE_BTN = (By.CSS_SELECTOR, "div.form-row.form-bottom-buttons > button:nth-child(1)")
    CANCEL_BTN = (By.CSS_SELECTOR, "div.form-row.form-bottom-buttons > button.mtt-back-button")
    # Priority Options:
    PRIO_NEGATIVE = (By.CSS_SELECTOR, "[value='-1']")
    PRIO_ZERO = (By.CSS_SELECTOR, "[value='0']")
    PRIO_ONE = (By.CSS_SELECTOR, "[value='1']")
    PRIO_TWO = (By.CSS_SELECTOR, "[value='2']")

    def click_a_tab(self, num):
        self.click_tab(self.TABS_LIST, num)

    def add_simple_task(self, txt):
        self.fill_text(self.taskField, txt)
        num = self.get_text(self.TASKS_TOTAL)
        self.click(self.addTaskBtn)
        time.sleep(1)
        num1 = self.get_text(self.TASKS_TOTAL)
        if int(num1) > int(num):
            return "pass"
        else:
            return "failed"

    def new_task(self):
        self.click(self.NEW_TASK_BTN)

    def set_priority(self, option):
        match option:
            case -1:
                self.click(self.PRIO_NEGATIVE)
            case 0:
                self.click(self.PRIO_ZERO)
            case 1:
                self.click(self.PRIO_ONE)
            case 2:
                self.click(self.PRIO_TWO)
            case _:
                print("No priority set")

    def fill_new_task(self, priority, date, title, note, tags):
        num = self.get_text(self.TASKS_TOTAL)
        self.new_task()
        self.set_priority(priority)
        self.fill_text(self.DUE, date)
        self.fill_text(self.TASK, title)
        self.fill_text(self.NOTE, note)
        self.fill_text(self.TAGS, tags)
        self.click(self.SAVE_BTN)
        time.sleep(1)
        num1 = self.get_text(self.TASKS_TOTAL)
        if int(num1) > int(num):
            return "pass"
        else:
            return "failed"

    def search_and_print(self, text):
        self.fill_text(self.SEARCH_FIELD, text)
        time.sleep(3)
        try:
            num = self.get_text(self.TASKS_TOTAL)
            if num == 0:
                return "There is 0 tasks found"
            else:
                return f"There was {num} tasks found for {text}"

        except Exception as e:
            return f"There was an error in search {e}"

    def last_tab(self):
        time.sleep(1)
        self.click_last_tab(self.TABS_LIST)
