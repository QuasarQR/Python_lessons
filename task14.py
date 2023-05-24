N = int(input("Введите число N: "))
for i in range(1, N // 2):
    if (2 ** i) <= N:
        print(2 ** i)
