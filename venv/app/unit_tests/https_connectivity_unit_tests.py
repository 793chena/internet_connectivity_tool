import unittest
from app.tests.https_connectivity import HTTPSConnectivity
import socket
import os
from app.unit_tests.unit_tests_helpers import UnitTestsHelpers

# This class tests a successfull HTTPS get request test functionality -
# we excpect to successfully perform HTTPS request and we want
# to check that the log file contains the correct log.
class TestSuccessfulHTTPSConnectivity(unittest.TestCase):
    def setUp(self):
        self.address = 'www.google.com'
        self.https_test = HTTPSConnectivity(address=self.address, method='GET', params=None, accepted_latency_threashold=10)
        self.https_test.run()

    def test_success_log_write(self):
        last_log = UnitTestsHelpers.last_log()
        self.assertIn("Succeeded with latency of ", last_log)
        self.assertIn("to perform HTTPS connectivity with GET request to " + self.address, last_log)

# This class tests a HTTPS test functionality in faliure-
# we excpect to fail performing HTTPS get request and we want
# to check that the log file contains the correct log.
class TestFailedHTTPSConnectivity(unittest.TestCase):
    def setUp(self):
        self.address = "www. " + UnitTestsHelpers.random_string() + ".com"
        self.https_test = HTTPSConnectivity(address=self.address, method='GET', params=None, accepted_latency_threashold=10)
        self.https_test.run()

    def test_faliure_log_write(self):
        last_log = UnitTestsHelpers.last_log()
        self.assertIn("Failed to perform HTTPS connectivity with GET request to " + self.address, last_log)

if __name__ == '__main__':
    unittest.main()