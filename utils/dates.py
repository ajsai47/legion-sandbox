from datetime import date, datetime


def format_iso(dt: datetime) -> str:
    """Return an ISO 8601 string representation of the given datetime."""
    return dt.isoformat()


def days_between(a: date, b: date) -> int:
    """Return the absolute number of days between two dates."""
    return abs((b - a).days)
