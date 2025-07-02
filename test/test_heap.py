from src.heap import Heap


def test_initialization() -> None:
    Heap()


def test_add_to_empty_heap() -> None:
    heap = Heap()
    heap.add(0)
    assert heap.peek() == 0


def test_heap_is_empty_on_initialization() -> None:
    heap = Heap()
    assert heap.is_empty()


def test_heap_is_not_empty_after_adding() -> None:
    heap = Heap()
    heap.add(0)
    assert not heap.is_empty()
