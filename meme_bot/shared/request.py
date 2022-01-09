class ValidRequestObject:
    def __bool__(self):
        return True

    @classmethod
    def from_dict(cls, params):
        raise NotImplementedError


class InvalidRequestObject:
    def __init__(
        self,
    ):
        self.errors = []

    def add_error(self, parameter, message):
        self.errors.append({"parameter": parameter, "message": message})

    def has_errors(self):
        return len(self.errors) > 0

    def __bool__(self):
        return False
