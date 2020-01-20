#from .test import Test
from .internet_requests import InternetRequests
import requests

HTTP_PREFIX = 'http://'

class HTTPConnectivity(InternetRequests):
    def run(self):
        try:
            if self.method == 'GET':
                latency = self.get_request_latency(url= HTTP_PREFIX + self.ip_address)
                self.set_success(True)
                self.set_result_latency(latency)
            else:
                raise Exception('Method is currently not supported')
        except requests.exceptions.ConnectionError:
            self.set_success(False)
        self.log()

    def log_message(self):
        result = "Succeed with latency of [" + str(self.result_latency) +"] " if self.success else "Failed "
        result += "to perform HTTP connectivity with " + self.method + " request to " + self.ip_address
        if self.attributes is not None and self.attributes != "":
            result +=" with params: " + self.attributes

        return result
