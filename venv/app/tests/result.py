class Result: #might be just not good
    def __init__(self, is_success, test_type, attribute, extra = None):
        self.is_success = is_success
        self.test_type = test_type
        self.attribute = attribute
        self.extra = extra

    def __str__(self):
        log = ""
        if self.is_success:
            log = log + "Successfully performed"
        else:
            log = log + "Failed to perform"
        log = log + self.test_type + "to" + attribute
        if self.extra is not None:
            log = log + extra
