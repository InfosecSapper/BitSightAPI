from BitSightAPI.client import Session


class Folders(Session):
    """
    Folders class
    """

    def __init__(self, session, folder_guid='', provider_guid=''):
        self.api_key = session.api_key
        self.api_endpoint = '/v1/folders'
        self.api_variables = {
            'folderguid': folder_guid,
            'providerguid': provider_guid
        }
        self.api_paths = {
            'root': '/',
            'folder': '/%(folder_guid)s',
            'companies': '/%(folder_guid)s/companies',
            'products': '/%(folder_guid)s/products',
            'product types': '/%(folder_guid)s/product-types',
            'providers': '/%(folder_guid)s/providers',
            'dependent companies': '/%(folder_guid)s/providers/%(provider_guid)s/companies',
            'provider products': '/%(folder_guid)s/providers/%(provider_guid)s/products'
        }
        self.api_params = []
