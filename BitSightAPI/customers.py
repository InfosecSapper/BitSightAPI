from bitsightapi.client import Session


class Customers(Session):
    """
    Customers class
    """

    def __init__(self, session, api_guid=''):
        self.api_key = session.api_key
        self.api_endpoint = '/v1/customers/current/api-tokens'
        self.api_variables = {
            'api_guid': api_guid
        }
        self.api_paths = {
            'root': '/'
        }
        self.api_params = [
            'data',
            'description',
            'format',
            'group'
        ]
