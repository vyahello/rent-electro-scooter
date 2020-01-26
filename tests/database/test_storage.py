import os
from scooter.database.storage import full_path


def test_full_path() -> None:
    assert full_path("file") == os.path.join(os.getcwd(), "scooter/database/file")
