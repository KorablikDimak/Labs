import random
import algorithm
import timeit


def check(collection):
    for i in range(len(collection) - 1):
        if collection[i] > collection[i + 1]:
            print("Result: PANIC!\n")
            return
    print("Result: OK\n")


items = []
for i in range(100000):
    items.append(random.random() * 1000 - 500)

start_time = timeit.default_timer()
algorithm.merge_sort(items, 0, 99999)
print(f"merge_sort time: {timeit.default_timer() - start_time}")

check(items)
items.clear()


items = []
for i in range(100000):
    items.append(random.random() * 1000 - 500)

start_time = timeit.default_timer()
algorithm.quick_sort(items, 0, 99999)
print(f"quick_sort time: {timeit.default_timer() - start_time}")

check(items)
items.clear()


items = []
for i in range(10000):
    items.append(random.random() * 1000 - 500)

start_time = timeit.default_timer()
algorithm.bucket_sort(items)
print(f"bucket_sort time: {timeit.default_timer() - start_time}")

check(items)
items.clear()


items = []
for i in range(100000):
    items.append(random.random() * 1000 - 500)

start_time = timeit.default_timer()
algorithm.comb_sort(items)
print(f"comb_sort time: {timeit.default_timer() - start_time}")

check(items)
items.clear()
