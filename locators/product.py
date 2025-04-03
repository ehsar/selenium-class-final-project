class Locator:
    # PRODUCTS
    ADD_TO_CART_BUTTON_ID      = lambda product_name: f'add-to-cart-{product_name}'
    REMOVE_FROM_CART_BUTTON_ID = lambda product_name: f'remove-{product_name}'
    PRODUCT_NAME_ID            = 'item_0_title_link'

    PRODUCT_TITLE_XPATH        = '//div[@class="header_secondary_container"]/span[@class="title"]'

    # DETAIL PRODUCT
    DETAIL_ADD_TO_CART_BUTTON_ID = 'add-to-cart'

    DETAIL_PRODUCT_NAME_XPATH    = '//div[@class="inventory_details_name large_size"]'
    DETAIL_PRODUCT_DESC_XPATH    = '//div[@class="inventory_details_desc large_size"]'
    DETAIL_PRODUCT_PRICE_XPATH   = '//div[@class="inventory_details_price"]'