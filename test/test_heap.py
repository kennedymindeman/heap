from src.heap import Heap


def test_initialization() -> None:
    Heap()


def test_insert_to_empty_heap() -> None:
    heap = Heap()
    heap.insert(0)
    assert heap.peek() == 0


def test_heap_is_empty_on_initialization() -> None:
    heap = Heap()
    assert heap.is_empty()


def test_heap_is_not_empty_after_inserting() -> None:
    heap = Heap()
    heap.insert(0)
    assert not heap.is_empty()


def test_heap_size_is_0_on_initialization() -> None:
    heap = Heap()
    assert heap.size() == 0
