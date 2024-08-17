def part3_1():
    a = int(input())
    print(f"Является положительным {a > 0}")


part3_1()

def part3_2():
    a = int(input())
    print(f"Является нечетным : {a % 2 != 0}")


part3_2()

def part3_3():
    a = int(input())
    print(f"Является четным : {a % 2 == 0}")


part3_3()

def part3_4():
    a = int(input())
    b = int(input())
    print(f"Справедливы неравенства A > 2 и B ≤ 3 : {a > 2 and b <= 3}")


part3_4()

def part3_5():
    a = int(input())
    b = int(input())
    print(f"Справедливы неравенства A > 2 и B ≤ 3 : {a > 2 and b <= 3}")


part3_5()

def part3_6():
    a = int(input())
    b = int(input())
    c = int(input())
    print(f"Справедливо двойное неравенство A < B < C : {a < b < c}")


part3_6()

def part3_7():
    a = int(input())
    b = int(input())
    c = int(input())
    print(f"Число B находится между числами A и C : {a < b < c or a > b > c}")


part3_7()

def part3_8():
    a = int(input())
    b = int(input())
    print(f"Каждое из чисел A и B нечетное : {a % 2 != 0 and b % 2 != 0}")


part3_8()

def part3_9():
    a = int(input())
    b = int(input())
    print(f"Хотя бы одно из чисел A и B нечетное : {a % 2 != 0 or b % 2 != 0}")


part3_9()

def part3_10():
    a = int(input())
    b = int(input())
    c = a % 2 != 0
    d = b % 2 != 0
    print(f"Ровно одно из чисел A и B нечетное : {c != d}")


part3_10()
