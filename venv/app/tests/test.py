from abc import ABC, abstractmethod
from datetime import datetime

# Gereral test abstract class - we want to force all tests to contain
# run operations log message for the program's output.
class Test(ABC):
    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def log_message(self):
        pass

    def write_to_log_file(self, message):
        f = open("tests_log.txt", "a+")
        f.write(str(datetime.now()) + " -- " + message +"\n")

        f.close()

    def log(self, success):
        message = self.log_message(success)
        self.write_to_log_file(message)
        print(message)
