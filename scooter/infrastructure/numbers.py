def make_int(text: str, default: int = -1) -> int:
    """Converts text into integer."""
    try:
        return int(text)
    except (TypeError, ValueError):
        return default
