from random import randrange


def bs(iterable, target):
    """iterable MUST be already sorted."""
    if not iterable:
        return None
    index = len(iterable) // 2
    mid = iterable[index]
    if mid == target:
        return mid
    elif mid > target:
        return bs(iterable[:index], target)
    else:
        return bs(iterable[index + 1:], target)


iterable = [randrange(0, 10) for _ in range(10)]
# print(iterable)
sorted_iterable = sorted(iterable)
print(sorted_iterable)
print(bs(sorted_iterable, 8))
