"""
Используя модуль concurrent.futures,
распараллельте на процессы процедуру вычисления квадратного корня уравнения.
Написанное приложение должно быть консольным.
Аргументы командной строки – коэффициенты квадратного уравнения ax^2+bx+c=0.
"""
import concurrent.futures
import math
from typing import Tuple


def calculate_quadratic_equation(_a: float, _b: float, _c: float) -> int | float | tuple[float, float]:
    d = _b * _b - 4 * _a * _c
    if d < 0:
        return 0
    elif d == 0:
        return -_b / (2 * _a)
    else:
        return (-_b + math.sqrt(d)) / (2 * _a), (-_b - math.sqrt(d)) / (2 * _a)


if __name__ == '__main__':
    a = float(input(float))
    b = float(input(float))
    c = float(input(float))
    with concurrent.futures.ProcessPoolExecutor() as executor:
        result = executor.submit(calculate_quadratic_equation, a, b, c)
        print(result.result())
