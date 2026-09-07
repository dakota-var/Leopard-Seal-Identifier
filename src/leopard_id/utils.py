from datetime import date, datetime
from datetime import time

DATE_FORMAT = "%d/%m/%Y"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

def parse_datetime(value: datetime | str) -> datetime:
    """Parse a datetime or string into a datetime."""
    if isinstance(value, datetime):
        return value

    if isinstance(value, str):
        return datetime.strptime(value, DATETIME_FORMAT)

    raise ValueError("Invalid datetime value. Expected datetime or string in YYYY-MM-DD HH:MM:SS format.")

def parse_time(value: time | datetime | str) -> time:
    """Parse a datetime or string into a datetime."""
    if isinstance(value, time):
        return value

    if isinstance(value, datetime):
        return value.time()

    if isinstance(value, str):
        return datetime.strptime(value, DATETIME_FORMAT).time()

    raise ValueError("Invalid time value. Expected time, datetime or string in YYYY-MM-DD HH:MM:SS format.")


def parse_date(value: date | datetime | str) -> date:
    """Parse a date, datetime, or DD/MM/YYYY date string into a date."""
    if isinstance(value, datetime):
        return value.date()

    if isinstance(value, date):
        return value

    if isinstance(value, str):
        return datetime.strptime(value, DATE_FORMAT).date()

    raise ValueError("Invalid date value. Expected date, datetime, or string in DD/MM/YYYY format.")
