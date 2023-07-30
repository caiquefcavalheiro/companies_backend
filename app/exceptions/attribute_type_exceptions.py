class AttributeTypeError(Exception):
    name_types = {
        str: "string",
        int: "integer",
        float: "decimal",
        bool: "boolean",
        list: "list",
    }

    def __init__(self, value: str, type: str, status_code: int = 400):
        self.response = {"message": f"Value {value} is not of the type {type}"}
        self.status_code = status_code
