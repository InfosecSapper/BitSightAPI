from bitsightapi import BitSightSession


class Subscriptions(BitSightSession):
    """
    Subscriptions class
    """

    def __init__(self, path, **params):
        self.api_endpoint = '/v1/subscriptions'
        self.api_paths = {
            'subscriptions': '/',
            'expired': '/expired'
        }
        self.api_params = {}
        pass