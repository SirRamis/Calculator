def calculator():
    try:
        input_string = input().strip()
        operators = ['+', '-', '*', '/']
        operator_found = False

        for operator in operators:
            if operator in input_string:
                operator_found = True
                break

        if not operator_found:
            raise ValueError("Неправильный формат ввода")

        parts = input_string.split(operator)

        if len(parts) != 2:
            raise ValueError("Неправильный формат ввода")

        a = parts[0].strip()
        b = parts[1].strip()

        a = int(a)
        b = int(b)

        if not (1 <= a <= 10 and 1 <= b <= 10):
            raise ValueError("Числа должны быть в диапазоне от 1 до 10 включительно")

        if operator == '+':
            result = a + b
        elif operator == '-':
            result = a - b
        elif operator == '*':
            result = a * b
        elif operator == '/':
            result = a // b
        else:
            raise ValueError("Неправильный оператор")

        return result

    except Exception as e:
        return "Ошибка: " + str(e)


result = calculator()
print(result)
