import pytest
from pages.menu import Menu
from pages.product import Product
from pages.checkout import Checkout
from pages.login import Login
import data.checkout as data_checkout
import data.config as data_config
from data.product import PRODUCTS, PRODUCT_TEST_CASES
from data.login import USERS, LOGIN_TEST_CASES

@pytest.mark.parametrize('case', LOGIN_TEST_CASES, ids=[tc['name'] for tc in LOGIN_TEST_CASES])
def test_login(driver, case):
    login     = Login(driver)
    user_data = USERS[case['user_key']]

    # Clear state
    driver.get(data_config.BASE_URL)

    login.enter_login_credentials(
        user_data.username,
        user_data.password
    )
    login.click_login()

    if user_data.expected_result == 'success':
        assert driver.current_url == case['expected_result']
    else:
        assert login.get_error_message() == case['expected_result']

@pytest.mark.parametrize('case', PRODUCT_TEST_CASES, ids=[tc['name'] for tc in PRODUCT_TEST_CASES])
def test_add_and_remove_from_cart(driver, case):
    product  = Product(driver)
    checkout = Checkout(driver)
    
    for i, product_key in enumerate(case['products_to_add']):
        product_data = PRODUCTS[product_key]
        product.click_add_to_cart(product_data.slug)
        assert checkout.get_shopping_cart_badge() == case['expected_counts'][i]
    
    for i, product_key in enumerate(case['products_to_remove'], start = len(case['products_to_add'])):
        product_data = PRODUCTS[product_key]
        product.click_remove_from_cart(product_data.slug)
        assert checkout.get_shopping_cart_badge() == case['expected_counts'][i]

def test_checkout_process(driver):
    checkout = Checkout(driver)
    
    checkout.click_shopping_cart()
    assert checkout.get_title() == data_config.CHECKOUT_YOUR_CART_TITLE
    
    checkout.click_checkout()
    assert checkout.get_title() == data_config.CHECKOUT_YOUR_INFORMATION_TITLE
    
    checkout.enter_information_credentials(
        data_checkout.INFORMATION['first_name'],
        data_checkout.INFORMATION['last_name'],
        data_checkout.INFORMATION['postal_code']
    )
    checkout.click_continue()
    
    assert checkout.get_title()           == data_config.CHECKOUT_OVERVIEW_TITLE
    assert checkout.get_total_cart_item() == 2
    
    checkout.click_finish()
    assert checkout.get_complete_header() == data_config.CHECKOUT_THANKYOU_TITLE

def test_logout(driver):
    menu       = Menu(driver)
    login_page = Login(driver)
    
    menu.click_menu()
    menu.click_logout()
    assert login_page.get_login_logo()