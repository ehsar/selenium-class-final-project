from selenium.webdriver.common.by import By
from locators.product import Locator
from utils.wait_utils import WaitUtils

class Product():
    def __init__(self, driver):
        self.driver = driver
        self.wait_utils = WaitUtils(driver)

    def get_title(self):
        title = self.driver.find_element(By.XPATH, Locator.PRODUCT_TITLE_XPATH).text

        return title

    def check_detail_product_name(self):
        return self.wait_utils.check_element_exists(By.XPATH, Locator.DETAIL_PRODUCT_NAME_XPATH)
    
    def check_detail_product_desc(self):
        return self.wait_utils.check_element_exists(By.XPATH, Locator.DETAIL_PRODUCT_DESC_XPATH)
    
    def check_detail_product_price(self):
        return self.wait_utils.check_element_exists(By.XPATH, Locator.DETAIL_PRODUCT_PRICE_XPATH)

    def click_add_to_cart(self, product_name):
        self.driver.find_element(By.ID, Locator.ADD_TO_CART_BUTTON_ID(product_name)).click()

    def click_remove_from_cart(self, product_name):
        self.driver.find_element(By.ID, Locator.REMOVE_FROM_CART_BUTTON_ID(product_name)).click()
    
    def click_product_name(self):
        self.driver.find_element(By.ID, Locator.PRODUCT_NAME_ID).click()
        
    def click_detail_add_to_cart(self):
        self.driver.find_element(By.ID, Locator.DETAIL_ADD_TO_CART_BUTTON_ID).click()