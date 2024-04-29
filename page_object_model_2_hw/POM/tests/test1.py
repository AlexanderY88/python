import time

from selenium import  webdriver

from POM.pageobjects.tasks_page import TasksPage

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.mytinytodo.net/demo/")

p1 = TasksPage(driver)
p1.click_a_tab(3)
p1.add_simple_task("Make a coffee")


input("END ")

