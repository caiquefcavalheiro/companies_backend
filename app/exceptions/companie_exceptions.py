class CNAEFormatError(Exception):
    def __init__(
        self,
        response={"error": "Provide a valid CNAE, example: '1111233'."},
        status_code=400,
    ):
        self.response = response
        self.status_code = status_code


class CNPJFormatError(Exception):
    def __init__(
        self,
        response={"error": "Provide a valid CNPJ, example: '11222333444455' ."},
        status_code=400,
    ):
        self.response = response
        self.status_code = status_code
