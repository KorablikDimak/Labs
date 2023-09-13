import math

while True: # проверка корректного ввода
    print('Выберите функцию: \n 1 - сложение,\n 2 - вычитание, \n 3 - умножение,\n 4 - деление,\n '
          '5 - возведение в степень,\n 6 - логарифм,\n 7 - округление в большую сторону,\n '
          '8 - округление в меньшую сторону')
    try:
        number_of_operation = int(input())
        break
    except ValueError:
        print('Вы написали не число')

while True: # проверка корректного ввода
    print('Введите первый элемент')
    try:
        a = float(input())
        break
    except ValueError:
        print('Вы написали не число')

while True: # проверка корректного ввода
    print('Введите второй элемент')
    try:
        b = float(input())
        break
    except ValueError:
        print('Вы написали не число')

if number_of_operation == 1:  # сложение
    print(a + b)
elif number_of_operation == 2:  # вычитание
    print(a - b)
elif number_of_operation == 3:  # умножение
    print(a * b)
elif number_of_operation == 4:  # деление
    print(a / b)
elif number_of_operation == 5:  # возведение в степень
    print(a ** b)
elif number_of_operation == 6:  # логарифм
    print(math.log(a, b))
elif number_of_operation == 7:  # округление в большую сторону
    while True:
        if b % 1 == 0 : # количество знаков после запятой может быть только натуральным числом
            if math.floor(a * (10 ** (b))) % 1 == 0: # забавный костыль, но он работает
                a = a // 10 ** (-b) / 10 ** b
            else:
                a = (a // 10 ** (-b) / 10 ** b) + 10 ** (-b)
            print(a)
            break
        else:
            print('Второй элемент должен быть целым натуральным числом')
elif number_of_operation == 8:  # округление в меньшую сторону
    while True:
        if b % 1 == 0: # количество знаков после запятой может быть только натуральным числом
            a = a // 10 ** (-b) / 10 ** b
            print(a)
            break
        else:
            print('Второй элемент должен быть целым натуральным числом')
else:
    print('Функции с таким номером не существует')
