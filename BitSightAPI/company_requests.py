from bitsightapi.client import Session


class CompanyRequests(Session):
    """
    Company Requests class
    """

    def __init__(self, session):
        self.api_key = session.api_key
        self.api_endpoint = '/v1/company-requests'
        self.api_variables = None
        self.api_paths = {
            'root': '/',
            'request status': '/%(requestguid)s'
        }
        self.api_params = {}
        pass