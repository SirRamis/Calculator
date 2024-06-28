def main():
    try:
        a, operator, b = input().split()
        print(type(a))
        if not (1 <= int(a) <= 10 and 1 <= int(b) <= 10):
            raise ValueError("Числа должны быть в диапазоне от 1 до 10 включительно")

        # if not len(q) == 2:
        #     raise ValueError("Неправильный формат ввода11")

        if operator == '+':
            result = int(a) + int(b)
        elif operator == '-':
            result = int(a) - int(b)
        elif operator == '*':
            result = int(a) * int(b)
        elif operator == '/':
            result = int(a) // int(b)
        else:
            raise ValueError("Неправильный оператор")

        return result

    except Exception as e:
        return "Ошибка: " + str(e)
result = main()
print(result)