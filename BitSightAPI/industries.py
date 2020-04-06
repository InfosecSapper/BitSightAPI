from bitsightapi.client import Session


class Industries(Session):
    """
    Industries class
    """

    def __init__(self, session):
        self.api_key = session.api_key
        self.api_endpoint = '/v1/industries'
        self.api_paths = {
            'root': '/',
            'industry history': '/%(industry)s'
        }
        self.api_params = {}
        pass