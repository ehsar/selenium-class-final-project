from dataclasses import dataclass
from typing import Dict

@dataclass
class Product:
    name : str
    slug : str

PRODUCTS: Dict[str, Product] = {
    'backpack': Product(
        name = 'Sauce Labs Backpack',
        slug = 'sauce-labs-backpack'
    ),
    'bike_light': Product(
        name = 'Sauce Labs Bike Light',
        slug = 'sauce-labs-bike-light'
    ),
    'bolt_tshirt': Product(
        name = 'Sauce Labs Bolt T-Shirt',
        slug = 'sauce-labs-bolt-t-shirt'
    ),
    'fleece_jacket': Product(
        name = 'Sauce Labs Fleece Jacket',
        slug = 'sauce-labs-fleece-jacket'
    )
}

TEST_CASES = [
    {
        'name'                  : 'Add two products then remove one',
        'products_to_add'       : ['backpack', 'bike_light'],
        'products_to_remove'    : ['backpack'],
        'expected_counts'       : ['1', '2', '1']
    },
    {
        'name'                  : 'Add three products then remove two',
        'products_to_add'       : ['backpack', 'fleece_jacket', 'bolt_tshirt'],
        'products_to_remove'    : ['backpack', 'bolt_tshirt'],
        'expected_counts'       : ['2', '3', '4', '3', '2']
    }
]