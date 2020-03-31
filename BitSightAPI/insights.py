from bitsightapi import BitSightSession


class Insights(BitSightSession):
    """
    Insights class
    """

    def __init__(self, path, **params):
        self.api_paths = {}
        self.api_params = {}
        pass