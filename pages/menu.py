from selenium.webdriver.common.by import By
from locators.menu import Locator
from utils.wait_utils import WaitUtils

class Menu():
    def __init__(self, driver):
        self.driver = driver
        self.wait_utils = WaitUtils(driver)

    def click_menu(self):
        self.driver.find_element(By.ID, Locator.BURGER_BUTTON_ID).click()

    def click_logout(self):
        self.driver.find_element(By.ID, Locator.LOGOUT_BUTTON_ID).click()