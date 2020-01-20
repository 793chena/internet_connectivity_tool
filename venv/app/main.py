from tests_parser import TestsParser

def main():
    tests_parser = TestsParser()
    tests = tests_parser.serialized_tests()
    for test in tests:
        test.run()

if __name__ == "__main__":
    main()