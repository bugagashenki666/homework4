def print_list(l):
    s = ""
    for i, e in enumerate(l):
        s += str(e) + " "
    print(f"{s}")


n = int(input())
lst = [int(x) for x in input().split()]
for idx in range(1, n):
    while lst[idx] < lst[idx - 1] and idx > 0:
        lst[idx], lst[idx - 1] = lst[idx - 1], lst[idx]
        idx -= 1
    
