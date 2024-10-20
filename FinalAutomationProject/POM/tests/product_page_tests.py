from selenium import webdriver

from POM.pages.order_form_page import OrderFormPage
from POM.pages.finish_order_page import FinishOrderPage
from POM.pages.login_page import LoginPage
from POM.pages.main_page import MainPage
from POM.pages.product_page import ProductPage
from POM.pages.cart_page import CartPage
from POM.pages.finish_order_confirmation_page import FinishOrderConfirmationPage


class Test_ProductPage:

    def test_01(self):  # check price appears on the page
        p1 = LoginPage(self.driver)  # 1. login
        p1.login("standard_user", "secret_sauce")
        p2 = MainPage(self.driver)
        p2.click_on_specific_product(2)
        p3 = ProductPage(self.driver)
        price2 = p3.get_product_price
        assert price2 != "", "Product price mismatch"

    def test_02(self):  # check product name appears on the page
        p1 = LoginPage(self.driver)  # 1. login
        p1.login("standard_user", "secret_sauce")
        p2 = MainPage(self.driver)
        p2.click_on_specific_product(2)
        p3 = ProductPage(self.driver)
        name = p3.get_product_name
        assert name != "", "Product name mismatch"

    def test_03(self):  # check via link opening product page and not cart or other page
        p1 = LoginPage(self.driver)  # 1. login
        p1.login("standard_user", "secret_sauce")
        p2 = MainPage(self.driver)
        p2.click_on_specific_product(2)
        p3 = ProductPage(self.driver)
        link = p3.get_link()
        assert "https://www.saucedemo.com/inventory-item.html?id=" in link, "Product page not opening"

    def test_04(self):  # checks the curt button appearing
        p1 = LoginPage(self.driver)  # 1. login
        p1.login("standard_user", "secret_sauce")
        p2 = MainPage(self.driver)
        p2.click_on_specific_product(2)
        p3 = ProductPage(self.driver)
        p3.add_to_cart()
        number = p3.items_in_cart()
        assert number == "1", "Click add to cart button did not update the cart correctly"

    def test_05(self):  # checks the curt button appearing
        p1 = LoginPage(self.driver)  # 1. login
        p1.login("standard_user", "secret_sauce")
        p2 = MainPage(self.driver)
        p2.click_on_specific_product(2)
        p3 = ProductPage(self.driver)
        p3.add_to_cart()
        number = p3.items_in_cart()
        assert number == "1", "Item was not added to the cart correctly"
        p3.click_remove_btn()
        number2 = p3.items_in_cart()
        assert number2 == "", "Item was not removed from the cart correctly"
