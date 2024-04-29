from selenium import  webdriver

from POM.pageobjects.new_tab_page import NewTabPage
from POM.pageobjects.tasks_page import TasksPage

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.mytinytodo.net/demo/")

p1 = TasksPage(driver)
p2 = NewTabPage(driver)
p2.new_list_create("test list")
p1.last_tab()
p1.fill_new_task(2, "15.05.22", "New Task 1", "Creating a new task, enter some text", "automation")
p1.fill_new_task(-1, "22.06.24", "New Task 2", "Another text ", "automation")
p2.number_of_tasks()
input("end ")
