from typing import Any


class HeapException(Exception):
    pass


class EmptyHeapException(HeapException):
    pass


class Heap:
    def __init__(self) -> None:
        self._data = []

    def insert(self, item: int) -> None:
        def swap(lst: list, index1: int, index2: int) -> None:
            lst[index1], lst[index2] = lst[index2], lst[index1]

        self._data.append(item)
        new_item_index = self.size() - 1
        while True:
            parent_index = (new_item_index - 1) // 2
            if (
                parent_index < 0 or
                self._data[parent_index] >= self._data[new_item_index]
            ):
                break
            swap(self._data, parent_index, new_item_index)
            new_item_index = parent_index

    def peek(self) -> Any:
        if self.is_empty():
            raise EmptyHeapException("Can't peek at an empty heap")
        return self._data[0]

    def is_empty(self) -> bool:
        return self.size() == 0

    def size(self) -> int:
        return len(self._data)
