from POM.pages.order_form_page import OrderFormPage
from POM.pages.finish_order_page import FinishOrderPage
from POM.pages.login_page import LoginPage
from POM.pages.main_page import MainPage
from POM.pages.product_page import ProductPage
from POM.pages.cart_page import CartPage
from POM.pages.finish_order_confirmation_page import FinishOrderConfirmationPage


class Test_FinishProcess:

    def test_01(self):  # buy  product E2E
        p1 = LoginPage(self.driver)
        p1.login("standard_user", "secret_sauce")  # 1. login
        p2 = MainPage(self.driver)
        p2.click_on_product(2)
        p3 = ProductPage(self.driver)
        p3.add_to_cart()
        p3.click_on_cart()
        p4 = CartPage(self.driver)
        p4.checkout()
        p5 = OrderFormPage(self.driver)
        p5.fill_form("Alex", "Alexander", "123456")
        p6 = FinishOrderConfirmationPage(self.driver)
        p6.finish_order()
        p7 = FinishOrderPage(self.driver)
        message = p7.message()
        assert message == "Thank you for your order!", "Error"

    def test_02(self): # cancel btn
        p1 = LoginPage(self.driver)
        p1.standard_user_login()
        p2 = MainPage(self.driver)
        p2.click_on_product(2)
        p3 = ProductPage(self.driver)
        p3.add_to_cart()
        p3.click_on_cart()
        p4 = CartPage(self.driver)
        p4.checkout()
        p5 = OrderFormPage(self.driver)
        p5.fill_form("Alex", "Alexander", "123456")
        p6 = FinishOrderConfirmationPage(self.driver)
        p6.cancel_order()
        link = p2.get_link()
        assert "https://www.saucedemo.com/inventory.html" == link, "Wrong url button cancel order"

    def test_03(self): # check the step-2 age url
        p1 = LoginPage(self.driver)
        p1.standard_user_login()
        p2 = MainPage(self.driver)
        p2.click_on_product(5)
        p3 = ProductPage(self.driver)
        p3.add_to_cart()
        p3.click_on_cart()
        p4 = CartPage(self.driver)
        p4.checkout()
        p5 = OrderFormPage(self.driver)
        p5.fill_form("Alex", "Alexander", "123456")
        p6 = FinishOrderConfirmationPage(self.driver)
        link = p6.get_link()
        assert "https://www.saucedemo.com/checkout-step-two.html" == link, "Wrong url at step 2"

    def test_04(self): # back home btn
        p1 = LoginPage(self.driver)
        p1.standard_user_login()
        p2 = MainPage(self.driver)
        p2.click_on_product(2)
        p3 = ProductPage(self.driver)
        p3.add_to_cart()
        p3.click_on_cart()
        p4 = CartPage(self.driver)
        p4.checkout()
        p5 = OrderFormPage(self.driver)
        p5.fill_form("Alex", "Alexander", "123456")
        p6 = FinishOrderConfirmationPage(self.driver)
        p6.finish_order()
        p7 = FinishOrderPage(self.driver)
        p7.back_home_btn()
        link = p2.get_link()
        assert "https://www.saucedemo.com/inventory.html" == link, "Error back to home screen"

