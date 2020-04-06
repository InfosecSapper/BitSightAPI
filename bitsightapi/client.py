import requests

API_URL = 'https://api.bitsighttech.com/ratings'


class Session(object):
    """
    This is the base class and provides a means to interact with the API.
    """

    def __init__(self, key: str):
        """
        This is the class constructor.
        
        The class is instantiated with the user's API key as an
        argument of the type string.
        """

        self.api_key = key
        self.api_endpoint = '/v1'
        self.api_variables = None
        self.api_paths = {
            'root': '/'
        }
        self.api_params = None


    def info(self, path='root', **params):
        """
        This is the main function for returning data from the API.
        """

        if path not in self.api_paths:
            raise ValueError("ERROR: path must be one of %r." % self.api_paths)
        url = API_URL + self.api_endpoint + self.api_paths[path] % self.api_variables
        info = self._call(url)
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
        data = requests.get(url, auth=(self.api_key, '')).json()
        return data