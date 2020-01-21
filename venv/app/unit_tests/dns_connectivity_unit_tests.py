import unittest
from app.tests.dns_connectivity import DNSConnectivity
from app.unit_tests.unit_tests_helpers import UnitTestsHelpers
import os

# This class tests a successfull DNS test functionality -
# we excpect to successfully perform DNS lookup and we want
# to check that the log file contains the correct log.
class TestSuccessfulDnsConnectivity(unittest.TestCase):
    def setUp(self):
        self.address = "www.google.com"
        self.dns_test = DNSConnectivity(address=self.address)
        self.dns_test.run()

    def test_success_log_write(self):
        last_log = UnitTestsHelpers.last_log()
        self.assertIn("Succeeded to perform DNS lookup to " + self.address, last_log)

# This class tests a DNS test functionality in faliure-
# we excpect to fail performing DNS lookup and we want
# to check that the log file contains the correct log.
class TestFailedDnsConnectivity(unittest.TestCase):
    def setUp(self):
        self.address = "www." + UnitTestsHelpers.random_string() + ".com"
        self.dns_test = DNSConnectivity(address=self.address)
        self.dns_test.run()

    def test_faliure_log_write(self):
        last_log = UnitTestsHelpers.last_log()
        self.assertIn("Failed to perform DNS lookup to " + self.address, last_log)

if __name__ == '__main__':
    unittest.main()