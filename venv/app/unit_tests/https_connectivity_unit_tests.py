import unittest
from app.tests.https_connectivity import HTTPSConnectivity
import socket
import os
from app.unit_tests.unit_tests_helpers import UnitTestsHelpers

class TestSuccessfulHTTPSConnectivity(unittest.TestCase):
    def setUp(self):
        self.address = 'www.google.com'
        self.https_test = HTTPSConnectivity(address=self.address, method='GET', params=None)
        self.https_test.run()

    def test_success_run_result(self):
        self.assertTrue(self.https_test.success)

    def test_success_log_write(self):
        last_log = UnitTestsHelpers.last_log()
        self.assertIn("Succeeded with latency of ", last_log)
        self.assertIn("to perform HTTPS connectivity with GET request to " + self.address, last_log)

class TestFailedHTTPSConnectivity(unittest.TestCase):
    def setUp(self):
        self.address = "www. " + UnitTestsHelpers.random_string() + ".com"
        self.https_test = HTTPSConnectivity(address=self.address, method='GET', params=None)
        self.https_test.run()

    def test_failure_run(self):
        self.assertFalse(self.https_test.success)

    def test_faliure_log_write(self):
        last_log = UnitTestsHelpers.last_log()
        self.assertIn("Failed to perform HTTPS connectivity with GET request to " + self.address, last_log)

if __name__ == '__main__':
    unittest.main()