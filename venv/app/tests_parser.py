from os import path
import json
from tests.test_factory import TestFactory

CONFIGURATIONS_PATH = 'configurations/configurations.json'
TESTS_KEY = "tests"

class TestsParser:
    def __init__(self):
        configurations_file = self.open_configuratios_file()
        raw_tests = self.load_tests(configurations_file)
        self.tests = self.create_tests(raw_tests)

    def serialized_tests(self):
        return self.tests

    def open_configuratios_file(self):
        base_path = path.dirname(__file__)
        file_path = path.abspath(path.join(base_path, "..", CONFIGURATIONS_PATH))
        file = open(file_path, "r")

        return file

    def load_tests(self, configurations_file):
        tests_configurations_json = configurations_file.read()
        tests_configurations = json.loads(tests_configurations_json)
        tests = tests_configurations[TESTS_KEY]

        return tests

    def create_tests(self, raw_tests):
        tests_objects = []
        for test in raw_tests:
            current_test = self.create_test(test)
            tests_objects.append(current_test)
            print(current_test)

        return tests_objects

    def create_test(self, test):
        return TestFactory.create_test(test["name"], test["properties"])
