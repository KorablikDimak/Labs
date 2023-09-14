import math

while True:  # проверка корректного ввода
    print('Выберите функцию: \n 1 - сложение,\n 2 - вычитание, \n 3 - умножение,\n 4 - деление,\n '
          '5 - возведение в степень,\n 6 - логарифм,\n 7 - округление в большую сторону,\n '
          '8 - округление в меньшую сторону')
    try:
        number_of_operation = int(input())
        break
    except ValueError:
        print('Вы написали не число')

while True:  # проверка корректного ввода
    print('Введите первый элемент')
    try:
        a = float(input())
        break
    except ValueError:
        print('Вы написали не число')

while True:  # проверка корректного ввода
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
    if b == 0:
        print('Деление на 0 недопустимо')
    else:
        print(a / b)
elif number_of_operation == 5:  # возведение в степень
    print(a ** b)
elif number_of_operation == 6:  # логарифм
    try:
        print(math.log(a, b))
    except:
        print('Значение неопределено')
elif number_of_operation == 7:  # округление в большую сторону
    if b.is_integer() and b >= 0:  # количество знаков после запятой может быть только целым неотрицательным числом
        a = math.ceil(a * 10**b) / 10**b
        print(a)
    else:
        print('Второй элемент должен быть целым неотрицательным числом')
elif number_of_operation == 8:  # округление в меньшую сторону
    if b.is_integer() and b >= 0:  # количество знаков после запятой может быть только целым неотрицательным числом
        a = math.floor(a * 10**b) / 10**b
        print(a)
    else:
        print('Второй элемент должен быть целым неотрицательным числом')
else:
    print('Функции с таким номером не существует')
