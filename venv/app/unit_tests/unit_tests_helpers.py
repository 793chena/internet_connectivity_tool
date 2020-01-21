import string
import random
import os
from app.tests_parser import TestsParser

class UnitTestsHelpers:
    def random_string(stringLength=10):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))

    def last_log():
        log_file = open("tests_log.txt", "r")
        lines = log_file.read().splitlines()
        log_file.close()
        os.remove("tests_log.txt")
        return lines[-1]

    def prepare_tests(configurations):
        configuratins_file = open("../../configurations/configurations.json", "w")
        configuratins_file.write(configurations)
        configuratins_file.close()
        test_parser = TestsParser()
        tests = test_parser.serialized_tests()

        return tests