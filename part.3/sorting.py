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
