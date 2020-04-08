from BitSightAPI.client import Session


class News(Session):
    """
    News class
    """

    def __init__(self, session):
        self.api_key = session.api_key
        self.api_endpoint = '/v1/news'
        self.api_variables = {}
        self.api_paths = {
            'root': '/'
        }
        self.api_params = [
            'sort',
            'limit',
            'offset',
            'show_on_dashboard'
        ]
