from app.exceptions import InvalidPaginateParamsError


class PaginateListServices:
    def validate_page_atributes(
        self, start: int, limit: int, sort: str, dir: str, accepted_keys: list
    ):
        if start < 0:
            raise InvalidPaginateParamsError(
                {"message": "The start parameter needs to be 0 or greater"}
            )
        elif limit <= 0:
            raise InvalidPaginateParamsError(
                {"message": "The limit parameter needs to be 0 or greater"}
            )
        elif dir not in ["asc", "desc"]:
            raise InvalidPaginateParamsError(
                {"message": "The dir parameter must be 'asc' or 'desc'"}
            )
        elif sort not in accepted_keys:
            raise InvalidPaginateParamsError(
                {
                    "message": f"The sort parameter must be one of the list {accepted_keys}"
                }
            )
