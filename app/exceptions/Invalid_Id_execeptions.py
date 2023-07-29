class InvalidIdError(Exception):
    def __init__(
        self,
        response={"message": "Invalid ID params"},
        status_code=400,
    ):
        self.response = response
        self.status_code = status_code
