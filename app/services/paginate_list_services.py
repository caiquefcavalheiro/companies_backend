from app.exceptions import InvalidPaginateParams


class PaginateListServices:
    def validate_page_atributes(
        self, start: int, limit: int, sort: str, dir: str, accepted_keys: list
    ):
        if start < 0:
            raise InvalidPaginateParams(
                {"message": "The start parameter needs to be 0 or greater"}
            )
        elif limit <= 0:
            raise InvalidPaginateParams(
                {"message": "The limit parameter needs to be 0 or greater"}
            )
        elif dir not in ["asc", "desc"]:
            raise InvalidPaginateParams(
                {"message": "The dir parameter must be 'asc' or 'desc'"}
            )
        elif sort not in accepted_keys:
            raise InvalidPaginateParams(
                {
                    "message": f"The sort parameter must be one of the list {accepted_keys}"
                }
            )
