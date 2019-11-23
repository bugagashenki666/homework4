import timeit

lst = [int(x) for x in input().split()]
n = len(lst) - 1
iterations = 0
for idx in range(1, n + 1):
    while lst[idx] < lst[idx - 1] and idx > 0:
        iterations += 1
        lst[idx], lst[idx - 1] = lst[idx - 1], lst[idx]
        idx -= 1

print(lst)
print(iterations)
