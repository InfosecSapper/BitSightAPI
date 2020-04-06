from bitsightapi.client import Session


class CompanyRelationships(Session):
    """
    Company Relationships class
    """

    def __init__(self, path, **params):
        self.api_endpoint = '/v1/company-relationships'
        self.api_paths = {
            'root': '/'
        }
        self.api_params = {}
        pass