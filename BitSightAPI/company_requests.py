from bitsightapi.client import Session


class CompanyRequests(Session):
    """
    Company Requests class
    """

    def __init__(self, session, data_object='', request_guid=''):
        self.api_key = session.api_key
        self.api_endpoint = '/v1/company-requests'
        self.api_variables = {
            'data_object': data_object,
            'request_guid': request_guid
        }
        self.api_paths = {
            'root': '/',
            'request status': '/%(request_guid)s'
        }
        self.api_params = []
