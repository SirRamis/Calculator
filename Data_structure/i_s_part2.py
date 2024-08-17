def part2_1():
    l = int(input())
    a = l // 100
    print(f"{l}см = {a} метр")


part2_1()


def part2_2():
    m = int(input())
    a = m // 1000
    print(f"{m}кг = {a} тон")


part2_2()


def part2_3():
    b = int(input())
    a = b // 1024
    print(f"{b}байта = {a} килобайт")


part2_3()


def part2_4():
    a = int(input())
    b = int(input())
    c = a // b
    print(f"На отрезке длины {a}, {c} количество отрезков")


part2_4()


def part2_5():
    a = int(input())
    b = int(input())
    c = a % b
    print(f"На отрезке длины {a}, {c} незанятой части")


part2_5()


def part2_6():
    a = int(input())
    print(f"Десятки {a // 10}, единицы {a % 10}")


part2_6()


def part2_7():
    a = int(input())
    b = a // 10
    c = a % 10
    print(f"Cуммa {b + c}, произведение {b * c}")


part2_7()


def part2_8():
    a = int(input())
    b = a // 10
    c = a % 10
    print(f"Перестановочное число {c}{b}")


part2_8()


def part2_9():
    a = int(input())
    b = a // 100
    print(f"Сотни {b}")


part2_9()


def part2_10():
    a = int(input())
    b = a % 10
    c = a % 100 // 10
    print(f"Единицы {b}, десятки {c}")


part2_10()
