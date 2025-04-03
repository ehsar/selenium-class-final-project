from selenium.webdriver.common.by import By
from locators.checkout import Locator
from utils.wait_utils import WaitUtils

class Checkout():
    def __init__(self, driver):
        self.driver = driver
        self.wait_utils = WaitUtils(driver)

    def get_shopping_cart_badge(self):
        shopping_cart_badge = self.driver.find_element(By.XPATH, Locator.SHOPPING_CART_BADGE_XPATH).text

        return shopping_cart_badge
    
    def get_title(self):
        title = self.driver.find_element(By.XPATH, Locator.TITLE_XPATH).text

        return title
    
    def get_complete_header(self):
        header = self.driver.find_element(By.XPATH, Locator.COMPLETE_HEADER_XPATH).text

        return header
    
    def get_total_cart_item(self):
        total = self.driver.find_elements(By.XPATH, Locator.LIST_ITEM_CART_XPATH)

        return len(total)

    def enter_information_credentials(self, first_name, last_name, postal_code):
        self.driver.find_element(By.ID, Locator.FIRST_NAME_TEXTBOX_ID).send_keys(first_name)
        self.driver.find_element(By.ID, Locator.LAST_NAME_TEXTBOX_ID).send_keys(last_name)
        self.driver.find_element(By.ID, Locator.POSTAL_CODE_TEXTBOX_ID).send_keys(postal_code)

    def click_continue(self):
        self.driver.find_element(By.ID, Locator.CONTINUE_BUTTON_ID).click()

    def click_finish(self):
        self.driver.find_element(By.ID, Locator.FINISH_BUTTON_ID).click()

    def click_shopping_cart(self):
        self.driver.find_element(By.XPATH, Locator.SHOPPING_CART_BADGE_XPATH).click()
    
    def click_checkout(self):
        self.driver.find_element(By.XPATH, Locator.CHECKOUT_BUTTON_XPATH).click()

    def click_back_to_home(self):
        self.driver.find_element(By.ID, Locator.BACK_TO_HOME_BUTTON_ID).click()