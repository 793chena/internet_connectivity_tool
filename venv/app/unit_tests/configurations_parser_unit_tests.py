import unittest
from app.unit_tests.unit_tests_helpers import UnitTestsHelpers
from app.tests.dns_connectivity import DNSConnectivity
from app.tests.http_connectivity import HTTPConnectivity
from app.tests.https_connectivity import HTTPSConnectivity

# This class tests the functionality of the tests parser -
# we want to make sure that according to a specific jaon
# configurations we get the correct test objects.
class TestConfigurationsParser(unittest.TestCase):
    def setUp(self):
        self.address = 'www.' + UnitTestsHelpers.random_string() + '.com'

    def test_dns_test(self):
        configurations = '{ "tests": [ {"name": "DNS_CONNECTIVITY", "properties": { "address": "' + self.address + '"}} ] }'
        tests = UnitTestsHelpers.prepare_tests(configurations)
        self.assertEqual(len(tests), 1)
        self.assertEqual(tests[0].address, self.address)
        self.assertIsInstance(tests[0], DNSConnectivity)

    def test_http_test(self):
        configurations = '{ "tests": [ {"name": "HTTP_CONNECTIVITY", "properties": { "address": "' + self.address + '", "method": "GET", "params" : null, "accepted_latency_threashold": 10}} ] }'
        tests = UnitTestsHelpers.prepare_tests(configurations)
        self.assertEqual(len(tests), 1)
        self.assertEqual(tests[0].address, self.address)
        self.assertIsInstance(tests[0], HTTPConnectivity)

    def test_https_test(self):
        configurations = '{ "tests": [ {"name": "HTTPS_CONNECTIVITY", "properties": { "address": "' + self.address + '", "method": "GET", "params" : null, "accepted_latency_threashold": 10}} ] }'
        tests = UnitTestsHelpers.prepare_tests(configurations)
        self.assertEqual(len(tests), 1)
        self.assertEqual(tests[0].address, self.address)
        self.assertIsInstance(tests[0], HTTPSConnectivity)

    def test_multiple_tests(self):
        configurations = '{ "tests": [ {"name": "HTTPS_CONNECTIVITY", "properties": { "address": "' + self.address + '", "method": "GET", "params" : null, "accepted_latency_threashold": 10}},' \
                                      '{"name": "HTTP_CONNECTIVITY", "properties": { "address": "' + self.address + '", "method": "GET", "params" : null, "accepted_latency_threashold": 10}},' \
                                      '{"name": "DNS_CONNECTIVITY", "properties": { "address": "' + self.address + '"}},' \
                                      '{"name": "DNS_CONNECTIVITY", "properties": { "address": "' + self.address + '"}} ] }'
        tests = UnitTestsHelpers.prepare_tests(configurations)
        self.assertEqual(len(tests), 4)

if __name__ == '__main__':
    unittest.main()



