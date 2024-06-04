import re

def calculator():
    try:
        expression = input()
        #match = re.match(r"^\s*(\d+)\s*([\+\-\*/])\s*(\d+)\s*$", expression)
        match = re.match(r"^(\d+)([\+\-\*/])(\d+)$", expression)
        if not match:
            if re.search(r"[\+\-\*/]", expression):
                result = "throws Exception: т.к. формат математической операции не удовлетворяет заданию - два операнда и один оператор (+, -, /, *)"
            else:
                result = "throws Exception: т.к. строка не является математической операцией"
            print(result)
            return result

        a, operator, b = match.groups()
        a, b = int(a), int(b)

        if not (1 <= a <= 10 and 1 <= b <= 10):
            result = "throws Exception: Числа должны быть от 1 до 10 включительно"
            print(result)
            return result

        if operator == '+':
            result = a + b
        elif operator == '-':
            result = a - b
        elif operator == '*':
            result = a * b
        elif operator == '/':
            if b == 0:
                result = "throws Exception: Деление на ноль невозможно"
                print(result)
                return result
            result = a // b
        else:
            result = "throws Exception: Неподдерживаемая операция"
            print(result)
            return result

        print(result)
        return result

    except Exception as e:
        result = f"throws Exception: {e}"
        print(result)
        return result

