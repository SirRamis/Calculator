def calculator(example):
    try:
        operators = ['+', '-', '*', '/']
        operator_found = False

        for operator in operators:
            if operator in example:
                operator_found = True
                break

        if not operator_found:
            raise ValueError("throws Exception //т.к. строка не является математической операцией")

        parts = example.split(operator)

        if len(parts) != 2:
            raise ValueError("throws Exception //т.к. формат математической операции не удовлетворяет заданию - два операнда и один оператор (+, -, /, *)")

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


def main(input_str):
    try:
        result = calculator(input_str)
        return str(result)
    except ValueError as e:
        return str(e)


if __name__ == "__main__":
    example = input("Введите пример: ")
    print(main(example))
