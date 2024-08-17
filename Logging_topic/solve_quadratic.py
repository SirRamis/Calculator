import logging

logging.basicConfig(level=logging.INFO, filename='solve_quadratic.log', filemode='w', encoding='utf-8',
                    format='%(asctime)s - %(levelname)s - %(message)s')

a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))


def solve_quadratic():
    try:
        discriminant = b ** 2 - 4 * a * c
        logging.info(f"Попытка решения уравнения {a}x^2 + {b}x + {c} = 0")
        print(f"Дискриминант: {discriminant}")

        if discriminant < 0:
            logging.info("Ошибка: Дискриминант отрицательный, действительных корней нет.")
            raise ValueError("Дискриминант отрицательный, действительных корней нет.")

        else:
            x1 = (-b + discriminant ** 0.5) / (2 * a)
            x2 = (-b - discriminant ** 0.5) / (2 * a)

            print(f"Корни уравнения: {x1}, {x2}")
            logging.info(f"Корни уравнения: {x1}, {x2}")

    except ValueError as e:
        print(f"Ошибка: {e}. Пожалуйста, попробуйте снова.")


solve_quadratic()
