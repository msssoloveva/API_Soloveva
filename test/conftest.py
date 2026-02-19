import pytest
import requests

from test.data.json_for_post_registration import JsonForPostRegistration
# from test.data.json_for_registration import JsonForPostRegistration
# from delete_product import DeleteProduct
# from get_product import GetProduct
# from test.data.json_for_post import JsonForPost

@pytest.fixture
def obj_get_product():
    return GetProduct()