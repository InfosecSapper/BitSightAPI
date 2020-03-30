import requests
import json


class BitSightAPI(object):
    """
    This class provides a means to interact with the BitSight API.

    Only GET requests are currently supported, using the get_data()
    method. Query parameters are not implemented; rather the query
    response is returned as a JSON object for the user to manipulate
    according to their needs.
    """

    def __init__(self, key: str):
        """This is the class constructor.
        
        The class is instantiated with the user's API key as an
        argument of the type string.
        """

        self.api_key = key
        self.API_URL = 'https://api.bitsighttech.com/ratings'
        self.api_dict = {
            'overview': {'root': '/v1', 'actions': {'default': '/'}},
            'alerts': {'root': '/v2/alerts', 'actions': {
                'default': '/',
                'latest': '/latest'
                }},
            'companies': {'root': '/v1/companies', 'actions': {
                'default': '/',
                'basic': '/%(companyguid)s/',
                'asset risk matrix': '/%(companyguid)s/assets/statistics',
                'company tree': '/%(companyguid)s/company-tree',
                'ip by country': '/%(companyguid)s/countries',
                'products by domain': '/%(companyguid)s/domains/%(domain)s/products',
                'providers by domain': '/%(companyguid)s/domains/%(domain)s/providers',
                'findings': '/%(companyguid)s/findings',
                'industry statistics': '/%(companyguid)s/industries/statistics',
                'detailed': '/%(companyguid)s/observations',
                'pdf': '/%(companyguid)s/pdf',
                'products': '/%(companyguid)s/products',
                'service providers': '/%(companyguid)s/providers',
                'nist report': '/%(companyguid)s/regulatory/nist',
                'compare peers': '/%(companyguid)s/reports/company-preview',
                'infrastructure': '/%(companyguid)s/reports/infrastructure',
                'statistics': '/%(companyguid)s/observations/statistics',
                'distribution': '/distribution',
                'ratings by date': '/'
                }},
            'company requests': {'root': '/v1/company-requests', 'actions': {
                'default': '/',
                'request status': '/%(requestguid)s'
                }},
            'customers': {'root': '/v1/customers/current/api-tokens', 'actions': {
                'default': '/'
                }},
            'folders': {'root': '/v1/folders', 'actions': {
                'default': '/',
                'products': '/%(folderguid)s/products',
                'product types': '/%(folderguid)s/product-types',
                'providers': '/%(folderguid)s/providers',
                'provider products': '/%(folderguid)s/providers/%(providerguid)s/products'
                }},
            'industries': {'root': '/v1/industries', 'actions': {
                'default': '/',
                'industry history': '/%(industry)s'
                }},
            'news': {'root': '/v1/news', 'actions': {
                'default': '/'
                }},
            'portfolio': {'root': '/v1/portfolio', 'actions': {
                'default': '/',
                'breaches': '/beaches',
                'contacts': '/contacts',
                'custom ids': '/entity-custom-ids',
                'filters': '/filters',
                'guids': '/guids',
                'products': '/products',
                'providers': '/providers',
                'provider dependents': '/providers/%(providerguid)s/companies',
                'provider products': '/providers/%(providerguid)s/products'
                }},
            'products': {'root': '/v1/products', 'actions': {
                'default': '/'
                }},
            'subscriptions': {'root': '/v1/subscriptions', 'actions': {
                'default': '/',
                'expired': '/expired'
                }},
            'tiers': {'root': '/v1/tiers', 'actions': {
                'default': '/',
                'providers': '/%(tierguid)s/providers',
                'provider dependents': '/%(tierguid)s/providers/%(providerguid)s/companies',
                'provider products': '/%(tierguid)s/providers/%(providerguid)s/products'
                }},
            'users': {'root': '/v1/users', 'actions': {
                'default': '/',
                'user': '/%(userguid)s'
                }}
            }

    def test_connection(self):
        """This is a helper function to test connectivity to the API.

        It returns the HTTP status code if the status is 'OK', else it
        raises an error with the status code. See the Requests docs
        for more information.
        """

        status = requests.get(self.API_URL + '/v1', params=None, auth=(self.api_key, ''))
        if status.status_code != requests.codes.ok:
            status.raise_for_status()
        else:
            return status

    def get_data(self, endpoint='overview', action='default', alertguid='', companyguid='', domain='', folderguid='', industry='', providerguid='', requestguid='', risktypes='', tierguid='', userguid=''):
        """The get_data() method makes the call to the BitSight API.

        It receives query elements as arguments and returns a JSON
        object of the query response.
        """

        if endpoint not in self.api_dict:
            raise ValueError(
                "ERROR: endpoint must be one of %r." % self.api_dict
            )
        variables = {
            'alertguid': alertguid,
            'companyguid': companyguid,
            'domain': domain,
            'folderguid': folderguid,
            'industry': industry,
            'providerguid': providerguid,
            'risktypes': risktypes,
            'tierguid': tierguid,
            'userguid': userguid
        }
        url = self.API_URL + self.api_dict[endpoint]['root'] + self.api_dict[endpoint]['actions'][action] % variables
        return requests.get(url, auth=(self.api_key, '')).json()
