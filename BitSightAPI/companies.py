from bitsightapi.client import Session


class Companies(Session):
    """
    Companies class
    """

    def __init__(self, session, companyguid='', domain=''):
        self.api_key = session.api_key
        self.api_endpoint = '/v1/companies'
        self.api_variables = {
            'companyguid': companyguid,
            'domain': domain
        }
        self.api_paths = {
            'root': '/',
            'company details': '/%(companyguid)s/',
            'asset risk matrix': '/%(companyguid)s/assets/statistics',
            'company tree': '/%(companyguid)s/company-tree',
            'ip by country': '/%(companyguid)s/countries',
            'products by domain': '/%(companyguid)s/domains/%(domain)s/products',
            'providers by domain': '/%(companyguid)s/domains/%(domain)s/providers',
            'findings': '/%(companyguid)s/findings',
            'industry statistics': '/%(companyguid)s/industries/statistics',
            'detailed': '/%(companyguid)s/observations',
            'products': '/%(companyguid)s/products',
            'service providers': '/%(companyguid)s/providers',
            'nist report': '/%(companyguid)s/regulatory/nist',
            'compare peers': '/%(companyguid)s/reports/company-preview',
            'infrastructure': '/%(companyguid)s/reports/infrastructure',
            'statistics': '/%(companyguid)s/observations/statistics',
            'distribution': '/distribution',
            'ratings by date': '/'
        }
        self.api_params = {}