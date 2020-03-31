from bitsightapi import BitSightSession


class Portfolio(BitSightSession):
    """
    Portfolio class
    """

    def __init__(self, path, **params):
        self.api_endpoint = '/v1/portfolio'
        self.api_paths = {
            'portfolio': '/',
            'breaches': '/beaches',
            'contacts': '/contacts',
            'custom ids': '/entity-custom-ids',
            'filters': '/filters',
            'guids': '/guids',
            'products': '/products',
            'providers': '/providers',
            'provider dependents': '/providers/%(providerguid)s/companies',
            'provider products': '/providers/%(providerguid)s/products'
        }
        self.api_params = {}
        pass