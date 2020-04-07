from bitsightapi.client import Session


class Reports(Session):
    """
    Reports class
    """

    def __init__(self, session):
        self.api_key = session.api_key
        self.api_endpoint = '/v1/reports'
        self.api_variables = {}
        self.api_paths = {
            'root': '/'
        }
        self.api_params = [
            'company'
        ]
