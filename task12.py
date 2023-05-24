sum = int(input("Введите сумму загаданных чисел: "))
mult = int(input("Введите произведение загаданных чисел: "))
result = False

for i in range(sum):
    for j in range(sum):
        if (i + j == sum) and (i * j == mult):
            print(f"Загаданные числа: {i}, {j}")
            result = True
            break
    if result:
        break
