import random
from typing import TypeVar

Self = TypeVar('Self', bound='Matrix')
Number = TypeVar('Number', bound='int | float | complex')


class Matrix:
    def __init__(self, row_count: int, column_count: int) -> None:
        if row_count <= 0 or column_count <= 0:
            raise Exception("row_count и column_count должны быть больше 0")

        self._table: list[list[Number]] = []
        self._row_count = row_count
        self._column_count = column_count

        for i in range(row_count):
            row: list[Number] = []
            for j in range(column_count):
                row.append(0)
            self._table.append(row)

    @staticmethod
    def from_matrix(matrix: Self) -> Self:
        copy = Matrix(matrix.row_count(), matrix.column_count())

        for i in range(copy.row_count()):
            for j in range(copy.column_count()):
                copy[i][j] = matrix[i][j]
        return copy

    @staticmethod
    def from_list(matrix: list[list[Number]]) -> Self:
        copy = Matrix(len(matrix), len(matrix[0]))

        for i in range(copy.row_count()):
            for j in range(copy.column_count()):
                copy[i][j] = matrix[i][j]
        return copy

    def __len__(self) -> tuple[int, int]:
        return self._row_count, self._column_count

    def __add__(self, other: Self) -> Self:
        if self._row_count != other.row_count() or self._column_count != other.column_count():
            raise Exception("Количество строк и столбцов у складываемых матриц должно совпадать")

        result = Matrix(self._row_count, self._column_count)
        for i in range(self._row_count):
            for j in range(self._column_count):
                result[i][j] = self._table[i][j] + other[i][j]

        return result

    def __iadd__(self, other: Self) -> None:
        if self._row_count != other.row_count or self._column_count != other.column_count():
            raise Exception("Количество строк и столбцов у складываемых матриц должно совпадать")

        for i in range(self._row_count):
            for j in range(self._column_count):
                self._table[i][j] += other[i][j]

    def __sub__(self, other: Self) -> Self:
        if self._row_count != other.row_count or self._column_count != other.column_count():
            raise Exception("Количество строк и столбцов у складываемых матриц должно совпадать")

        result = Matrix(self._row_count, self._column_count)
        for i in range(self._row_count):
            for j in range(self._column_count):
                result[i][j] = self._table[i][j] - other[i][j]

        return result

    def __isub__(self, other: Self) -> None:
        if self._row_count != other.row_count or self._column_count != other.column_count():
            raise Exception("Количество строк и столбцов у вычитаемых матриц должно совпадать")

        for i in range(self._row_count):
            for j in range(self._column_count):
                self._table[i][j] -= other[i][j]

    def __mul__(self, other: Self | Number) -> Self:
        if type(other) is Matrix:
            if self._column_count != other.row_count():
                raise Exception("Количество столбцов левой матрицы должно быть равно количеству строк правой матрицы")

            result = Matrix(self._row_count, other.column_count())

            for i in range(self._row_count):
                for j in range(other.column_count()):
                    c = 0
                    for k in range(self._column_count):
                        c += self._table[i][k] * other[k][j]
                    result[i][j] = c

            return result
        elif type(other) is float or type(other) is int or type(other) is complex:
            result = Matrix(self._row_count, self._column_count)
            for i in range(self._row_count):
                for j in range(self._column_count):
                    result = self._table[i][j] * other

            return result

    def __imul__(self, other: Number) -> None:
        for i in range(self._row_count):
            for j in range(self._column_count):
                self._table[i][j] *= other

    def __neg__(self) -> Self:
        neg_matrix = Matrix(self._row_count, self._column_count)

        for i in range(self._row_count):
            for j in range(self._row_count):
                neg_matrix[i][j] = -self._table[i][j]

        return neg_matrix

    def __invert__(self) -> Self:
        det: Number = self.det()
        if det == 0:
            raise Exception("Для нахождения обратной матрицы определитель не должен быть равен 0")

        inverse_matrix = Matrix(self._row_count, self._column_count)
        for i in range(self._row_count):
            for j in range(self._column_count):
                a: Number = self.algebraic_complement(i, j)
                inverse_matrix[j][i] = a / det

        return inverse_matrix

    def __eq__(self, other: Self) -> bool:
        if self._row_count != other.row_count or self._column_count != other.column_count():
            return False

        for i in range(self._row_count):
            for j in range(self._column_count):
                if abs(self._table[i][j] - other[i][j]) > 0.000000001:
                    return False
        return True

    def __ne__(self, other: Self) -> bool:
        if self._row_count != other.row_count or self._column_count != other.column_count():
            return True

        for i in range(self._row_count):
            for j in range(self._column_count):
                if abs(self._table[i][j] - other[i][j]) > 0.000000001:
                    return True
        return False

    def __getitem__(self, key: int) -> list[Number]:
        return self._table[key]

    def __setitem__(self, key: int, value: list[Number]) -> None:
        self._table[key] = value

    def __str__(self) -> str:
        result = ""
        for i in range(self._row_count):
            for j in range(self._column_count):
                result += f"{self._table[i][j]}\t"
            result += "\n"
        return result

    def row_count(self) -> int:
        return self._row_count

    def column_count(self) -> int:
        return self._column_count

    def transpose(self) -> Self:
        result = Matrix(self._column_count, self._row_count)

        for i in range(self._row_count):
            for j in range(self._column_count):
                result[j][i] = self._table[i][j]

        return result

    def erase_row(self, row_number: int) -> None:
        if self._row_count == 1:
            raise Exception("Нельзя удалить строку из матрицы с всего одной строкой")

        self._table.pop(row_number)
        self._row_count -= 1

    def erase_column(self, column_number: int) -> None:
        if self._column_count == 1:
            raise Exception("Нельзя удалить столбец из матрицы с всего одним столбцом")

        for i in range(self._row_count):
            self._table[i].pop(column_number)
        self._column_count -= 1

    def algebraic_complement(self, i: int, j: int) -> Number:
        minor_matrix = Matrix.from_matrix(self)
        minor_matrix.erase_row(i)
        minor_matrix.erase_column(j)
        return (-1) ** (i + j + 2) * minor_matrix.det()

    def det(self) -> Number:
        if self._row_count != self._column_count:
            raise Exception("Количество строк должно быть равно количеству столбцов")

        if self._row_count == 1:
            return self._table[0][0]

        result: Number = 0
        for i in range(self._row_count):
            result += self._table[i][0] * self.algebraic_complement(i, 0)
        return result

    def swap_row(self, row1_number: int, row2_number: int) -> None:
        temp: list[Number] = self._table[row1_number]
        self._table[row1_number] = self._table[row2_number]
        self._table[row2_number] = temp

    def swap_column(self, column1_number: int, column2_number: int) -> None:
        for i in range(self._row_count):
            temp: Number = self._table[i][column1_number]
            self._table[i][column1_number] = self._table[i][column2_number]
            self._table[i][column2_number] = temp

    def rank(self) -> int:
        rank = self._column_count
        copy = Matrix.from_matrix(self)

        for row in range(rank):
            if copy[row][row]:
                for col in range(self._row_count):
                    if col != row:
                        multiplier: Number = copy[col][row] / copy[row][row]
                        for i in range(rank):
                            copy[col][i] -= multiplier * copy[row][i]
            else:
                reduce = True

                for i in range(row + 1, self._row_count, 1):
                    if copy[i][row]:
                        copy.swap_row(i, rank)
                        reduce = False
                        break

                if reduce:
                    rank -= 1

                    for i in range(self._row_count):
                        copy[i][row] = copy[i][rank]

                row -= 1

        return rank

    def random(self, scale: Number = 1) -> Self:
        for i in range(self._row_count):
            for j in range(self._column_count):
                self._table[i][j] = random.random() - 0.5
                self._table[i][j] *= scale
        return self

    def input(self) -> Self:
        for i in range(self._row_count):
            for j in range(self._column_count):
                print(f"Введите элемент {i + 1}, {j + 1}: ")
                self._table[i][j] = float(input())
        return self

    def print(self) -> None:
        print(str(self))
