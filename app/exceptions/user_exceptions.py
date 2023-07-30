class EmailFormatError(Exception):
    def __init__(
        self,
        message: dict = {"message": "Provide a valid email"},
        status_code: int = 400,
    ):
        self.message = message
        self.status_code = status_code


class NameFormatError(Exception):
    def __init__(
        self,
        response: dict = {"message": "Provide a valid Name."},
        status_code: int = 400,
    ):
        self.response = response
        self.status_code = status_code
