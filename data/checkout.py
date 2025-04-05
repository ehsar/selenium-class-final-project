from dataclasses import dataclass
from typing import Dict
import data.config as data_config

@dataclass
class Information:
    first_name      : str
    last_name       : str
    postal_code     : str
    expected_result : str


INFORMATIONS: Dict[str, Information] = {
    'valid_information': Information(
        first_name      = 'Abu',
        last_name       = 'Jahal',
        postal_code     = '12345',
        expected_result = 'success'
    ),
    'empty_first_name': Information(
        first_name      = '',
        last_name       = 'Jahal',
        postal_code     = '12345',
        expected_result = 'error'
    ),
    'empty_last_name': Information(
        first_name      = 'Abu',
        last_name       = '',
        postal_code     = '12345',
        expected_result = 'error'
    ),
    'empty_postal_code': Information(
        first_name      = 'Abu',
        last_name       = 'Jahal',
        postal_code     = '',
        expected_result = 'error'
    )
}

INFORMATION_TEST_CASES = [
    {
        'name'            : 'Empty first name',
        'information_key' : 'empty_first_name',
        'expected_result' : data_config.FIRST_NAME_REQUIRED_MESSAGE
    },
    {
        'name'            : 'Empty last name',
        'information_key' : 'empty_last_name',
        'expected_result' : data_config.LAST_NAME_REQUIRED_MESSAGE
    },
    {
        'name'            : 'Empty postal code',
        'information_key' : 'empty_postal_code',
        'expected_result' : data_config.POSTAL_CODE_REQUIRED_MESSAGE
    },
    {
        'name'            : 'Valid information',
        'information_key' : 'valid_information',
        'expected_result' : data_config.CHECKOUT_OVERVIEW_TITLE,
    }
]