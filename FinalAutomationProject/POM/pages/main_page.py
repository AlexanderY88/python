from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from POM.pages.base_page import BasePage


# products page
class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # elements
    product_1 = (By.CSS_SELECTOR, "#item_0_title_link")
    product_1_price = (By.XPATH, "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div/text()[2]")
    product_2 = (By.CSS_SELECTOR, "#item_1_title_link")
    product_2_price = (By.XPATH, "//*[@id='inventory_container']/div/div[3]/div[2]/div[2]/div/text()[2]")
    product_3 = (By.CSS_SELECTOR, "#item_2_title_link")
    product_3_price = (By.XPATH, "//*[@id='inventory_container']/div/div[5]/div[2]/div[2]/div/text()[2]")
    product_4 = (By.CSS_SELECTOR, "#item_3_title_link")
    product_4_price = (By.XPATH, "//*[@id='inventory_container']/div/div[6]/div[2]/div[2]/div/text()[2]")
    product_5 = (By.CSS_SELECTOR, "#item_4_title_link")
    product_5_price = (By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div/text()[2]")
    product_6 = (By.CSS_SELECTOR, "#item_5_title_link")
    product_6_price = (By.XPATH, "//*[@id='inventory_container']/div/div[4]/div[2]/div[2]/div/text()[2]")
    CART_BTN = (By.CSS_SELECTOR, ".shopping_cart_link")

    PRODUCTS_PRICES_LIST = (By.CSS_SELECTOR, ".inventory_item_description > div.pricebar > div")
    PRODUCT_NAMES_LIST = (By.CSS_SELECTOR, ".inventory_item_name")
    NUM_OF_PRODUCTS_IN_CART = (By.CSS_SELECTOR, "#shopping_cart_container > a > span")

    def click_on_specific_product(self, option):
        match option:
            case 1:
                self.click(self.product_1)
            case 2:
                self.click(self.product_2)
            case 3:
                self.click(self.product_3)
            case 4:
                self.click(self.product_4)
            case 5:
                self.click(self.product_5)
            case 6:
                self.click(self.product_6)
            case _:
                print("No product chosen")

    def return_price_main_page(self, option):
        match option:
            case 1:
                price = self.get_text(self.product_1_price)
                return price
            case 2:
                price = self.get_text(self.product_2_price)
                return price
            case 3:
                price = self.get_text(self.product_3_price)
                return price
            case 4:
                price = self.get_text(self.product_4_price)
                return price
            case 5:
                price = self.get_text(self.product_5_price)
                return price
            case 6:
                price = self.get_text(self.product_6_price)
                return price
            case _:
                print("No product chosen")

    def click_on_cart(self):
        self.click(self.CART_BTN)

    def get_all_product_names(self) -> list:
        try:
            product_elements = self.driver.find_elements(*self.PRODUCT_NAMES_LIST)
            product_names = [element.text for element in product_elements]
            return product_names
        except NoSuchElementException:
            # Return an empty list if no elements are found
            return []

    def check_product_name(self, num_of_element: int) -> str:
        try:
            # Ensure the index is within range and get the product name
            if 0 <= num_of_element < len(self.PRODUCT_NAMES_LIST):
                product_name = self.PRODUCT_NAMES_LIST[num_of_element].text
                return product_name
            else:
                raise IndexError("Product index is out of range.")
        except NoSuchElementException:
            return ""
        except IndexError as e:
            return ""

    def click_on_product(self, num_of_element: int):
        try:
            product_elements = self.driver.find_elements(*self.PRODUCT_NAMES_LIST)
            if 0 <= num_of_element < len(product_elements):
                product_elements[num_of_element].click()
                return True
            else:
                raise IndexError("Product index is out of range.")
        except NoSuchElementException:
            return False

    def check_product_price(self, num_of_element: int) -> str:
        try:
            # Ensure the index is within range and get the product name
            if 0 <= num_of_element < len(self.PRODUCTS_PRICES_LIST):
                product_price = self.PRODUCTS_PRICES_LIST[num_of_element].text
                return product_price
            else:
                raise IndexError("Product index is out of range.")
        except NoSuchElementException:
            return ""
        except IndexError as e:
            return ""

    def get_link(self):
        link = self.get_url()
        return link

    def items_in_shopping_cart(self):
        try:
            num = self.get_text(self.NUM_OF_PRODUCTS_IN_CART)
            return num
        except (ValueError, NoSuchElementException) as e:
            num = "0"
            return num
