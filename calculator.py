import re

def calculator():
    try:
        expression = input()
        match = re.match(r"^(\d+)([\+\-\*/])(\d+)$", expression)
        if not match:
            if re.search(r"[\+\-\*/]", expression):
                return ValueError("т.к. формат математической операции не удовлетворяет заданию - два операнда и один оператор (+, -, /, *)")
            else:
                return ValueError("т.к. строка не является математической операцией")

        a, operator, b = match.groups()
        a, b = int(a), int(b)
        if not (1 <= a <= 10 and 1 <= b <= 10):
            return ValueError("Числа должны быть от 1 до 10 включительно")
        if operator == '+':
            result = a + b
        elif operator == '-':
            result = a - b
        elif operator == '*':
            result = a * b
        elif operator == '/':
            if b == 0:
                return ValueError("Деление на ноль невозможно")
            result = a // b
        else:
            return ValueError("Неподдерживаемая операция")
        return result

    except Exception as e:
        return f"throws Exception: {e}"

