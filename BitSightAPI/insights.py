from bitsightapi.client import Session


class Insights(Session):
    """
    Insights class
    """

    def __init__(self, session):
        self.api_key = session.api_key
        self.api_endpoint = '/v1/insights'
        self.api_variables = {}
        self.api_paths = {
            'root': '/'
        }
        self.api_params = [
            'company',
            'start',
            'end',
            'format',
            'score_delta_lt'
        ]
