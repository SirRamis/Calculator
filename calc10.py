def calc(express):
    if len(express) < 3:
        raise ValueError("throws Exception//Не является математической операцией")
    operators = ['-', '+', '*', '/']
    operator = None
    for op in operators:
        if op in express:
            operator = op
            break
    if operator is None:
        raise ValueError("throws Exception//Недопустимая операция")

    try:
        a, b = map(int, express.split(operator))
    except ValueError:
        raise ValueError("throws Exception//Неподходящие числа")

    if not (1 <= a <= 10 and 1 <= b <= 10):
        raise ValueError("throws Exception//Числа должны быть от 1 до 10")

    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    elif operator == '/':
        result = a // b
    return result
def main(input_str):
    try:
        result = calc(input_str)
        return str(result)
    except ValueError as e:
        return str(e)


if __name__ == "__main__":
    express = input("Введите пример: ")
    print(main(express))