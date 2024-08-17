def binary_search(arr:list, target, left, right):
    if left > right:
        return -1  # базовый случай: если границы сошлись и элемент не найден

    mid = (left + right) // 2  # находим середину

    if arr[mid] == target:  # если нашли цель
        return mid
        print(3)
    elif arr[mid] < target:  # если цель больше середины
        return binary_search(arr, target, mid + 1, right)  # ищем в правой половине
        print(1)
    else:  # если цель меньше середины
        return binary_search(arr, target, left, mid - 1)  # ищем в левой половине
        print(2)
    print(4)
print()
binary_search([1, 3, 5, 7, 9, 11, 13, 15],5,0, len([1, 3, 5, 7, 9, 11, 13, 15]) - 1)