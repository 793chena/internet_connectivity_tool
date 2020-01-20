import unittest
from app.tests.dns_connectivity import DNSConnectivity
from app.unit_tests_helpers import UnitTestsHelpers
import os

class TestSuccessfulDnsConnectivity(unittest.TestCase):
    def setUp(self):
        self.address = "www.google.com"
        self.dns_test = DNSConnectivity(address=self.address)
        self.dns_test.run(dry_mode=True)

    def test_success_run_result(self):
        self.assertTrue(self.dns_test.success)

    def test_success_log_write(self):
        log_file = open("tests_log_dry.txt", "r")
        lines = log_file.read().splitlines()
        last_line = lines[-1]
        self.assertIn("Succeed to perform DNS lookup to " + self.address, last_line)
        log_file.close()
        os.remove("tests_log_dry.txt")

class TestFailedDnsConnectivity(unittest.TestCase):
    def setUp(self):
        self.address = "www." + UnitTestsHelpers.random_string() + ".com"
        self.dns_test = DNSConnectivity(address=self.address)
        self.dns_test.run(dry_mode=True)

    def test_failure_run(self):
        self.assertFalse(self.dns_test.success)

    def test_faliure_log_write(self):
        log_file = open("tests_log_dry.txt", "r")
        lines = log_file.read().splitlines()
        last_line = lines[-1]
        self.assertIn("Failed to perform DNS lookup to " + self.address, last_line)
        log_file.close()
        os.remove("tests_log_dry.txt")

if __name__ == '__main__':
    unittest.main()