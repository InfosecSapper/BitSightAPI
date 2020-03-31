from bitsightapi import BitSightSession


class Tiers(BitSightSession):
    """
    Tiers class
    """

    def __init__(self, path, **params):
        self.api_endpoint = '/v1/tiers'
        self.api_paths = {
            'tiers': '/',
            'providers': '/%(tierguid)s/providers',
            'provider dependents': '/%(tierguid)s/providers/%(providerguid)s/companies',
            'provider products': '/%(tierguid)s/providers/%(providerguid)s/products'
        }
        self.api_params = {}
        pass