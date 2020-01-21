from .http_protocols_requests import HttpProtocolsRequests
import requests

HTTP_PREFIX = 'http://'

class HTTPConnectivity(HttpProtocolsRequests):
    def run(self):
        try:
            if self.method == 'GET':
                latency = self.get_request_latency(url= HTTP_PREFIX + self.address)
                success = True
                self.set_result_latency(latency)
            else:
                raise Exception("Method "+ self.method +" is currently not supported")
        except requests.exceptions.ConnectionError:
            success = False
        self.log(success)

    def log_message(self, success):
        result = "Succeeded with latency of [" + str(self.result_latency) +"] " if success else "Failed "
        result += "to perform HTTP connectivity with " + self.method + " request to " + self.address
        if self.params is not None and self.params != "":
            result +=" with params: " + str(self.params)

        return result
