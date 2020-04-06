from bitsightapi.client import Session


class Folders(Session):
    """
    Folders class
    """

    def __init__(self, session):
        self.api_key = session.api_key
        self.api_endpoint = '/v1/folders'
        self.api_paths = {
            'root': '/',
            'products': '/%(folderguid)s/products',
            'product types': '/%(folderguid)s/product-types',
            'providers': '/%(folderguid)s/providers',
            'provider products': '/%(folderguid)s/providers/%(providerguid)s/products'
        }
        self.api_params = {}
        pass