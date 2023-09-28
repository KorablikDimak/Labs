import timeit
import numpy


def my_program(A):
    det_A = A[0][0] * A[1][1] * A[2][2] + A[0][1] * A[1][2] * A[2][0] + A[0][2] * A[1][0] * A[2][1] - A[0][2] * A[1][
        1] * \
            A[2][0] - A[0][1] * A[1][0] * A[2][2] - A[0][0] * A[1][2] * A[2][1]

    A11 = A[1][1] * A[2][2] - A[1][2] * A[2][1]
    A12 = -(A[1][0] * A[2][2] - A[1][2] * A[2][0])
    A13 = A[1][0] * A[2][1] - A[1][1] * A[2][0]
    A21 = -(A[0][1] * A[2][2] - A[0][2] * A[2][1])
    A22 = A[0][0] * A[2][2] - A[0][2] * A[2][0]
    A23 = -(A[0][0] * A[2][1] - A[0][1] * A[2][0])
    A31 = A[0][1] * A[1][2] - A[0][2] * A[1][1]
    A32 = -(A[0][0] * A[1][2] - A[0][2] * A[1][0])
    A33 = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    return [[A11 / det_A, A21 / det_A, A31 / det_A], [A12 / det_A, A22 / det_A, A32 / det_A],
            [A13 / det_A, A23 / det_A, A33 / det_A]]


def numpy_program(A):
    return numpy.linalg.inv(A)


A = []

for i in range(1, 4):
    stroka = []
    for j in range(1, 4):
        print("Введите элемент матрицы с координатами {", i, "}, {", j, "}: ")
        stroka.append(int(input()))
    A.append(stroka)

print("Исходная матрица: ")
for stroka in A:
    print(stroka)

time_result = timeit.timeit("my_program", setup="from __main__ import my_program")
print(time_result)
time_result = timeit.timeit("numpy_program", setup="from __main__ import numpy_program")
print(time_result)
