import socket
from .test import Test

class DNSConnectivity(Test):
    def __init__(self, address):
        self.address = address

    def run(self):
        try:
            socket.gethostbyname(self.address)
            success = True
        except socket.gaierror:
            success = False
        self.log(success)

    def log_message(self, success):
        result = "Succeeded " if success else "Failed "
        result += "to perform DNS lookup to " + self.address

        return result
