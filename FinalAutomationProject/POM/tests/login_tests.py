import pytest


from POM.pages.login_page import LoginPage


@pytest.mark.usefixtures("setup")
class TestLogIn:

    def test_01(self): # Pass a valid username and correct password
        global p1
        p1 = LoginPage(self.driver)
        p1.login("standard_user", "secret_sauce")
        url = p1.return_current_url()
        assert url == "https://www.saucedemo.com/inventory.html", "Pass"

    def test_02(self):   # Pass an empty username and  correct password
        p1 = LoginPage(self.driver)
        p1.login("", "secret_sauce")
        error_msg = p1.get_error_message()
        expected_error_msg = "Epic sadface: Username is required"
        assert error_msg == expected_error_msg, f"Expected error message: '{expected_error_msg}', but got: '{error_msg}'"

    def test_03(self):   # Pass a valid username and an empty password
        p1 = LoginPage(self.driver)
        p1.login("standard_user", "")
        error_msg = p1.get_error_message()
        expected_error_msg = "Epic sadface: Password is required"
        assert error_msg == expected_error_msg, f"Expected error message: '{expected_error_msg}', but got: '{error_msg}'"

    def test_04(self): # # Pass a valid username and an incorrect password
        p1 = LoginPage(self.driver)
        p1.login("standard_user", "wrong_password")
        error_msg = p1.get_error_message()
        expected_error_msg = "Epic sadface: Username and password do not match any user in this service"
        assert error_msg == expected_error_msg, f"Expected error message: '{expected_error_msg}', but got: '{error_msg}'"

    def test_05(self):  # Pass a valid password and an incorrect username
        p1 = LoginPage(self.driver)
        p1.login("wrong_username", "secret_sauce")
        error_msg = p1.get_error_message()
        expected_error_msg = "Epic sadface: Username and password do not match any user in this service"
        assert error_msg == expected_error_msg, f"Expected error message: '{expected_error_msg}', but got: '{error_msg}'"

    def test_06(self): # Pass empty username and empty password
        p1 = LoginPage(self.driver)
        p1.login("", "")
        error_msg = p1.get_error_message()
        expected_error_msg = "Epic sadface: Username is required"
        assert error_msg == expected_error_msg, f"Expected error message: '{expected_error_msg}', but got: '{error_msg}'"

    def test_07(self): # Pass a valid username and an incorrect password
        p1 = LoginPage(self.driver)
        p1.login("standard_123", "wrong_password")
        error_msg = p1.get_error_message()
        expected_error_msg = "Epic sadface: Username and password do not match any user in this service"
        assert error_msg == expected_error_msg, f"Expected error message: '{expected_error_msg}', but got: '{error_msg}'"