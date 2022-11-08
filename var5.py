"""
Используя пакет multiprocessing,
распараллельте на процессы процедуру вычисления выборочной дисперсии трех чисел.
Написанное приложение должно быть консольным. Аргументы командной строки – три числа.
"""


import multiprocessing


def calculate_i_number(i: float, koef: float) -> float:
    # print((i-koef)*(i-koef))
    return (i-koef)*(i-koef)


if __name__ == '__main__':
    x = float(input(float))
    y = float(input(float))
    z = float(input(float))
    koef = (x+y+z)/3.0
    result = 0.0
    items = [(x, koef), (y, koef), (z, koef)]
    with multiprocessing.Pool(3)as p:
        result_sum = p.starmap(calculate_i_number, items)
    for i in result_sum:
        result += i
    print(result/2)
