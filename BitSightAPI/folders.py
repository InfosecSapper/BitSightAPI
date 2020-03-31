from bitsightapi import BitSightSession


class Folders(BitSightSession):
    """
    Folders class
    """

    def __init__(self, path, **params):
        self.api_endpoint = '/v1/folders'
        self.api_paths = {
            'folders': '/',
            'products': '/%(folderguid)s/products',
            'product types': '/%(folderguid)s/product-types',
            'providers': '/%(folderguid)s/providers',
            'provider products': '/%(folderguid)s/providers/%(providerguid)s/products'
        }
        self.api_params = {}
        pass