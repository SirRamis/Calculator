"""Бинарный поиск — это эффективный алгоритм для поиска элемента в отсортированном массиве.
Основная идея заключается в том,
 чтобы делить массив пополам и сравнивать элемент с центральным элементом массива,
уменьшая область поиска вдвое на каждом шаге."""


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # находим середину

        if arr[mid] == target:  # если нашли цель
            return mid
        elif arr[mid] < target:  # если цель больше середины
            left = mid + 1
        else:  # если цель меньше середины
            right = mid - 1

    return -1  # если элемент не найден


arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7

result = binary_search(arr, target)

if result != -1:
    print(f"Элемент найден на позиции: {result}")
else:
    print("Элемент не найден")
