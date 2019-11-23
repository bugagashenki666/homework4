from random import choice, randint


def quicksort_python_recursive(lst):
    if not lst:
        return lst
    med = choice(lst)
    less = [x for x in lst if x < med]
    equal = [x for x in lst if x == med]
    great = [x for x in lst if x > med]

    less = quicksort_python_recursive(less)
    great = quicksort_python_recursive(great)
    return less + equal + great


def quicksort_recursive(lst, left=0, right=None):
    if right is None:
        right = len(lst) - 1
    if left >= right:
        return
    pivot = lst[randint(left, right)]
    _left = left
    _right = right
    while _left <= _right:
        while lst[_left] < pivot:
            _left += 1
        while lst[_right] > pivot:
            _right -= 1

        if _left <= _right:
            lst[_left], lst[_right] = lst[_right], lst[_left]
            _left += 1
            _right -= 1

    quicksort_recursive(lst, left, _right)
    quicksort_recursive(lst, _left, right)


lst = [int(x) for x in input().split()]
lst1 = lst.copy()
lst1 = quicksort_python_recursive(lst1)
print("quick_sort_recursive: ", lst1)

lst2 = lst.copy()
quicksort_recursive(lst2)
print("quick_sort: ", lst2)
