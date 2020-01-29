from typing import Any
import pytest
from scooter.infrastructure.numbers import make_int


@pytest.mark.parametrize("enter, result", (("10", 10), ("-10", -10), (None, -1), ("", -1), ({}, -1)))
def test_make_int(enter: Any, result: int) -> None:
    assert make_int(enter) == result
