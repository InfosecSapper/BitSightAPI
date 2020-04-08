from BitSightAPI.client import Session


class Portfolio(Session):
    """
    Portfolio class
    """

    def __init__(self, session, company_guid='', user_guid=''):
        self.api_key = session.api_key
        self.api_endpoint = '/v1/portfolio'
        self.api_variables = {
            'company_guid': company_guid,
            'user_guid': user_guid
        }
        self.api_paths = {
            'root': '/',
            'breaches': '/beaches',
            'contacts': '/contacts',
            'edit contacts': '/contacts/%(user_guid)s',
            'custom ids': '/entity-custom-ids',
            'filters': '/filters',
            'guids': '/guids',
            'products': '/products',
            'providers': '/providers',
            'provider dependents': '/providers/%(company_guid)s/companies',
            'provider products': '/providers/%(company_guid)s/products',
            'ratings': '/ratings',
            'statistics': '/statistics'
        }
        self.api_params = [
            'company_guid',
            'custom_id',
            'email',
            'end',
            'exclude_alerts_only',
            'fields',
            'folder',
            'formal_name',
            'format',
            'friendly_name',
            'guid',
            'name',
            'phone_number',
            'quarters_back',
            'rating_date',
            'show_ips',
            'show_event_evidence',
            'start',
            'tier',
            'types'
        ]