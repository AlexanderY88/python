from selenium import webdriver

from POM.pages.Wizard8_menu import Wizard8
from POM.pages.wisard5_page import Wizard5
from POM.pages.wisard7_page import Wizard7
from POM.pages.wizard1_page import Wizard1
from POM.pages.wizard2_page import Wizard2
from POM.pages.wizard3_page import Wizard3
from POM.pages.wizard4_page import Wizard4
from POM.pages.wizard6_page import Wizard6

class Test3:
    def test_03(self):
        # 1. login
        p1 = Wizard1(self.driver)
        p1.login("standard_user","secret_sauce")
        # 2. click on product
        p2 = Wizard2(self.driver)
        p2.click_on_product(2)
        # 3. add product to the cart
        p3 = Wizard3(self.driver)
        p3.add_to_cart()
        p3.click_on_cart()
        # cart page - remove first product
        p4 = Wizard4(self.driver)
        p4.remove_first_product()
        # click on checkout when no products in the cart
        p4.checkout()
        # there is a bug. I expected some error, but the site let me continue
        p5 = Wizard5(self.driver)
        p5.cancel_btn()
        p4.back_btn()
        p8 = Wizard8(self.driver)
        p8.logout()
        url = p1.return_current_url()
        assert url == "https://www.saucedemo.com/", "Error at log-out process"
