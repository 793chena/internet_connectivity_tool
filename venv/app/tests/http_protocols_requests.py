from .test import Test
import requests
from abc import abstractmethod
import os

# Abstract http protocols class - http and https are supported tests
# which both have some similar attributes and mechanism.
class HttpProtocolsRequests(Test):
    def __init__(self, address, method, params, accepted_latency_threashold):
        self.address = address
        self.method = method
        self.params = params
        self.result_latency = None
        self.accepted_latency_threashold = accepted_latency_threashold

    def set_result_latency(self, result_latency):
        self.result_latency = result_latency

    def get_request_latency(self, url):
        return requests.get(url=url, params=self.params).elapsed.total_seconds()

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def log_message(self, success):
        pass

    def alert(self, threashold):
        print('Latency to get to: ' + self.address + ' took ' + str(threashold) + " seconds more than last run")

    def get_last_result(self, file_name):
        if not os.path.exists(file_name):
            return None

        file = open(file_name, "r")
        lines = file.read().splitlines()
        file.close()
        if len(lines) == 0:
            return None
        line = [lines[i] for i in range(len(lines) - 1, -1, -1) if self.address in lines[i]]
        return float(line[0].split(" ")[1]) if line is not None and len(line) != 0 else None

    def write_result(self, file_name):
        f = open(file_name, "a+")
        f.write(self.address + " " + str(self.result_latency) + "\n")
        f.close()

