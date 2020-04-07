from bitsightapi.client import Session


class Companies(Session):
    """
    Companies class
    """

    def __init__(self, session, company_guid='', domain=''):
        self.api_key = session.api_key
        self.api_endpoint = '/v1/companies'
        self.api_variables = {
            'company_guid': company_guid,
            'domain': domain
        }
        self.api_paths = {
            'root': '/',
            'company details': '/%(company_guid)s/',
            'asset risk matrix': '/%(company_guid)s/assets/statistics',
            'company tree': '/%(company_guid)s/company-tree',
            'ip by country': '/%(company_guid)s/countries',
            'products by domain': '/%(company_guid)s/domains/%(domain)s/products',
            'providers by domain': '/%(company_guid)s/domains/%(domain)s/providers',
            'findings': '/%(company_guid)s/findings',
            'industry statistics': '/%(company_guid)s/industries/statistics',
            'detailed': '/%(company_guid)s/observations',
            'products': '/%(company_guid)s/products',
            'service providers': '/%(company_guid)s/providers',
            'nist report': '/%(company_guid)s/regulatory/nist',
            'compare peers': '/%(company_guid)s/reports/company-preview',
            'infrastructure': '/%(company_guid)s/reports/infrastructure',
            'statistics': '/%(company_guid)s/observations/statistics',
            'distribution': '/distribution',
            'ratings by date': '/'
        }
        self.api_params = [
            'fields',
            'limit',
            'offset',
            'q',
            'sort'
        ]
