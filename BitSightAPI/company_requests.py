from bitsightapi import BitSightSession


class CompanyRequests(BitSightSession):
    """
    Company Requests class
    """

    def __init__(self, path, **params):
        self.api_endpoint = '/v1/company-requests'
        self.api_paths = {
            'company requests': '/',
            'request status': '/%(requestguid)s'
        }
        self.api_params = {}
        pass