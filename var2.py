"""
Используя модуль concurrent.futures,
распараллельте на процессы процедуру вычисления квадратного корня уравнения.
Написанное приложение должно быть консольным.
Аргументы командной строки – коэффициенты квадратного уравнения ax^2+bx+c=0.
"""
import concurrent.futures
import math


def calculate_i_number(i: float, koef: float) -> float:
    # print((i-koef)*(i-koef))
    return (i-koef)*(i-koef)


if __name__ == '__main__':
    a = float(input(float))
    b = float(input(float))
    c = float(input(float))
    koef = (a+b+c)/3.0
    result = 0.0
    items = [(a, koef), (b, koef), (c, koef)]
    with concurrent.futures.ProcessPoolExecutor() as p:
        result_sum = p.starmap(calculate_i_number, items)
    for i in result_sum:
        result += i
    print(math.sqrt(result/2))
