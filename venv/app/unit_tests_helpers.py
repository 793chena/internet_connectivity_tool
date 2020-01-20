import string
import random

class UnitTestsHelpers:
    def random_string(stringLength=10):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))
