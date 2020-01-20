import socket
from .test import Test
from interface import implements
from datetime import datetime

class DNSConnectivity(implements(Test)):
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

    def write_to_log_file(self, message):
        f = open("tests_log.txt", "a+")
        f.write(str(datetime.now()) + " -- " + message +"\n")

        f.close()

    def log(self, success):
        message = self.log_message(success)
        self.write_to_log_file(message)
        print(message)
