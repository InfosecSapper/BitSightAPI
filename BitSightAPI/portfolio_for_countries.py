from bitsightapi.client import Session


class PortfolioForCountries(Session):
    """
    Portfolio for Countries class
    """

    def __init__(self, session):
        self.api_key = session.api_key
        self.api_endpoint = None
        self.api_variables = None
        self.api_paths = {}
        self.api_params = {}
        pass