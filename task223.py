# N = int(input("Введите размер  массива:\n"))
# m = [int(x) for x in input("Введите массив:\n").split(sep=" ", maxsplit=N)]
# x = int(input("Введите искомое число:\n"))
# print(m)
N = int(input())
m = [int(x) for x in input().split(sep=" ", maxsplit=N)]
x = int(input())
count_x = 0
for n in m:
    if x == n:
        count_x += 1

print(count_x)
