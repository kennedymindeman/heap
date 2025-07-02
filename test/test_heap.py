from src.heap import Heap


def test_initialization() -> None:
    heap = Heap()


def test_add_to_empty_heap() -> None:
    heap = Heap()
    heap.add(0)
    assert heap.lst == [0]
