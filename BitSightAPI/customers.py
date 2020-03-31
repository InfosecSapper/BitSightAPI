from bitsightapi import BitSightSession


class Customers(BitSightSession):
    """
    Customers class
    """

    def __init__(self, path, **params):
        self.api_endpoint = '/v1/customers/current/api-tokens'
        self.api_paths = {
            'customers': '/'
        }
        self.api_params = {}
        pass