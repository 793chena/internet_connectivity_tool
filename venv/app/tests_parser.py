from os import path
import json
from app.tests.test_factory import TestFactory

CONFIGURATIONS_PATH = 'configurations/configurations.json'
TESTS_KEY = "tests"
NAME_KEY = "name"
PROPERTIES_KEY = "properties"

class TestsParser:
    def __init__(self):
        raw_tests = self.extract_tests_from_configurations()
        self.tests = self.create_tests(raw_tests)

    def get_serialized_tests(self):
        return self.tests

    def extract_tests_from_configurations(self):
        file_path = self.get_configuration_file_path()
        configurations_file = open(file_path, "r")
        tests = self.read_configurations(configurations_file)
        configurations_file.close()

        return tests

    def get_configuration_file_path(self):
        base_path = path.dirname(__file__)
        return path.abspath(path.join(base_path, "..", CONFIGURATIONS_PATH))

    def read_configurations(self, configurations_file):
        tests_configurations_json = configurations_file.read()
        tests_configurations = json.loads(tests_configurations_json)
        tests = tests_configurations[TESTS_KEY]

        return tests

    def create_tests(self, raw_tests):
        tests_objects = []
        for raw_test in raw_tests:
            current_test = self.create_single_test(raw_test)
            tests_objects.append(current_test)

        return tests_objects

    def create_single_test(self, test):
        return TestFactory.create_test(test[NAME_KEY], test[PROPERTIES_KEY])
