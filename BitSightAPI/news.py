from bitsightapi import BitSightSession


class News(BitSightSession):
    """
    News class
    """

    def __init__(self, path, **params):
        self.api_endpoint = '/v1/news'
        self.api_paths = {
            'news': '/'
        }
        self.api_params = {}
        pass