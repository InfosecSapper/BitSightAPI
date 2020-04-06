from bitsightapi.client import Session


class Tiers(Session):
    """
    Tiers class
    """

    def __init__(self, session):
        self.api_key = session.api_key
        self.api_endpoint = '/v1/tiers'
        self.api_paths = {
            'root': '/',
            'providers': '/%(tierguid)s/providers',
            'provider dependents': '/%(tierguid)s/providers/%(providerguid)s/companies',
            'provider products': '/%(tierguid)s/providers/%(providerguid)s/products'
        }
        self.api_params = {}
        pass