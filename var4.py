"""
Используя модуль concurrent.futures,
распараллельте на процессы процедуру вычисления гипотенузы прямоугольного треугольника.
Написанное приложение должно быть консольным. Аргументы командной строки – численные значения катетов.
"""

import concurrent.futures
import math


def calculate_hypotenuse(_a: float, _b: float) -> float:
    return math.sqrt(_a * _a + _b * _b)


if __name__ == '__main__':
    a = float(input(float))
    b = float(input(float))
    with concurrent.futures.ProcessPoolExecutor() as executor:
        result = executor.submit(calculate_hypotenuse, a, b)
        print(result.result())
