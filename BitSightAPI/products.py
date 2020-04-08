from BitSightAPI.client import Session


class Products(Session):
    """
    Products class
    """

    def __init__(self, session, product_guid=''):
        self.api_key = session.api_key
        self.api_endpoint = '/v1/products'
        self.api_variables = {
            'product_guid': product_guid
        }
        self.api_paths = {
            'root': '/%(product_guid)s/companies'
        }
        self.api_params = []
