import random

def quick_sort_easy(arr):
    if len(arr) <= 1:
        return arr

    pivot = random.randint(0, len(arr) - 1)

    less = []
    greater = []

    for index, value in enumerate(arr):
        if index == pivot:
            continue

        if value <= arr[pivot]:
            less.append(value)
        else:
            greater.append(value)

    return quick_sort_easy(less) + [arr[pivot]] + quick_sort_easy(greater)


arr = [random.randint(1,50) for i in range(10)]

print quick_sort_easy(arr)

