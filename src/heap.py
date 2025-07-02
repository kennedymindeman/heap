from typing import Any


class Heap:
    def __init__(self) -> None:
        self.lst = []

    def add(self, item: int) -> None:
        self.lst.append(item)

    def peek(self) -> Any:
        return self.lst[0]
