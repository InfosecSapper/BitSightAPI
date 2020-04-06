from bitsightapi.client import Session


class Users(Session):
    """
    Users class
    """

    def __init__(self, session):
        self.api_key = session.api_key
        self.api_endpoint = '/v1/users'
        self.api_paths = {
            'root': '/',
            'user': '/%(userguid)s'            
        }
        self.api_params = {}
        pass