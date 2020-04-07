from bitsightapi.client import Session


class Industries(Session):
    """
    Industries class
    """

    def __init__(self, session, industry_slug=''):
        self.api_key = session.api_key
        self.api_endpoint = '/v1/industries'
        self.api_variables = {
            'industry_slug': industry_slug
        }
        self.api_paths = {
            'root': '/',
            'industry history': '/%(industry_slug)s'
        }
        self.api_params = []
