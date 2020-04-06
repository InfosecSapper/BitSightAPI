from bitsightapi.client import Session


class Customers(Session):
    """
    Customers class
    """

    def __init__(self, session):
        self.api_key = session.api_key
        self.api_endpoint = '/v1/customers/current/api-tokens'
        self.api_variables = None
        self.api_paths = {
            'root': '/'
        }
        self.api_params = {}
        pass