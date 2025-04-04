import pytest
from selenium import webdriver
import data.config as data_config

@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(data_config.BASE_URL)

    yield driver

    driver.quit()