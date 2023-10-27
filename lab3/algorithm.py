import math


def merge_sort(collection):
    merge_sort_(collection, 0, len(collection) - 1)


def merge_sort_(collection, start, end):
    if start >= end:
        return
    mid = (start + end) // 2
    merge_sort_(collection, start, mid)
    merge_sort_(collection, mid + 1, end)
    merge(collection, start, mid, end)


def merge(collection, start, mid, end):
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


def quick_sort(collection):
    quick_sort_(collection, 0, len(collection) - 1)


def quick_sort_(collection, start, end):
    if start >= end:
        return
    mid = partition(collection, start, end)
    if mid != 0:
        quick_sort_(collection, start, mid - 1)
    quick_sort_(collection, mid + 1, end)


def partition(collection, start, end):
    mid = start

    for i in range(start, end):
        if collection[i] <= collection[end]:
            select = collection[mid]
            collection[mid] = collection[i]
            collection[i] = select
            mid += 1

    select = collection[mid]
    collection[mid] = collection[end]
    collection[end] = select

    return mid


def insertion_sort(collection):
    for i in range(len(collection)):
        select = collection[i]
        j = i - 1

        while j >= 0 and select < collection[j]:
            collection[j + 1] = collection[j]
            j -= 1

        collection[j + 1] = select


def bucket_sort(collection):
    minimum = min(collection)
    maximum = max(collection)
    block_count = math.ceil(math.log2(len(collection)))
    if block_count == 0:
        return

    bucket = {}
    block_indexes = []

    for i in range(block_count):
        index = minimum + (maximum - minimum) / block_count * i
        bucket[index] = []
        block_indexes.append(index)

    for element in collection:
        for i in range(block_count - 1, -1, -1):
            if element >= block_indexes[i]:
                bucket[block_indexes[i]].append(element)
                break

    for block in bucket.values():
        if len(block) == 0:
            continue
        insertion_sort(block)

    count = 0

    for i in range(block_count):
        block = bucket[block_indexes[i]]
        size = len(block)
        if size == 0:
            continue

        for j in range(size):
            collection[count] = block[j]
            count += 1


def comb_sort(collection):
    step = len(collection) - 1
    while step >= 1:
        for i in range(len(collection) - step):
            if collection[i + step] < collection[i]:
                temp = collection[i]
                collection[i + step] = collection[i]
                collection[i] = temp

        step = int(step / 1.2473309)
