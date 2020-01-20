import unittest
from app.tests.https_connectivity import HTTPSConnectivity
import socket
import os
from app.unit_tests_helpers import UnitTestsHelpers

class TestSuccessfulHTTPSConnectivity(unittest.TestCase):
    def setUp(self):
        self.address = 'www.google.com'
        self.https_test = HTTPSConnectivity(address=self.address, method='GET', params=None)
        self.https_test.run(dry_mode=True)

    def test_success_run_result(self):
        self.assertTrue(self.https_test.success)

    def test_success_log_write(self):
        log_file = open("tests_log_dry.txt", "r")
        lines = log_file.read().splitlines()
        last_line = lines[-1]
        self.assertIn("Succeed with latency of ", last_line)
        self.assertIn("to perform HTTPS connectivity with GET request to " + self.address, last_line)
        log_file.close()
        os.remove("tests_log_dry.txt")

class TestFailedHTTPSConnectivity(unittest.TestCase):
    def setUp(self):
        self.address = "www. " + UnitTestsHelpers.random_string() + ".com"
        self.https_test = HTTPSConnectivity(address=self.address, method='GET', params=None)
        self.https_test.run(dry_mode=True)

    def test_failure_run(self):
        self.assertFalse(self.https_test.success)

    def test_faliure_log_write(self):
        log_file = open("tests_log_dry.txt", "r")
        lines = log_file.read().splitlines()
        last_line = lines[-1]
        self.assertIn("Failed to perform HTTPS connectivity with GET request to " + self.address, last_line)
        log_file.close()
        os.remove("tests_log_dry.txt")


if __name__ == '__main__':
    unittest.main()