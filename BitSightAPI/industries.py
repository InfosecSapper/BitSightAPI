from bitsightapi import BitSightSession


class Industries(BitSightSession):
    """
    Industries class
    """

    def __init__(self, path, **params):
        self.api_endpoint = '/v1/industries'
        self.api_paths = {
            'industries': '/',
            'industry history': '/%(industry)s'
        }
        self.api_params = {}
        pass