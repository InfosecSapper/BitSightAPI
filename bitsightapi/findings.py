from bitsightapi.client import Session


class Findings(Session):
    """
    Findings class
    """

    def __init__(self, session):
        self.api_key = session.api_key
        self.api_endpoint = '/v1/findings/wfh'
        self.api_variables = {}
        self.api_paths = {
            'root': '/'
        }
        self.api_params = [
            'ips',
            'date_interval',
            'risk_types',
            'limit',
            'offset'
        ]
