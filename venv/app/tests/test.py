from abc import ABC, abstractmethod
from datetime import datetime

class Test(ABC):

    @abstractmethod
    def run(self, dry_mode = False):
        pass

    @abstractmethod
    def set_success(self):
        pass

    @abstractmethod
    def log_message(self):
        pass

    def write_to_log_file(self, message, dry_mode=False):
        f = open("tests_log.txt", "a+") if not dry_mode else open("tests_log_dry.txt", "a+")
        f.write(str(datetime.now()) + " -- " + message +"\n")

        f.close()

    def log(self, dry_mode=False):
        message = self.log_message()
        self.write_to_log_file(message, dry_mode)

        if not dry_mode:
            print(message)
