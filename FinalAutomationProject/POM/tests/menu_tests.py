from POM.pages.menu import Menu
from POM.pages.order_form_page import OrderFormPage
from POM.pages.finish_order_page import FinishOrderPage
from POM.pages.login_page import LoginPage
from POM.pages.main_page import MainPage
from POM.pages.product_page import ProductPage
from POM.pages.cart_page import CartPage
from POM.pages.finish_order_confirmation_page import FinishOrderConfirmationPage


class Tests_menu:

    def test_01(self):  # click logout
        p1 = LoginPage(self.driver)
        p1.standard_user_login()
        p2 = Menu(self.driver)
        p2.open_menu()
        p2.click_logout()
        link = p2.get_link()
        assert "https://www.saucedemo.com/" == link, "Navigation to \"about\" link error"

    def test_02(self):  # click all items
        p1 = LoginPage(self.driver)
        p1.standard_user_login()
        p2 = MainPage(self.driver)
        p2.click_on_product(2)
        p3 = Menu(self.driver)
        p3.open_menu()
        p3.click_all_items()
        link = p2.get_link()
        assert "https://www.saucedemo.com/inventory.html" == link, "Navigation to \"all items page\" link error"


    def test_03(self):  # navigate from cart to main page
        p1 = LoginPage(self.driver)
        p1.login("standard_user", "secret_sauce")  # 1. login
        p2 = MainPage(self.driver)
        p2.click_on_product(2)
        p3 = ProductPage(self.driver)
        p3.add_to_cart()
        p2.click_on_cart()  # navigate to the cart page
        p5 = Menu(self.driver)
        p5.open_menu()
        p5.click_all_items()
        link = p2.get_link()
        assert "https://www.saucedemo.com/inventory.html" == link, "Navigation to \"all items page\" link error"


