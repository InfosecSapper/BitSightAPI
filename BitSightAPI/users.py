from bitsightapi import BitSightSession


class Users(BitSightSession):
    """
    Users class
    """

    def __init__(self, path, **params):
        self.api_endpoint = '/v1/users'
        self.api_paths = {
            'users': '/',
            'user': '/%(userguid)s'            
        }
        self.api_params = {}
        pass