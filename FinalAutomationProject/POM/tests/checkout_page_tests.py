import time

import pytest

from POM.pages.order_form_page import OrderFormPage
from POM.pages.finish_order_page import FinishOrderPage
from POM.pages.login_page import LoginPage
from POM.pages.main_page import MainPage
from POM.pages.product_page import ProductPage
from POM.pages.cart_page import CartPage
from POM.pages.finish_order_confirmation_page import FinishOrderConfirmationPage

@pytest.mark.usefixtures("setup")
class Test_CheckoutPage:

    def test_01(self):  # CheckoutPage: link to Your infornation
        p1 = LoginPage(self.driver)
        p1.standard_user_login()
        p2 = MainPage(self.driver)
        p2.click_on_product(4)
        p3 = ProductPage(self.driver)
        p3.add_to_cart()
        p3.click_on_cart()
        p4 = CartPage(self.driver)
        p4.checkout()
        p5 = OrderFormPage(self.driver)
        link = p5.get_current_url()
        assert "https://www.saucedemo.com/checkout-step-one.html" == link, "Error entering checkout process"

    def test_02(self): # click continue without filling form
        p1 = LoginPage(self.driver)
        p1.standard_user_login()
        p2 = MainPage(self.driver)
        p2.click_on_product(4)
        p3 = ProductPage(self.driver)
        p3.add_to_cart()
        p3.click_on_cart()
        p4 = CartPage(self.driver)
        p4.checkout()
        p5 = OrderFormPage(self.driver)
        p5.click_continue_btn()
        error_text = p5.error_text()
        assert "Error: First Name is required" in error_text, "Wrong error message"

    def test_03(self): # click continue without filling lastname
        p1 = LoginPage(self.driver)
        p1.standard_user_login()
        p2 = MainPage(self.driver)
        p2.click_on_product(4)
        p3 = ProductPage(self.driver)
        p3.add_to_cart()
        p3.click_on_cart()
        p4 = CartPage(self.driver)
        p4.checkout()
        p5 = OrderFormPage(self.driver)
        p5.fill_form("Alex","","")
        p5.click_continue_btn()
        error_text = p5.error_text()
        assert "Error: Last Name is required" in error_text, "Wrong error message"

    def test_04(self): # click continue without filling postal code
        p1 = LoginPage(self.driver)
        p1.standard_user_login()
        p2 = MainPage(self.driver)
        p2.click_on_product(4)
        p3 = ProductPage(self.driver)
        p3.add_to_cart()
        p3.click_on_cart()
        p4 = CartPage(self.driver)
        p4.checkout()
        p5 = OrderFormPage(self.driver)
        p5.fill_form("Alex","Yarovinsky","")
        p5.click_continue_btn()
        error_text = p5.error_text()
        assert "Error: Postal Code is required" in error_text, "Wrong error message"

    def test_05(self): # click continue without filling postal code
        p1 = LoginPage(self.driver)
        p1.standard_user_login()
        p2 = MainPage(self.driver)
        p2.click_on_product(4)
        p3 = ProductPage(self.driver)
        p3.add_to_cart()
        p3.click_on_cart()
        p4 = CartPage(self.driver)
        p4.checkout()
        p5 = OrderFormPage(self.driver)
        p5.cancel_btn()
        link = p5.get_current_url()
        assert "https://www.saucedemo.com/cart.html" == link, "Wrong page at clicking cancel btn"

