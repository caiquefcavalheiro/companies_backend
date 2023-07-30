class InvalidPaginateParamsError(Exception):
    def __init__(self, response: dict, status_code: int = 400):
        self.response = response
        self.status_code = status_code
