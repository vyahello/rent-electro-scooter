import os


def full_path(filename: str) -> str:
    """Returns full path for a database."""
    return os.path.join(os.path.dirname(__file__), filename)
