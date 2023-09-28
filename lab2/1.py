from Matrix import Matrix

matrix1 = Matrix.from_list([[1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 9]])

matrix2 = Matrix.from_list([[5, 8, 9],
                            [4, 5, 6],
                            [1, 2, 5]])

matrix3 = matrix1 * matrix2
print(f"matrix3 =\n{matrix3}")

matrix4 = matrix1 + matrix2
print(f"matrix4 =\n{matrix4}")

print(f"det of matrix1 = {matrix1.det()}\n")
print(f"det of matrix2 = {matrix2.det()}\n")

print(f"inverse matrix2 =\n{~matrix2}")

print(f"rank of matrix2 =\n{matrix2.rank()}")

print(f"negative matrix1 =\n{-matrix1}")

matrix5 = Matrix(3, 3).random()
print(f"matrix5 =\n{matrix5}")

matrix6 = Matrix(2, 2).input()
print(f"matrix6 =\n{matrix6}")
