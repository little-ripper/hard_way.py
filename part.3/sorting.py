def bubble_sort(iterators):
    while True:
        is_swapped = False
        node = iterators.begin.next
        while node:
            if node.prev.value > node.value:
                node.prev.value, node.value = node.value, node.prev.value
                is_swapped = True
            node = node.next
        if not is_swapped:
            break


def count(node):
    count = 0
    while node:
        node = node.next
        count += 1
    return count


def merge_sort_count(iterators):
    iterators.begin = merge_node_count(iterators.begin)
    node = iterators.begin
    while node.next:
        node = node.next
    iterators.end = node


def merge_node_count(start):
    if start.next is None:
        return start
    mid = count(start) // 2
    scanner = start
    for i in range(0, mid-1):
        scanner = scanner.next
    mid_node = scanner.next
    scanner.next = None
    mid_node.prev = None
    merged_left = merge_node_count(start)
    merged_right = merge_node_count(mid_node)
    return merge_count(merged_left, merged_right)


def merge_count(left, right):
    result = None
    if left is None:
        return right
    if right is None:
        return left
    if left.value > right.value:
        result = right
        result.next = merge_count(left, right.next)
    else:
        result = left
        result.next = merge_count(left.next, right)
    result.next.prev = result
    return result


def merge_sort(iterators):
    iterators.begin = merge_node(iterators.begin, iterators.count())
    node = iterators.begin
    while node.next:
        node = node.next
    iterators.end = node


def merge_node(start, num_items):
    if start.next is None:
        return start
    mid = num_items // 2
    scanner = start
    for i in range(0, mid-1):
        scanner = scanner.next
    mid_node = scanner.next
    scanner.next = None
    mid_node.prev = None
    merged_left = merge_node(start, mid)
    merged_right = merge_node(mid_node, mid)
    return merge(merged_left, merged_right)


def merge(left, right):
    result = None
    if left is None:
        return right
    if right is None:
        return left
    if left.value > right.value:
        result = right
        result.next = merge(left, right.next)
    else:
        result = left
        result.next = merge(left.next, right)
    result.next.prev = result
    return result


def partition(iterators, lo, hi):
    pivot = iterators.get((lo + hi + 1) // 2)
    i = lo
    j = hi
    while True:
        while i < j and iterators.get(i) < pivot:
            i += 1
        while j > i and iterators.get(j) > pivot:
            j -= 1
        if i < j:
            print(iterators, i, j)
            val_i = iterators.get(i)
            val_j = iterators.get(j)
            (
                iterators.get_node(i).value,
                iterators.get_node(j).value
            ) = val_j, val_i
            i += 1
            j -= 1
            print(iterators, i, j)
        else:
            return j


def quick_s(iterators, lo, hi):
    if hi <= lo:
        return
    j = partition(iterators, lo, hi)
    print(j, end='')
    quick_s(iterators, lo, j - 1)
    quick_s(iterators, j, hi)


def quick_sort(iterators):
    quick_s(iterators, 0, iterators.count() - 1)
