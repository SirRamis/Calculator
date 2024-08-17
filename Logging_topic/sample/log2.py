import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w', encoding='utf-8',
                    format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_square(number):
    logging.info(f"Начало вычисления квадрата числа {number}")
    result = number ** 2
    logging.info(f"Результат: {result}")
    return result

# Примеры вызова функции
calculate_square(2)
calculate_square(4)
calculate_square(6)
