def _abs(n):
    if n < 0:
        return -1 * n
    return n


# Линейный поиск не проходит тесты по времени
def print_match(ar1, ar2, n, k):
    for i in range(0, k):
        for j in range(0, n):
            match__ = ar1[j]
            if ar2[i] <= ar1[j]:
                if j == 0:
                    match__ = ar1[j]
                else:
                    if ar1[j] - ar2[i] >= ar2[i] - ar1[j - 1]:
                        match__ = ar1[j - 1]
                    else:
                        match__ = ar1[j]
                break
            j += 1
        print(match__)
        i += 1


def get_deltas(arr, lbound, rbound, index, need):
    delta1 = _abs(arr[index] - need)
    if lbound < index < rbound:
        delta2 = _abs(arr[index - 1] - need)
        delta3 = _abs(arr[index + 1] - need)
    elif index == lbound:
        delta2 = None
        delta3 = _abs(arr[index + 1] - need)
    elif index == rbound:
        delta2 = _abs(arr[index - 1] - need)
        delta3 = None
    return delta1, delta2, delta3


def match(arr1, index, delta, delta_plus, delta_minus):
    if delta_minus is None:
        min_delta = min(delta, delta_plus)
        if min_delta == delta_plus != delta:
            return arr1[index + 1]
        elif min_delta == delta != delta_plus or min_delta == delta == delta_plus:
            return arr1[index]
    elif delta_plus is None:
        min_delta = min(delta, delta_minus)
        if min_delta == delta != delta_minus:
            return arr1[index]
        elif min_delta == delta_minus != delta or min_delta == delta_minus == delta:
            return arr1[index - 1]
    else:
        min_delta = min(delta, delta_plus, delta_minus)
        if min_delta == delta_minus != delta or min_delta == delta_minus == delta:
            return arr1[index - 1]
        elif min_delta == delta_plus != delta:
            return arr1[index + 1]
        elif min_delta == delta_plus == delta or min_delta == delta:
            return arr1[index]


# бинарный поиск должен работать быстрее
def search_binary(arr1, a2i):
    left = 0
    right = len(arr1) - 1
    while left <= right:
        index = (left + right) // 2
        if arr1[index] > a2i:
            right = index - 1
        elif arr1[index] < a2i:
            left = index + 1
        else:
            break
    delta, delta_minus, delta_plus = get_deltas(arr1, 0, len(arr1) - 1, index, a2i)
    return match(arr1=arr1, index=index, delta=delta, delta_minus=delta_minus, delta_plus=delta_plus)


def print_match_binary(ar1, ar2, n, k):
    for i in range(0, k):
        match_ = search_binary(ar1, ar2[i])
        print(match_)


N, K = input().split()
N, K = int(N), int(K)
a1 = [int(x) for x in input().split()]
a2 = [int(x) for x in input().split()]
# print_match(a1, a2, N, K)
print_match_binary(tuple(a1), tuple(a2), N, K)
