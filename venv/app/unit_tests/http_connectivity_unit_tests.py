import unittest
from app.tests.http_connectivity import HTTPConnectivity
import socket
import os
from app.unit_tests.unit_tests_helpers import UnitTestsHelpers

class TestSuccessfulHTTPConnectivity(unittest.TestCase):
    def setUp(self):
        self.address = 'www.google.com'
        self.http_test = HTTPConnectivity(address=self.address, method='GET', params=None)
        self.http_test.run()

    def test_success_run_result(self):
        self.assertTrue(self.http_test.success)

    def test_success_log_write(self):
        last_log = UnitTestsHelpers.last_log()
        self.assertIn("Succeeded with latency of ", last_log)
        self.assertIn("to perform HTTP connectivity with GET request to " + self.address, last_log)

class TestFailedHTTPConnectivity(unittest.TestCase):
    def setUp(self):
        self.address = "www. " + UnitTestsHelpers.random_string() + ".com"
        self.http_test = HTTPConnectivity(address=self.address, method='GET', params=None)
        self.http_test.run()

    def test_failure_run(self):
        self.assertFalse(self.http_test.success)

    def test_faliure_log_write(self):
        last_log = UnitTestsHelpers.last_log()
        self.assertIn("Failed to perform HTTP connectivity with GET request to " + self.address, last_log)

if __name__ == '__main__':
    unittest.main()