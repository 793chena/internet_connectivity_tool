import unittest
from app.tests.dns_connectivity import DNSConnectivity
from app.unit_tests.unit_tests_helpers import UnitTestsHelpers
import os

class TestSuccessfulDnsConnectivity(unittest.TestCase):
    def setUp(self):
        self.address = "www.google.com"
        self.dns_test = DNSConnectivity(address=self.address)
        self.dns_test.run()

    def test_success_run_result(self):
        self.assertTrue(self.dns_test.success)

    def test_success_log_write(self):
        last_log = UnitTestsHelpers.last_log()
        self.assertIn("Succeeded to perform DNS lookup to " + self.address, last_log)

class TestFailedDnsConnectivity(unittest.TestCase):
    def setUp(self):
        self.address = "www." + UnitTestsHelpers.random_string() + ".com"
        self.dns_test = DNSConnectivity(address=self.address)
        self.dns_test.run()

    def test_failure_run(self):
        self.assertFalse(self.dns_test.success)

    def test_faliure_log_write(self):
        last_log = UnitTestsHelpers.last_log()
        self.assertIn("Failed to perform DNS lookup to " + self.address, last_log)

if __name__ == '__main__':
    unittest.main()