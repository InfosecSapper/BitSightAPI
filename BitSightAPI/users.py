from bitsightapi.client import Session


class Users(Session):
    """
    Users class
    """

    def __init__(self, session, user_guid=''):
        self.api_key = session.api_key
        self.api_endpoint = '/v1/users'
        self.api_variables = {
            'user_guid': user_guid
        }
        self.api_paths = {
            'root': '/',
            'user': '/%(user_guid)s',
            'company views': '/%(user_guid)s/company-views'
        }
        self.api_params = [
            'include_details',
            'show_all',
            'view_company',
            'days_back',
            'limit',
            'folder'
        ]
