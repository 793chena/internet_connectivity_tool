from .test import Test
from interface import implements
import requests

HTTP_PREFIX = 'http://'

class HTTPConnectivity(implements(Test)):
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

    def write_to_log_file(self, message):
        f = open("tests_log.txt", "a+")
        f.write(str(datetime.now()) + " -- " + message +"\n")

        f.close()

    def log(self, success):
        message = self.log_message(success)
        self.write_to_log_file(message)
        print(message)
