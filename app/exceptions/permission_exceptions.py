class PermissionError(Exception):
    def __init__(
        self,
        message: dict = {"message": "Need to be admin or owner"},
        status_code: int = 401,
    ):
        self.response = message
        self.status_code = status_code
