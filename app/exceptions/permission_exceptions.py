class PermissionError(Exception):
    def __init__(
        self, message={"message": "Need to be admin or owner"}, status_code=401
    ):
        self.response = message
        self.status_code = status_code
