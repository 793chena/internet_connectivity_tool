from .test import Test
from interface import implements
import requests

HTTPS_PREFIX = 'https://'

class HTTPSConnectivity(implements(Test)):
    def __init__(self, ip_address, method, attributes):
        self.ip_address = ip_address
        self.method = method
        self.attributes = attributes

    def run(self):
        try:
            result = requests.get(url = HTTPS_PREFIX + self.ip_address, params = self.attributes)
        except requests.exceptions.ConnectionError:
            return 'No No'
        return result

    def log(self, success):
        pass