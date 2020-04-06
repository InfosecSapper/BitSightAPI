from bitsightapi.client import Session


class Tiers(Session):
    """
    Tiers class
    """

    def __init__(self, session, tier_guid='', provider_guid=''):
        self.api_key = session.api_key
        self.api_endpoint = '/v1/tiers'
        self.api_variables = {
            'tier_guid': tier_guid,
            'provider_guid': provider_guid
        }
        self.api_paths = {
            'root': '/',
            'tiers': '/%(tier_guid)s',
            'companies': '/%(tier_guid)s/companies',
            'providers': '/%(tier_guid)s/providers',
            'provider dependents': '/%(tier_guid)s/providers/%(provider_guid)s/companies',
            'provider products': '/%(tier_guid)s/providers/%(provider_guid)s/products'
        }
        self.api_params = {}
