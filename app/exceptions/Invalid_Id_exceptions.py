class InvalidIdError(Exception):
    def __init__(
        self,
        response: dict = {"message": "Invalid ID params"},
        status_code: int = 400,
    ):
        self.response = response
        self.status_code = status_code
