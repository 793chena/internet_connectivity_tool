#from .test import Test
import requests
from .internet_requests import InternetRequests

HTTPS_PREFIX = 'https://'

class HTTPSConnectivity(InternetRequests):
    def run(self, dry_mode = False):
        try:
            if self.method == 'GET':
                latency = self.get_request_latency(url=HTTPS_PREFIX + self.address)
                self.set_success(True)
                self.set_result_latency(latency)
            else:
                raise Exception("Method "+ self.method +" is currently not supported")
        except requests.exceptions.ConnectionError:
            self.set_success(False)
        self.log(dry_mode)

    def log_message(self):
        result = "Succeed with latency of [" + str(self.result_latency) +"] " if self.success else "Failed "
        result += "to perform HTTPS connectivity with " + self.method + " request to " + self.address
        if self.params is not None and self.params != "":
            result +=" with params: " + self.params
        return result

