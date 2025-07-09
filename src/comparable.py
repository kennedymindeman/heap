from __future__ import annotations
from typing import Protocol


class Comparable(Protocol):
    def __lt__(self, other: Comparable) -> bool:
        ...

    def __gt__(self, other: Comparable) -> bool:
        ...

    def __le__(self, other: Comparable) -> bool:
        ...

    def __ge__(self, other: Comparable) -> bool:
        ...
