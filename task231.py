def print_list(l):
    s = ""
    for i_ in l:
        s += str(i_) + ' '
    print(s)


def solution(l, pos, num_):
    l.append(0)
    for i in range(len(l) - 1, pos - 1, -1):
        l[i] = l[i - 1]
    l[pos - 1] = num_
    print_list(l)


def solution2(l, pos, num_):
    l.insert(pos - 1, num_)
    print_list(l)


def solution3(l, pos, num_):
    l1 = l[:pos - 1] + [num_] + l[pos - 1:]
    print_list(l1)


N = int(input())
lst = [int(x) for x in input().split()]
num, position = [int(x) for x in input().split()]
solution2(lst, position, num)
