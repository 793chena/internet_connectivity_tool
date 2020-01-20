import socket
from .test import Test

class DNSConnectivity(Test):
    def __init__(self, address):
        self.address = address

    def run(self):
        try:
            result = socket.gethostbyname(self.address)
            success = True
        except socket.gaierror:
            success = False
        print(self.log(success)) # Todo write to log file

    def log_message(self, success):
        result = "Succeed " if success else "Failed "
        result += "to perform DNS lookup to " + self.address

        return result
