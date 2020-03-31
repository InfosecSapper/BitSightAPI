from bitsightapi import BitSightSession


class CompanyRelationships(BitSightSession):
    """
    Company Relationships class
    """

    def __init__(self, path, **params):
        self.api_endpoint = '/v1/company-relationships'
        self.api_paths = {
            'company relationships': '/'
        }
        self.api_params = {}
        pass