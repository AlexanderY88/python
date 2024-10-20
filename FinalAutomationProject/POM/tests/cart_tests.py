from POM.pages.order_form_page import OrderFormPage
from POM.pages.finish_order_page import FinishOrderPage
from POM.pages.login_page import LoginPage
from POM.pages.main_page import MainPage
from POM.pages.product_page import ProductPage
from POM.pages.cart_page import CartPage
from POM.pages.finish_order_confirmation_page import FinishOrderConfirmationPage


class Tests_Cart_Page:

    def test_01(self):  # Purchase process E2E
        p1 = LoginPage(self.driver)
        p1.login("standard_user", "secret_sauce")  # 1. login
        p2 = MainPage(self.driver)
        p2.click_on_product(2)  # 2. click on product
        p3 = ProductPage(self.driver)
        p3.add_to_cart()  # 3. add product to the cart
        p3.back_to_products_page()  # 4. back t the products page
        p2.click_on_product(3)  # 5. choose another product
        p3.add_to_cart()  # 6. add another product to the cart
        p3.back_to_products_page()  # 7. back to the products page
        p2.click_on_cart()  # 8. enter to the cart page
        p4 = CartPage(self.driver)  # 9. finish order
        p4.checkout()  # 10. fill form and cick continue
        p5 = OrderFormPage(self.driver)
        p5.fill_form("Alex", "Alexander", "123456")
        p6 = FinishOrderConfirmationPage(self.driver)  # 11. click on finish
        p6.finish_order()
        p7 = FinishOrderPage(self.driver)
        message = p7.message()  # 12. message at the finish process screen
        assert message == "Thank you for your order!", "Error"

    def test_02(self): #test_remove_product_from_cart
        p1 = LoginPage(self.driver)
        p1.login("standard_user", "secret_sauce")  # 1. login
        p2 = MainPage(self.driver)
        p2.click_on_product(2)  # 2. click on product
        p3 = ProductPage(self.driver)
        p3.add_to_cart()  # 3. add product to the cart
        p2.click_on_cart()  # 4. enter to the cart page
        p4 = CartPage(self.driver)
        p4.remove_first_product()  # 5. remove product from cart
        assert p4.is_cart_empty(), "Cart should be empty after removal"  # 6. verify cart is empty

    def test_03(self): #test_navigation_to_cart_page
        p1 = LoginPage(self.driver)
        p1.login("standard_user", "secret_sauce")  # 1. login
        p2 = MainPage(self.driver)
        p2.click_on_cart()  # 2. navigate to the cart page
        p4 = CartPage(self.driver)
        # Check if cart page elements are visible
        assert p4.cart_navigation_buttons(), "Checkout button or continue shopping button is not visible on the cart page"

    def test_04(self): #test_back_navigation_from_cart_page
        p1 = LoginPage(self.driver)
        p1.login("standard_user", "secret_sauce")  # 1. login
        p2 = MainPage(self.driver)
        p2.click_on_product(2)  # 2. click on a product
        p3 = ProductPage(self.driver)
        p3.add_to_cart()  # 3. add the product to the cart
        p2.click_on_cart()  # 4. navigate to the cart page
        p4 = CartPage(self.driver)
        p4.back_btn()  # 5. click on back button
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html", "Did not navigate back to the product page"

