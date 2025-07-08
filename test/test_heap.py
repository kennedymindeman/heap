import pytest
from src.heap import EmptyHeapException, Heap
from random import randint, seed


def extract_all_from_heap(heap: Heap) -> list:
    heap_contents = []
    while not heap.is_empty():
        heap_contents.append(heap.extract_max())
    return heap_contents


@pytest.fixture(name="random_list")
def get_random_list() -> list:
    seed(69)
    return [randint(1, 1000) for _ in range(100)]


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


def test_heap_size_is_1_after_inserting() -> None:
    heap = Heap()
    heap.insert(0)
    assert heap.size() == 1


def test_peek_on_empty_heap_raises_exception() -> None:
    heap = Heap()
    with pytest.raises(EmptyHeapException):
        heap.peek()


def test_adding_to_heap_ascending() -> None:
    heap = Heap()
    heap.insert(0)
    heap.insert(1)
    assert heap.peek() == 1


def test_adding_3_nodes() -> None:
    heap = Heap()
    heap.insert(0)
    heap.insert(2)
    heap.insert(1)
    assert heap.peek() == 2


def test_adding_negative_values() -> None:
    heap = Heap()
    heap.insert(-1)
    heap.insert(-2)
    assert heap.peek() == -1


def test_extract_max_returns_highest_value() -> None:
    heap = Heap()
    heap.insert(0)
    heap.insert(1)
    assert heap.extract_max() == 1


def test_highest_value_on_top_after_extract_max() -> None:
    heap = Heap()
    heap.insert(0)
    heap.insert(2)
    heap.insert(1)
    heap.extract_max()
    assert heap.peek() == 1


def test_extract_max_on_size_1_heap() -> None:
    heap = Heap()
    heap.insert(0)
    assert heap.extract_max() == 0


def test_iterable_passed_to_constructor() -> None:
    heap = Heap([1, 2, 3])
    assert heap.size() == 3


def test_peek_after_passing_iterable_to_constructor() -> None:
    heap = Heap([1, 2, 3])
    assert heap.peek() == 3


def test_order_of_heap_after_constructor(random_list: list) -> None:
    heap = Heap(random_list)
    assert extract_all_from_heap(heap) == sorted(random_list, reverse=True)


def test_extract_max_on_empty_heap_raises_exception() -> None:
    heap = Heap()
    with pytest.raises(EmptyHeapException):
        heap.extract_max()


def test_heaps_made_from_inserts_match_constructor_version(random_list: list) -> None:
    heap1 = Heap(random_list)
    heap2 = Heap()
    for num in random_list:
        heap2.insert(num)
    assert extract_all_from_heap(heap1) == extract_all_from_heap(heap2)
