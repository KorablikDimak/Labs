import numpy as np

print('Введите количество строк')
raz_1 = int(input())
print('Введите количество столбцов')
raz_2 = int(input())

#создание матрицы поэлементным вводом
matrix1 = []
s = []
n = 0
for i in range(raz_1):
    matrix1.append(s)
    for j in range(raz_2):
        print(f'Введите элемент {i + 1} {j + 1}')
        el = float(input())
        s.append(el)
        n += 1
        if n == 2:
            s = []
    n = 0

matrix = np.array(matrix1)


print("Выберите действие:")
print("1-транспонирование матрицы")
print("2-умножение матриц")
print("3-определение ранга матрицы")
o = int(input())

#транспонирование матрицы
if o == 1:
    print(f"транспонированная матрица =\n{np.transpose(matrix)}")

#умножение матриц
elif o == 2:
    print('Введите элементы матрицы - второго множителя')
    print('Введите количество строк')
    raz_11 = int(input())
    print('Введите количество столбцов')
    raz_21 = int(input())
    if raz_2 == raz_11:
        matrix2 = []
        s1 = []
        k = 0
        for i in range(raz_11):
            matrix2.append(s1)
            for j in range(raz_21):
                print(f'Введите элемент {i + 1} {j + 1}')
                elem = float(input())
                s1.append(elem)
                k += 1
                if k == 2:
                    s1 = []
            k = 0

        matrixm = np.array(matrix2)
        print(f"результат умножения =\n{np.dot(matrix, matrixm)}")
    else:
        print("Неподходящая размерность")

#нахождение ранга матрицы
if o == 3:
    print(f"ранг матрицы = {np.linalg.matrix_rank(matrix)}")
