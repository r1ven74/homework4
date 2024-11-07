try:
    n = int(input("Введите кол-во пар"))
    lst = []

    for i in range(n):
        one, two = map(int, input().split())
        lst.append((one, two))

    max_sum = 0

    for o in range(2 ** n):
        current_sum = 0
        for p in range(n):
            if (o >> p) and 1:
                current_sum += lst[p][0]
            else:
                current_sum += lst[p][1]

        if current_sum % 3 == 0:
            max_sum = max(max_sum, current_sum)

    print(max_sum)
except ValueError:
    print("Напиши ДВА ЧИСЛА")
