import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function", autouse=True)
def setup(request):
    global driver
    driver = webdriver.Chrome()
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome()
    request.cls.driver = driver
    driver.maximize_window()
    driver.get("http://www.mytinytodo.net/demo/")
    yield
    driver.quit()

