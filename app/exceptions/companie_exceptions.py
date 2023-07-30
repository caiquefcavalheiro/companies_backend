class CNAEFormatError(Exception):
    def __init__(
        self,
        response={"message": "Provide a valid CNAE, example: '1111-2/33'."},
        status_code=400,
    ):
        self.response = response
        self.status_code = status_code


class CNPJFormatError(Exception):
    def __init__(
        self,
        response: dict = {
            "message": "Provide a valid CNPJ, example: '11.222.333/4444-55' ."
        },
        status_code: int = 400,
    ):
        self.response = response
        self.status_code = status_code


class CNPJNotFound(Exception):
    def __init__(self, cnpj: str):
        self.response = {"message": f"The CNPJ {cnpj} not found"}
        self.status_code = 404
