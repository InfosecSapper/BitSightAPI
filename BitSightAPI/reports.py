from bitsightapi import BitSightSession


class Reports(BitSightSession):
    """
    Reports class
    """

    def __init__(self, path, **params):
        self.api_paths = {}
        self.api_params = {}
        pass