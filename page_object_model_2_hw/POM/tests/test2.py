from selenium import  webdriver

from POM.pageobjects.tasks_page import TasksPage

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.mytinytodo.net/demo/")

p1 = TasksPage(driver)
p1.click_a_tab(2)
p1.fill_new_task(2, "15.05.22", "New Task 1", "Creating a new task, enter some text", "automation")
p1.fill_new_task(-1, "22.06.24", "New Task 2", "Another text ", "automation")

input("End ")

