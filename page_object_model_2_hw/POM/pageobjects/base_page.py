import time

from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def click(self, locator):
        time.sleep(0.5)
        self.driver.find_element(*locator).click()

    def fill_text(self, locator, txt: str) -> None:
        el = self.driver.find_element(*locator)
        el.clear()
        el.send_keys(txt)

    def get_text(self, locator) -> str:
        return self.driver.find_element(*locator).text

    def click_tab(self, locator, num):
        tab_index = num - 1
        tabs_list = self.driver.find_elements(*locator)
        #print("Number of tabs:", len(tabs_list))
        #print("Requested tab index:", tab_index)
        if tab_index < 0:
            print("Invalid tab index: Negative value")
        elif tab_index >= len(tabs_list):
            print("Invalid tab index: Out of range")
        else:
            tabs_list[tab_index].click()


    def click_last_tab(self, locator):
        tabs_list = self.driver.find_elements(*locator)
        tab_index = len(tabs_list) - 1
        #print("The last tab:", tab_index)
        #print("Requested tab index:", tab_index)
        if tab_index < 0:
            print("Invalid tab index: Negative value")
        elif tab_index >= len(tabs_list):
            print("Invalid tab index: Out of range")
        else:
            tabs_list[tab_index].click()
