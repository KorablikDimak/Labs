import math

while(True):
    print('Выберите функцию: 1- сложение, 2- вычитание, 3- умножение, 4- деление, 5- возведение в степень, '
          '6- логарифм, 7- округление в большую сторону, 8- округление в меньшую сторону')

    number_of_operation = input()
    if not number_of_operation.isnumeric():
        print('Вы написали не число')
        continue
    number_of_operation = int(number_of_operation)

    print('Введите первый элемент')
    a = float(input())
    print('Введите второй элемент')
    b = float(input())

    if number_of_operation == 1: #сложение
        print(a + b)
    elif number_of_operation == 2: #вычитание
        print(a - b)
    elif number_of_operation == 3: #умножение
        print(a * b)
    elif number_of_operation == 4: #деление
        print(a / b)
    elif number_of_operation == 5: #возведение в степень
        print(a ** b)
    elif number_of_operation == 6: #логарифм
        print(math.log(a, b))
    elif number_of_operation == 7: #округление в большую сторону
        print(math.ceil(a, b))
    elif number_of_operation == 8: #округление в меньшую сторону
        print(math.floor(a, b))
    else:
        print('Функции с таким номером не существует')
