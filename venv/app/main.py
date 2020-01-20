from tests_parser import TestsParser

def main():
    tests_parser = TestsParser()
    tests = tests_parser.serialized_tests()
    for test in tests:
        try:
            test.run()
        except Exception as e:
            print("Failed to run test: " + type(test).__name__ + " with the following error: " + str(e))
            #print(e)


if __name__ == "__main__":
    main()