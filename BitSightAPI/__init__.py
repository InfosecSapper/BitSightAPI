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

from bitsightapi import alerts
from bitsightapi import companies
from bitsightapi import company_relationships
from bitsightapi import company_requests
from bitsightapi import customers
from bitsightapi import findings
from bitsightapi import folders
from bitsightapi import industries
from bitsightapi import insights
from bitsightapi import news
from bitsightapi import portfolio
from bitsightapi import products
from bitsightapi import rapid_underwriting_assessments
from bitsightapi import reports
from bitsightapi import subscriptions
from bitsightapi import users
