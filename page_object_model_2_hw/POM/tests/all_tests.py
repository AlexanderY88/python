from POM.pageobjects.new_tab_page import NewTabPage
from POM.pageobjects.tasks_page import TasksPage


class Test:

    def test_01(self):
        global p1
        p1 = TasksPage(self.driver)
        p1.click_a_tab(2)
        test = p1.add_simple_task("Make a coffee")
        assert "pass" in test, "Test failed"

    def test_02(self):
        p1 = TasksPage(self.driver)
        p1.click_a_tab(2)
        p1.fill_new_task(2, "15.05.22", "New Task 1", "Creating a new task, enter some text", "automation")
        tasks_counter = p1.fill_new_task(-1, "22.06.24", "New Task 2", "Another text ", "automation")
        assert "pass" in tasks_counter, "Test failed"

    def test_03(self):
        p1 = TasksPage(self.driver)
        p1.click_a_tab(2)
        tasks = p1.search_and_print("task")
        assert "error" not in tasks, "Test failed"



    def test_04(self):
        p1 = TasksPage(self.driver)
        p2 = NewTabPage(self.driver)
        p2.new_list_create("test list")
        p1.last_tab()
        p1.fill_new_task(2, "15.05.22", "New Task 1", "Creating a new task, enter some text", "automation")
        p1.fill_new_task(-1, "22.06.24", "New Task 2", "Another text ", "automation")
        num_of_tasks = p2.number_of_tasks()
        assert "error" not in num_of_tasks, "Test failed"


