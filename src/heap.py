from typing import Any


class HeapException(Exception):
    pass


class EmptyHeapException(HeapException):
    pass


class Heap:
    def __init__(self) -> None:
        self._data = []

    def insert(self, item: int) -> None:
        self._data.append(item)
        new_item_index = self.size() - 1
        while True:
            parent_index = (new_item_index - 1) // 2
            if (
                parent_index < 0 or
                self._data[parent_index] >= self._data[new_item_index]
            ):
                break
            self._swap(parent_index, new_item_index)
            new_item_index = parent_index

    def peek(self) -> Any:
        if self.is_empty():
            raise EmptyHeapException("Can't peek at an empty heap")
        return self._data[0]

    def is_empty(self) -> bool:
        return self.size() == 0

    def size(self) -> int:
        return len(self._data)

    def extract_max(self) -> Any:
        if self.is_empty():
            raise EmptyHeapException("Can't extract max from an empty heap")
        ret = self._data[0]
        self._data[0] = self._data.pop()
        curr_index = 0
        while True:
            left = curr_index * 2 + 1
            if left >= self.size():
                break
            right = curr_index * 2 + 2
            if right >= self.size():
                self._swap(curr_index, left)
                break
            swap_index = max([left, right], key=lambda x: self._data[x])
            self._swap(curr_index, swap_index)
            curr_index = swap_index
        return ret

    def _swap(self, index1: int, index2: int) -> None:
        self._data[index1], self._data[index2] = self._data[index2], self._data[index1]
