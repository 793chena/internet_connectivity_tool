from .test import Test
import requests

HTTP_PREFIX = 'http://'

class HTTPConnectivity(Test):
    def __init__(self, ip_address, method, attributes):
        self.ip_address = ip_address
        self.method = method
        self.attributes = attributes

    def run(self):
        result = requests.get(url = HTTP_PREFIX + self.ip_address, params = self.attributes)
        if result == None:
            return 'Oh no'
        return result

    def log_message(self, success):
        result = "Succeed " if success else "Failed "
        result += "to perform HTTP connectivity with " + self.method + " to" + self.ip_address + \
                  " with params: " + self.attributes

        return result
