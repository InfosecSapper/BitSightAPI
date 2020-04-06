from bitsightapi.client import Session


class Portfolio(Session):
    """
    Portfolio class
    """

    def __init__(self, session):
        self.api_key = session.api_key
        self.api_endpoint = '/v1/portfolio'
        self.api_variables = None
        self.api_paths = {
            'root': '/',
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