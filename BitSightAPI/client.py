import requests

API_URL = 'https://api.bitsighttech.com/ratings'


class Session(object):
    """This is the base class and provides a means to interact with the API."""

    def __init__(self, key: str):
        """
        This is the class constructor.
        
        The class is instantiated with the user's API key as an
        argument of the type string.
        """

        self.api_key = key
        self.api_endpoint = '/v1'
        self.api_variables = {}
        self.api_paths = {
            'root': '/'
        }
        self.api_params = []


    def info(self, path='root', **params):
        """Return API data as JSON object."""
        if path not in self.api_paths:
            raise ValueError("ERROR: path must be one of %r." % self.api_paths)
        for param in params:
            if param not in self.api_params:
                raise ValueError("ERROR: %s is not a valid parameter for this request! Valid parameters are: %r." % (param, self.api_params))
        url = API_URL + self.api_endpoint + self.api_paths[path] % self.api_variables
        info = self._call(url, **params)
        return info


    def test(self):
        """
        This is a helper function to test connectivity to the API.

        It returns the HTTP status code if the status is 'OK', else it
        raises an error with the status code. See the Requests docs
        for more information.
        """

        url = API_URL + self.api_endpoint + self.api_paths['root']
        status = requests.get(url, params=None, auth=(self.api_key, ''))
        if status.status_code != requests.codes.ok:
            status.raise_for_status()
        else:
            return status

    
    def _call(self, url, **params):
        data = requests.get(url, params=params, auth=(self.api_key, '')).json()
        return data
