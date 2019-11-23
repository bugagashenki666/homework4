a = [int(x) for x in input().split()]
# a = list(map(int, input().split()))
n = len(a)

for i in range(1, n):
    for j in range(n - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)
