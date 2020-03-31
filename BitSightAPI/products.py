from bitsightapi import BitSightSession


class Products(BitSightSession):
    """
    Products class
    """

    def __init__(self, path, **params):
        self.api_endpoint = '/v1/products'
        self.api_paths = {
            'products': '/'
        }
        self.api_params = {}
        pass