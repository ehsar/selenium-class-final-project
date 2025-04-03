import pytest
from selenium import webdriver
from pages.login import Login
import data.login as data_login
import data.config as data_config

@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver

    driver.quit()

@pytest.fixture
def login(driver):
    driver.get(data_config.BASE_URL)
    login_page = Login(driver)
    login_page.enter_login_credentials(
        data_login.CREDENTIAL['username'],
        data_login.CREDENTIAL['password']
    )
    login_page.click_login()
    yield driver
    
    driver.get(data_config.INVENTORY_URL)