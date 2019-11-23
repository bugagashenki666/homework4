lst = [int(x) for x in input("Введите массив чисел:\n").split()]
need = int(input("Введите искомое число:\n"))

lst_copy = lst.copy()
iterations = 0
while lst_copy:
    iterations += 1
    index = len(lst_copy) // 2
    pivot = lst_copy[index]
    if pivot > need:
        lst_copy = lst_copy[:index]
    elif pivot < need:
        lst_copy = lst_copy[index + 1:]
    else:
        print(f"{need} found for {iterations} iterations")
        break
else:
    print(f"{need} not found for {iterations} iterations")

iterations = 0
left = 0
right = len(lst) - 1
while left <= right:
    iterations += 1
    idx = (left + right) // 2
    if lst[idx] > need:
        right = idx - 1
    elif lst[idx] < need:
        left = idx + 1
    else:
        print(f"{need} found on index {idx} for {iterations} iterations")
        break
else:
    print(f"{need} not found for {iterations} iterations")
