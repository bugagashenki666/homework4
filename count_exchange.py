n = int(input())
a = [int(x) for x in input().split()]
count_exchange = 0

for i in range(1, n):
    for j in range(n - i):
        if a[j] > a[j + 1]:
            count_exchange += 1
            a[j], a[j + 1] = a[j + 1], a[j]

print(count_exchange)