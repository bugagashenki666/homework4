N = int(input())
lst = [int(x) for x in input().split()]
num, position = [int(x) for x in input().split()]
if 0 <= position < N:
    lst.insert(position, num)
elif position >= N:
    lst.append(num)
    s = ""
for i in lst:
    s += str(i) + ' '
print(s)