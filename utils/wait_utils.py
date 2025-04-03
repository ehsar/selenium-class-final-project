from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WaitUtils:
    def __init__(self, driver):
        self.driver = driver

    def check_element_exists(self, by_type, locator):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((by_type, locator))
            )

            return True
        except:
            print(f"Element with locator '{locator}' not found.")

            return False

