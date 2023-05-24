n = int(input("Введите количество монет, которые лежат на столе: "))
count_zero = 0
count_one = 0
for i in range(n):
    x = int(input("Введите число (0 - решка, 1 - герб): "))
    if x == 0:
        count_zero += 1
    else:
        count_one += 1
if count_one > count_zero:
    print(count_zero)
else:
    print(count_one)
