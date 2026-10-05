from datetime import date, datetime


class CommonValidation:
    @staticmethod
    def int(value, nullable=True, negative_allowed=False) -> int | None:
        if str(value).strip() == "":
            value = None

        if value is None:
            if nullable:
                return None
            raise ValueError("Value cannot be null")

        if negative_allowed:
            return int(value)
        elif int(value) < 0:
            raise ValueError(
                f"Value must be a positive integer: {value}"
            )
        else:
            return int(value)

    @staticmethod
    def str(value, nullable=True):
        if str(value).strip() == "":
            value = None

        if value is None:
            if nullable:
                return None
            raise ValueError("Value cannot be null")

        return str(value)


def validate_int(value, nullable=True, negative_allowed=False) -> int | None:
    if value is None:
        if nullable:
            return None
        raise ValueError("Value cannot be null")

    if negative_allowed:
        return int(value)
    elif value < 0:
        raise ValueError(
            f"Value must be a positive integer: {value}"
        )
    else:
        return int(value)


def validate_latitude(value: float | None) -> list[str]:
    issues = []

    if value is not None and not -90 <= value <= 90:
        issues.append(
            f"Latitude must be between -90 and 90: {value}"
        )

    return issues


def validate_longitude(value: float | None) -> list[str]:
    issues = []

    if value is not None and not -180 <= value <= 180:
        issues.append(
            f"Longitude must be between -180 and 180: {value}"
        )

    return issues


def validate_date(value: date | None) -> list[str]:
    issues = []

    if value is not None and value > date.today():
        issues.append(
            f"Date cannot be in the future: {value}"
        )

    return issues


def validate_datetime(value: datetime | None) -> list[str]:
    issues = []

    if value is not None and value.tzinfo is None:
        issues.append(
            f"Datetime must include timezone information: {value}"
        )

    return issues
