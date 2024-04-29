from selenium import webdriver
import pytest

from POM.pages.base_page import BasePage
from POM.pages.wisard5_page import Wizard5
from POM.pages.wisard7_page import Wizard7
from POM.pages.wizard1_page import Wizard1
from POM.pages.wizard2_page import Wizard2
from POM.pages.wizard3_page import Wizard3
from POM.pages.wizard4_page import Wizard4
from POM.pages.wizard6_page import Wizard6


class Test:
    def test_01(self):
        # log-in
        global p1
        p1 = Wizard1(self.driver)
        p1.login("standard_user", "secret_sauce")
        url = p1.return_current_url()
        assert url == "https://www.saucedemo.com/inventory.html", "Pass"

    def test_02(self):
        # Purchase process E2E
        # 1. login
        p1 = Wizard1(self.driver)
        p1.login("standard_user", "secret_sauce")
        # 2. click on product
        p2 = Wizard2(self.driver)
        p2.click_on_product(2)
        # 3. add product to the cart
        p3 = Wizard3(self.driver)
        p3.add_to_cart()
        # 4. back t the products page
        p3.back_to_products_page()
        # 5. choose another product
        p2.click_on_product(3)
        # 6. add another product to the cart
        p3.add_to_cart()
        # 7. back to the products page
        p3.back_to_products_page()
        # 8. enter to the cart page
        p2.click_on_cart()
        # 9. finish order
        p4 = Wizard4(self.driver)
        p4.checkout()
        # fill form and cick continue
        p5 = Wizard5(self.driver)
        p5.fill_form("Alex", "Alexander", "123456")
        # click on finish
        p6 = Wizard6(self.driver)
        p6.finish_order()
        p7 = Wizard7(self.driver)
        message = p7.message()
        print(message)
        assert message == "Thank you for your order!", "Error"

    def test_03(self):
        # error - empty password
        p1 = Wizard1(self.driver)
        error_msg = p1.login("standard_user", "")
        assert error_msg == "Epic sadface: Password is required", "Error at validation - empty password"

    def test_04(self):
        # error - empty password
        p1 = Wizard1(self.driver)
        error_msg = p1.login("standard_user", "qwerty123")
        assert error_msg == "Epic sadface: Username and password do not match any user in this service", "Error at validation - wrong password"

    def test_05(self):
        # error - empty password and username
        p1 = Wizard1(self.driver)
        error_msg = p1.login("", "qwerty123")
        assert error_msg == "Epic sadface: Username is required", "Error at validation - wrong password"

    def test_06(self):
        # error - wrong password and username
        p1 = Wizard1(self.driver)
        error_msg = p1.login("123123", "qwerty123")
        assert error_msg == "Epic sadface: Username and password do not match any user in this service", "Error at validation - wrong password"

    def test_07(self):
        # Test failed for example
        p1 = Wizard1(self.driver)
        error_msg = p1.login("standard_user", "secret_sauce")
        assert error_msg == "Epic sadface: Username and password do not match any user in this service", "Error at validation - wrong password"
