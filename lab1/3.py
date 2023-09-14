def fib(previous: int, current: int, target: int) -> bool:
    if target == 0:
        return True
    elif current == target:
        return True
    elif current > target:
        return False
    else:
        return fib(current, current + previous, target)


while True:
    print("Введите число на проверку принадлежности к числам Фибоначчи:")
    try:
        target = int(input())
        print(fib(0, 1, target))
    except ValueError:
        print("Ошибка ввода")
