from BitSightAPI.client import Session

class Alerts(Session):
    """
    This class handles the Alerts API endpoint
    """
    def __init__(self, session):
        self.api_key = session.api_key
        self.api_endpoint = '/v2/alerts'
        self.api_variables = {}
        self.api_paths = {
            'root': '/',
            'recent alerts': '/latest'
        }
        self.api_params = [
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
        ]
        self.alert_types = [
            'INFORMATIONAL',
            'NIST_CATEGORY',
            'PERCENT_CHANGE',
            'RATING_THRESHOLD',
            'RISK_CATEGORY',
            'VULNERABILITY'
        ]
        self.severity_levels = [
            'INFORMATIONAL',
            'INCREASE',
            'WARN',
            'CRITICAL'
        ]