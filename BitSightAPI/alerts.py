from bitsightapi import BitSightSession


class Alert(BitSightSession):
    """
    This class handles the Alerts API endpoint
    """

    def __init__(self, path='alerts', **params):
        self.api_endpoint = '/v2/alerts'
        self.api_paths = {
            'alerts': '/',
            'recent alerts': '/latest'
        }
        self.api_params = {
            'alert_date',
            'alert_date_gt',
            'alert_date_gte',
            'alert_date_lt',
            'alert_date_lte',
            'alert_type',
            'company_guid',
            'expand',
            'folder_guid',
            'limit',
            'offset',
            'q',
            'severity',
            'sort'
        }
        self.alert_types = {
            'INFORMATIONAL',
            'NIST_CATEGORY',
            'PERCENT_CHANGE',
            'RATING_THRESHOLD',
            'RISK_CATEGORY',
            'VULNERABILITY'
        }
        self.severity_levels = {
            'INFORMATIONAL',
            'INCREASE',
            'WARN',
            'CRITICAL'
        }