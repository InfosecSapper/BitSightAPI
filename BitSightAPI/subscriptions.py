from bitsightapi.client import Session


class Subscriptions(Session):
    """
    Subscriptions class
    """

    def __init__(self, session):
        self.api_key = session.api_key
        self.api_endpoint = '/v1/subscriptions'
        self.api_paths = {
            'root': '/',
            'expired': '/expired'
        }
        self.api_params = {}
        pass