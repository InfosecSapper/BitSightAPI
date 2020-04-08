from BitSightAPI.client import Session


class RapidUnderwritingAssessments(Session):
    """
    Rapid Underwriting Assessments class
    """

    def __init__(self, session):
        self.api_key = session.api_key
        self.api_endpoint = '/v1/fast-ratings'
        self.api_variables = {}
        self.api_paths = {
            'root': '/'
        }
        self.api_params = [
            'generate_report',
            'industry',
            'url'
        ]
