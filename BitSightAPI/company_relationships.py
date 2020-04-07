from bitsightapi.client import Session


class CompanyRelationships(Session):
    """
    Company Relationships class
    """

    def __init__(self, session):
        self.api_key = session.api_key
        self.api_endpoint = '/v1/company-relationships'
        self.api_variables = {}
        self.api_paths = {
            'root': '/'
        }
        self.api_params = [
            'company_guid',
            'relationship_type'
        ]
