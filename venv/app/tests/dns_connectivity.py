import socket
from .test import Test

class DNSConnectivity(Test):
    def __init__(self, address):
        self.address = address
        self.success = None

    def set_success(self, success):
        self.success = success

    def run(self):
        try:
            result = socket.gethostbyname(self.address)
            self.set_success(True)
        except socket.gaierror:
            self.set_success(False)
        self.log()

    def log_message(self):
        result = "Succeed " if self.success else "Failed "
        result += "to perform DNS lookup to " + self.address

        return result
