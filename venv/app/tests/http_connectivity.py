from .http_protocols_requests import HttpProtocolsRequests
import requests

HTTP_PREFIX = 'http://'
HTTP_RESULTS_FILE = 'http_results.txt'

class HTTPConnectivity(HttpProtocolsRequests):
    addresses_latency = {} #initialize addresses latency hashmap

    def run(self):
        try:
            if self.method == 'GET':
                latency = self.get_request_latency(url= HTTP_PREFIX + self.address)
                success = True
                self.set_result_latency(latency)
                self.alert_if_needed(latency)
            else:
                raise Exception("Method "+ self.method +" is currently not supported")
        except requests.exceptions.ConnectionError:
            success = False
        self.log(success)

    def alert_if_needed(self, latency):
        last_latency = self.get_last_result(HTTP_RESULTS_FILE)
        if last_latency is not None:
            threashold = latency - last_latency
            if threashold > self.accepted_latency_threashold:
                self.alert(threashold)
        self.write_result(HTTP_RESULTS_FILE)

    def log_message(self, success):
        result = "Succeeded with latency of [" + str(self.result_latency) +"] " if success else "Failed "
        result += "to perform HTTP connectivity with " + self.method + " request to " + self.address
        if self.params is not None and self.params != "":
            result +=" with params: " + str(self.params)
        return result
