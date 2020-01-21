from .test import Test
import requests
from abc import abstractmethod

#todo naming
class InternetRequests(Test):
    def __init__(self, address, method, params):
        self.address = address
        self.method = method
        self.params = params
        self.result_latency = None

    def set_result_latency(self, result_latency):
        self.result_latency = result_latency

    def get_request_latency(self, url):
        return requests.get(url=url, params=self.params).elapsed.total_seconds()

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def log_message(self):
        pass
