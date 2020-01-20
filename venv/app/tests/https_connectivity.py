from .test import Test
import requests

HTTPS_PREFIX = 'https://'

class HTTPSConnectivity(Test):
    def __init__(self, ip_address, method, attributes):
        self.ip_address = ip_address
        self.method = method
        self.attributes = attributes
        self.success = None
        self.result_latency = None

    def set_success(self, success):
        self.success = success

    def set_result_latency(self, result_latency):
        self.result_latency = result_latency

    def run(self):
        try:
            latency = requests.get(url = HTTPS_PREFIX + self.ip_address, params = self.attributes).elapsed.total_seconds()
            self.set_success(True)
            self.set_result_latency(latency)
        except requests.exceptions.ConnectionError:
            self.set_success(False)
        self.log()

    def log_message(self):
        result = "Succeed with latency of [" + str(self.result_latency) +"] " if self.success else "Failed "
        result += "to perform HTTPS connectivity with " + self.method + " request to " + self.ip_address
        if self.attributes is not None and self.attributes != "":
            result +=" with params: " + self.attributes
        return result

