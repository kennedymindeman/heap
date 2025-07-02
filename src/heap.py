from typing import Any


class Heap:
    def __init__(self) -> None:
        self._data = []

    def add(self, item: int) -> None:
        self._data.append(item)

    def peek(self) -> Any:
        return self._data[0]

    def is_empty(self) -> bool:
        raise NotImplementedError
