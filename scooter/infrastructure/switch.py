# pylint: disable=inconsistent-return-statements
import uuid
from typing import Callable, Any, Set, List, ContextManager


class Switch(ContextManager["Switch"]):
    """The class represents switch-case syntax in python.

    Copyright Michael Kennedy (https://twitter.com/mkennedy)
    """

    __no_result: uuid.UUID = uuid.uuid4()
    __default: uuid.UUID = uuid.uuid4()

    def __init__(self, value: Any) -> None:
        self.value: Any = value
        self.cases: Set[Any] = set()
        self._found: bool = False
        self.__result: uuid.UUID = Switch.__no_result
        self._falling_through: bool = False
        self._func_stack: List[Any] = []

    def default(self, func: Callable[[], Any]) -> None:
        self.case(Switch.__default, func)

    def case(self, key, func: Callable[[], Any], fallthrough: bool = False):  # noqa: C901
        if fallthrough is not None:
            if self._falling_through:
                self._func_stack.append(func)
                if not fallthrough:
                    self._falling_through = False

        if isinstance(key, (list, range)):
            found: bool = False
            for next_key in key:
                if self.case(next_key, func, fallthrough=None):
                    found = True
                    if fallthrough is not None:
                        self._falling_through = fallthrough
            return found

        if key in self.cases:
            raise ValueError(f"Duplicate case: {key}")
        if not func:
            raise ValueError("Action for case cannot be None")
        if not callable(func):
            raise ValueError("Func must be callable")

        self.cases.add(key)
        if key == self.value or not self._found and key == self.__default:
            self._func_stack.append(func)
            self._found = True
            if fallthrough is not None:
                self._falling_through = fallthrough
            return True

    def __enter__(self) -> "Switch":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_val:
            raise exc_val

        if not self._func_stack:
            raise ValueError(f"Value does not match any case and there is not default case: value {self.value}")

        for func in self._func_stack:
            self.__result = func()

    @property
    def result(self):
        if self.__result == Switch.__no_result:
            raise ValueError("No result has been computed (did you access Switch.result inside the with block?)")
        return self.__result


def strict_range(start: int, stop: int, step: int = 1) -> range:
    """Returns string range of iterable numbers."""
    if start >= stop:
        raise ValueError("Start must be less than stop.")
    return range(start, stop + step, step)
