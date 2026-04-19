def clamp(n: float, lo: float, hi: float) -> float:
    """Return n clamped to the inclusive range [lo, hi]."""
    return max(lo, min(n, hi))


def percent(part: float, whole: float) -> float:
    """Return part/whole * 100, or 0.0 if whole is 0."""
    if whole == 0:
        return 0.0
    return part / whole * 100
