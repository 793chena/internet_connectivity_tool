import unittest
from app.tests.http_connectivity import HTTPConnectivity
import socket
import os
from app.unit_tests_helpers import UnitTestsHelpers

class TestSuccessfulHTTPConnectivity(unittest.TestCase):
    def setUp(self):
        self.address = 'www.google.com'
        self.http_test = HTTPConnectivity(address=self.address, method='GET', params=None)
        self.http_test.run(dry_mode=True)

    def test_success_run_result(self):
        self.assertTrue(self.http_test.success)

    def test_success_log_write(self):
        log_file = open("tests_log_dry.txt", "r")
        lines = log_file.read().splitlines()
        last_line = lines[-1]
        self.assertIn("Succeed with latency of ", last_line)
        self.assertIn("to perform HTTP connectivity with GET request to " + self.address, last_line)
        log_file.close()
        os.remove("tests_log_dry.txt")

class TestFailedHTTPConnectivity(unittest.TestCase):
    def setUp(self):
        self.address = "www. " + UnitTestsHelpers.random_string() + ".com"
        self.http_test = HTTPConnectivity(address=self.address, method='GET', params=None)
        self.http_test.run(dry_mode=True)

    def test_failure_run(self):
        self.assertFalse(self.http_test.success)

    def test_faliure_log_write(self):
        log_file = open("tests_log_dry.txt", "r")
        lines = log_file.read().splitlines()
        last_line = lines[-1]
        self.assertIn("Failed to perform HTTP connectivity with GET request to " + self.address, last_line)
        log_file.close()
        os.remove("tests_log_dry.txt")


if __name__ == '__main__':
    unittest.main()