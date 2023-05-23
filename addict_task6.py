number = str(input("Введите номер билета: "))
if (int(number[0]) + int(number[1]) + int(number[2])) == (int(number[3]) + int(number[4]) + int(number[5])):
    print("Ваш билет счастливый")
else:
    print("Ваш билет не является счастливым")
