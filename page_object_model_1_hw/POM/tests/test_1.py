from selenium import webdriver
import pytest

from POM.pages.base_page import BasePage
from POM.pages.wizard1_page import Wizard1


class Test_01:
    def test_01(self):
        global p1
        p1 = Wizard1(self.driver)
        p1.login("standard_user", "secret_sauce")
        url = p1.return_current_url()
        assert url == "https://www.saucedemo.com/inventory.html", "Pass"


