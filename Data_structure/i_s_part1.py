def part1_1(x: int) -> float:
    a = float(input())
    print(f"Периметр равна : {4 * a}")


part1_1()


def part1_2():
    a = float(input())
    print(f"Площадь равна : {a ** 2}")


part1_2()


def part1_3():
    a = float(input())
    b = float(input())
    print(f"Площадь равна : {a * b}\nПериметр равна : {(a + b) * 2}")


part1_3()


def part1_4():
    d = float(input())
    print(f"Длина равна : {3.14 * d}")


part1_4()


def part1_5():
    a = float(input())
    print(f"Объем куба равна : {a ** 3}\nПлощадь поверхности равна : {6 * a ** 2}")


part1_5()


def part1_6():
    a = float(input())
    b = float(input())
    c = float(input())
    print(f"Объем равна : {a * b * c}\nПлощадь поверхности равна : {(a * b + b * c + a * c) * 2}")


part1_6()


def part1_7():
    r = float(input())
    l = 2 * 3.14 * r
    s = 3.14 * r ** 2
    print(f"Окружность равна : {l}\nПлощадь круга равна : {s}")


part1_7()


def part1_8():
    a = float(input())
    b = float(input())
    print(f"Среднее арифметическое равна : {(a + b) / 2}")


part1_8()


def part1_9():
    a = float(input())
    b = float(input())
    print(f"Среднее геометрическое равна : {(a * b) * 1 / 2}")


part1_9()


def part1_10():
    a = float(input()) ** 2
    b = float(input()) ** 2
    print(
        f"Сумма квадратов равна : {a + b}\nРазность квадратов равна : {a - b}\nПроизведение квадратов равна : {a * b}\nЧастное их квадратов равна : {a / b}")


part1_10()
