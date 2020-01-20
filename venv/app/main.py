from tests_parser import TestsParser

def main():
    parsed_tests = TestsParser()
    for test in parsed_tests.serialized_tests():
        print(test.run())

if __name__ == "__main__":
    main()