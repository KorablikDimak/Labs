print('Выберите функцию: Сложение, Вычитание, Умножение, Деление, Возведение в степень, Логарифм...')
f = input()
print('Введите первый операнд')
a = int(input())
print('Введите второй операнд')
b = int(input())
if f == 'Сложение' or f == 'сложение':
    print(a+b)
if f == 'Вычитание' or f == 'вычитание':
    print(a-b)
if f == 'Умножение' or f == 'умножение':
    print(a*b)
if f == 'Деление' or f == 'деление':
    print(a//b)
if f == 'Возведение в степень' or f == 'возведение в степень':
    print(a**b)
if f == 'Логарифм' or f == 'логарифм':
    import math
    print(math.log(a, b))
if f == 'Округление в большую сторону' or f == 'округление в большую сторонуа':
    print(a//10**(-b))

def умножение(a, b):
    return a*b
def сложение(a, b):
    return a+b
def вычитание(a, b):
    return a-b
def деление(a, b):
    return a//b
print('*словечки для пользователя*')
f=input()
a=int(input())
b=int(input())
print(f(a,b))