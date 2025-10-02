import sorting
from double_linked_lists import DoubleLinkedList
from random import randint


MAX_NUMBERS = 5


def random_list(count):
    iterators = DoubleLinkedList()
    for i in range(count, 0, -1):
        iterators.shift(randint(0, 10000))
    return iterators


def is_sorted(iterators):
    node = iterators.begin
    while node and node.next:
        if node.value > node.next.value:
            return False
        else:
            node = node.next
    return True


def test_bubble_sort():
    iterators = random_list(MAX_NUMBERS)
    sorting.bubble_sort(iterators)
    assert is_sorted(iterators)


def test_merge_sort_count():
    iterators = random_list(MAX_NUMBERS)
    sorting.merge_sort_count(iterators)
    assert is_sorted(iterators)


def test_merge_sort():
    iterators = random_list(MAX_NUMBERS)
    sorting.merge_sort(iterators)
    assert is_sorted(iterators)


def test_quick_sort():
    iterators = random_list(MAX_NUMBERS)
    sorting.quick_sort(iterators)
    assert is_sorted(iterators)
