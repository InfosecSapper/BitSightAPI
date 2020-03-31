#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""
This module is a Python wrapper for the BitSight API.

Only GET requests are supported in the initial release, but post requests
will be added in a future release.
"""

__version__ = "1.0"
__author__ = "InfosecSapper"

# -----------------------------------------------------------------------------

from os.path import dirname, basename, isfile, join
import glob
import requests
import json



class BitSightSession(object):
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
        self.API_URL = 'https://api.bitsighttech.com/ratings'
        self.api_dict = {
            'overview': {
            'root': '/v1',
            'actions': {
                'default': '/'
                }
            }
        }

    def test_connection(self):
        """
        This is a helper function to test connectivity to the API.

        It returns the HTTP status code if the status is 'OK', else it
        raises an error with the status code. See the Requests docs
        for more information.
        """

        status = requests.get(self.API_URL + '/v1', params=None, auth=(self.api_key, ''))
        if status.status_code != requests.codes.ok:
            status.raise_for_status()
        else:
            return status

    def get_data(self, endpoint='overview', action='default', alertguid='', companyguid='', domain='', folderguid='', industry='', providerguid='', requestguid='', risktypes='', tierguid='', userguid=''):
        """
        The get_data() method makes the call to the BitSight API.

        It receives query elements as arguments and returns a JSON
        object of the query response.
        """

        if endpoint not in self.api_dict:
            raise ValueError(
                "ERROR: endpoint must be one of %r." % self.api_dict
            )
        variables = {
            'alertguid': alertguid,
            'companyguid': companyguid,
            'domain': domain,
            'folderguid': folderguid,
            'industry': industry,
            'providerguid': providerguid,
            'risktypes': risktypes,
            'tierguid': tierguid,
            'userguid': userguid
        }
        url = self.API_URL + self.api_dict[endpoint]['root'] + self.api_dict[endpoint]['actions'][action] % variables
        return requests.get(url, auth=(self.api_key, '')).json()
