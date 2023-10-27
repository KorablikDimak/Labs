def bubble_sort(collection: list):
    n = len(collection)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if collection[j] > collection[j + 1]:
                collection[j], collection[j + 1] = collection[j + 1], collection[j]


# абсолютно бессмысленный алгоритм, который просто удаляет 3 минимальных элемента, имеет сложность O(3n)
def o_3n(collection: list):
    minimum = collection[0]
    for i in range(3):
        for j in range(len(collection)):
            if collection[j] < minimum:
                minimum = collection[j]
        collection.remove(minimum)


# взят из предыдущей лабы, всегда имеет сложность O(n*log(n))
def merge_sort(collection: list):
    merge_sort_(collection, 0, len(collection) - 1)


def merge_sort_(collection: list, start: int, end: int):
    if start >= end:
        return
    mid = (start + end) // 2
    merge_sort_(collection, start, mid)
    merge_sort_(collection, mid + 1, end)
    merge(collection, start, mid, end)


def merge(collection: list, start: int, mid: int, end: int):
    n1 = mid - start + 1
    n2 = end - mid

    array1 = []
    for i in range(start, mid + 1):
        array1.append(collection[i])

    array2 = []
    for i in range(mid + 1, end + 1):
        array2.append(collection[i])

    i = 0
    j = 0

    for k in range(start, end + 1):
        if i != n1 and (j == n2 or array1[i] < array2[j]):
            collection[k] = array1[i]
            i += 1
        elif j != n2 and (i == n1 or array2[j] < array1[i]):
            collection[k] = array2[j]
            j += 1
        elif i != n1 and (j == n2 or array1[i] == array2[j]):
            collection[k] = array1[i]
            i += 1


# имеет факториальную сложность и генерирует все возможные перестановки коллекции
def generate_permutations(collection: list):
    n = len(collection)

    # Базовый случай - если длина массива равна 1, возвращаем его
    if n == 1:
        return [collection]

    # Инициализация списка для хранения всех перестановок
    permutations = []

    # Генерация перестановок
    for i in range(n):
        # Создаем копию массива без текущего элемента
        copy = collection[:i] + collection[i + 1:]

        # Генерация всех перестановок для оставшегося массива
        for element in generate_permutations(copy):
            # Добавляем текущий элемент в начало каждой перестановки
            permutations.append([collection[i]] + element)

    # Возвращаем список всех перестановок
    return permutations


# алгоритм перемножения матриц в чистом виде имеет сложность O(n^3)
def multiple_matrix(left_matrix: list[list], right_matrix: list[list]):
    if len(left_matrix[0]) != len(right_matrix):
        raise Exception("Количество столбцов левой матрицы должно быть равно количеству строк правой матрицы")

    result = []

    for i in range(len(left_matrix)):
        result.append([])
        for j in range(len(right_matrix[0])):
            result[i].append(0)

    for i in range(len(left_matrix)):
        for j in range(len(right_matrix[0])):
            c = 0
            for k in range(len(left_matrix[0])):
                c += left_matrix[i][k] * right_matrix[k][j]
            result[i][j] = c

    return result


# снова какой-то бред но допустим оно имеет сложность O(3log(n))
def o_3log_n(collection):
    double_minimum = min(collection) * 2
    index = binary_search(collection, double_minimum)
    if index != -1:
        print(f"double_minimum found")

    average_min_max = (min(collection) + max(collection)) / 2
    index = binary_search(collection, average_min_max)
    if index != -1:
        print(f"average_min_max found")

    half_max = max(collection) / 2
    index = binary_search(collection, half_max)
    if index != -1:
        print(f"half_max found")


# сам по себе имеет сложность O(log(n), но вызывать его будем три раза
def binary_search(collection: list, target):
    low = 0
    high = len(collection) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = collection[mid]

        if guess == target:
            return mid
        elif guess < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # если элемент не найден
