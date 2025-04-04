from dataclasses import dataclass
from typing import Dict
import data.config as data_config

@dataclass
class User:
    username        : str
    password        : str
    expected_result : str

USERS: Dict[str, User] = {
    'standard_user': User(
        username        = 'standard_user',
        password        = 'secret_sauce',
        expected_result = 'success'
    ),
    'locked_out_user': User(
        username        = 'locked_out_user',
        password        = 'secret_sauce',
        expected_result = 'error'
    ),
    'invalid_user': User(
        username        = 'invalid_user',
        password        = 'secret_sauce',
        expected_result = 'error'
    ),
}

LOGIN_TEST_CASES = [
    {
        'name'            : 'Locked out user',
        'user_key'        : 'locked_out_user',
        'expected_result' : data_config.LOCKED_OUT_USER_MESSAGE
    },
    {
        'name'            : 'Invalid user',
        'user_key'        : 'invalid_user',
        'expected_result' : data_config.INVALID_USER_MESSAGE
    },
    {
        'name'            : 'Valid standard user',
        'user_key'        : 'standard_user',
        'expected_result' : data_config.INVENTORY_URL
    }
]