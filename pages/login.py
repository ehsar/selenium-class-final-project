from selenium.webdriver.common.by import By
from locators.login import Locator
from utils.wait_utils import WaitUtils

class Login():
    def __init__(self, driver):
        self.driver = driver
        self.wait_utils = WaitUtils(driver)

    def get_login_logo(self):
        return self.wait_utils.check_element_exists(By.XPATH, Locator.LOGIN_LOGO_XPATH)

    def get_error_message(self):
        message = self.driver.find_element(By.XPATH, Locator.ERROR_MESSAGE_XPATH).text

        return message
    
    def enter_login_credentials(self, username, password):
        self.driver.find_element(By.ID, Locator.USERNAME_TEXTBOX_ID).send_keys(username)
        self.driver.find_element(By.ID, Locator.PASSWORD_TEXTBOX_ID).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, Locator.LOGIN_BUTTON_ID).click()

    def click_logout(self):
        self.driver.find_element(By.ID, ).click()