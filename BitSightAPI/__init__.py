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

from BitSightAPI import alerts
from BitSightAPI import companies
from BitSightAPI import company_relationships
from BitSightAPI import company_requests
from BitSightAPI import customers
from BitSightAPI import findings
from BitSightAPI import folders
from BitSightAPI import industries
from BitSightAPI import insights
from BitSightAPI import news
from BitSightAPI import portfolio
from BitSightAPI import products
from BitSightAPI import rapid_underwriting_assessments
from BitSightAPI import reports
from BitSightAPI import subscriptions
from BitSightAPI import users
