# pylint: disable=redefined-outer-name
from typing import NamedTuple
import pytest
from _pytest.fixtures import SubRequest
from scooter.infrastructure.switch import strict_range


class Range(NamedTuple):
    """Returns range place holder."""

    start: int
    stop: int
    range_: range


@pytest.fixture(
    scope="session",
    params=(
        Range(1, 10, range(1, 11)),
        Range(1, 20, range(1, 21)),
        Range(1, 30, range(1, 31)),
    ),
)
def custom_range(request: SubRequest) -> Range:
    return request.param


def test_strict_range(custom_range: Range) -> None:
    assert (
        strict_range(custom_range.start, custom_range.stop)
        == custom_range.range_
    )


def test_strict_range_length(custom_range: Range) -> None:
    assert (
        len(strict_range(custom_range.start, custom_range.stop))
        == custom_range.stop
    )


def test_strict_range_first(custom_range: Range) -> None:
    assert (
        strict_range(custom_range.start, custom_range.stop)[0]
        == custom_range.start
    )


def test_strict_range_last(custom_range: Range) -> None:
    assert (
        strict_range(custom_range.start, custom_range.stop)[-1]
        == custom_range.stop
    )


def test_wrong_strict_range() -> None:
    with pytest.raises(ValueError):
        strict_range(10, 1)
