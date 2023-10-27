import random
import timeit
import algorithm


def check(collection):
    for i in range(len(collection) - 1):
        if collection[i] > collection[i + 1]:
            print("Result: PANIC!\n")
            return
    print("Result: OK\n")


items = []
for i in range(1000):
    items.append(random.random() * 1000 - 500)

start_time = timeit.default_timer()
algorithm.bubble_sort(items)
print(f"bubble_sort time: {timeit.default_timer() - start_time}")

check(items)
items.clear()


items = []
for i in range(1000):
    items.append(random.random() * 1000 - 500)

start_time = timeit.default_timer()
items.sort()
print(f"sort time: {timeit.default_timer() - start_time}")

check(items)
items.clear()


arr = [1, 2, 3]
permutations = algorithm.generate_permutations(arr)
for p in permutations:
    print(p)


matrix1 = [[1, 3, 4],
           [3, 5, 1]]

matrix2 = [[8, 4],
           [7, 1],
           [9, 0]]

result = algorithm.multiple_matrix(matrix1, matrix2)
print("\n", result)
