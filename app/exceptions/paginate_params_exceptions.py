class InvalidPaginateParamsError(Exception):
    def __init__(self, response, status_code=400):
        self.response = response
        self.status_code = status_code
