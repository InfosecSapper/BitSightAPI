from bitsightapi.client import Session


class Products(Session):
    """
    Products class
    """

    def __init__(self, session):
        self.api_key = session.api_key
        self.api_endpoint = '/v1/products'
        self.api_paths = {
            'root': '/'
        }
        self.api_params = {}
        pass