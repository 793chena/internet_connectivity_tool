import unittest
from app.unit_tests_helpers import UnitTestsHelpers
import json
from tests_parser import TestsParser
from tests.dns_connectivity import DNSConnectivity
from tests.http_connectivity import HTTPConnectivity
from tests.https_connectivity import HTTPSConnectivity

class TestSuccessfulHTTPSConnectivity(unittest.TestCase):
    def setUp(self):
        pass

    def test_dns_test(self):
        address = UnitTestsHelpers.random_string()
        configuratins_file = open("../configurations/configurations.json", "w")
        configurations = '{ "tests": [ {"name": "DNS_CONNECTIVITY", "properties": { "address": "' + address + '"}} ] }'
        configuratins_file.write(configurations)
        configuratins_file.close()
        test_parser = TestsParser()
        tests = test_parser.serialized_tests()
        self.assertEqual(len(tests), 1)
        self.assertEqual(tests[0].address, address)
        self.assertIsInstance(tests[0], DNSConnectivity)

    def test_http_test(self):
        address = UnitTestsHelpers.random_string()
        configuratins_file = open("../configurations/configurations.json", "w")
        configurations = '{ "tests": [ {"name": "HTTP_CONNECTIVITY", "properties": { "address": "' + address + '", "method": "GET", "params" : null}} ] }'
        configuratins_file.write(configurations)
        configuratins_file.close()
        test_parser = TestsParser()
        tests = test_parser.serialized_tests()
        self.assertEqual(len(tests), 1)
        self.assertEqual(tests[0].address, address)
        self.assertIsInstance(tests[0], HTTPConnectivity)

    def test_https_test(self):
        address = UnitTestsHelpers.random_string()
        configuratins_file = open("../configurations/configurations.json", "w")
        configurations = '{ "tests": [ {"name": "HTTPS_CONNECTIVITY", "properties": { "address": "' + address + '", "method": "GET", "params" : null}} ] }'
        configuratins_file.write(configurations)
        configuratins_file.close()
        test_parser = TestsParser()
        tests = test_parser.serialized_tests()
        self.assertEqual(len(tests), 1)
        self.assertEqual(tests[0].address, address)
        self.assertIsInstance(tests[0], HTTPSConnectivity)

    def test_https_test(self):
        address = UnitTestsHelpers.random_string()
        configuratins_file = open("../configurations/configurations.json", "w")
        configurations = '{ "tests": [ {"name": "HTTPS_CONNECTIVITY", "properties": { "address": "' + address + '", "method": "GET", "params" : null}} ] }'
        configuratins_file.write(configurations)
        configuratins_file.close()
        test_parser = TestsParser()
        tests = test_parser.serialized_tests()
        self.assertEqual(len(tests), 1)
        self.assertEqual(tests[0].address, address)
        self.assertIsInstance(tests[0], HTTPSConnectivity)

    def test_multiple_tests(self):
        address = UnitTestsHelpers.random_string()
        configuratins_file = open("../configurations/configurations.json", "w")
        configurations = '{ "tests": [ {"name": "HTTPS_CONNECTIVITY", "properties": { "address": "' + address + '", "method": "GET", "params" : null}},' \
                                      '{"name": "HTTP_CONNECTIVITY", "properties": { "address": "' + address + '", "method": "GET", "params" : null}},' \
                                      '{"name": "DNS_CONNECTIVITY", "properties": { "address": "' + address + '"}},' \
                                      '{"name": "DNS_CONNECTIVITY", "properties": { "address": "' + address + '"}} ] }'
        configuratins_file.write(configurations)
        configuratins_file.close()
        test_parser = TestsParser()
        tests = test_parser.serialized_tests()
        self.assertEqual(len(tests), 4)

if __name__ == '__main__':
    unittest.main()



