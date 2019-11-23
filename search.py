
lst = [int(x) for x in input("Введите массив чисел:\n").split()]
need = int(input("Введите искомое число:\n"))

iterations = 0
for i, e in enumerate(lst):
    iterations += 1
    if need == e:
        print(f"found {e} on index {i} for {iterations} iterations")
        break
else:
    print(f"{need} not found for {iterations} iterations")
