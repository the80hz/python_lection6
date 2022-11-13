"""
Распараллельте на процессы процедуру вычисления приближения числа π по распределению
π(N)=4/N ∑_(i=1)^N 1/(1+((i-0.5)/N)^2 ).
Написанное приложение должно быть консольным. Аргумент командной строки – число N.
"""
import math
import threading
import time
from datetime import datetime



def proc(_i: int, _N: int):
    _th_name = threading.current_thread().name
    print(f'{_th_name}: обработка данных => i = {_i}')
    result = 1 / (1 + math.pow((_i - 0.5) / _N, 2))
    time.sleep(1)
    print(f'{_th_name}: обработка закончена - {_i} => {result}')
    return result


if __name__ == "__main__":
    N = int(input("Введите (N): "))
    start_time = datetime.now()
    res = 4 / N
    tmp = list()
    th_name = threading.current_thread().name
    print(f'{th_name}: запущен...' + "\n" + "<-- Σ от i до N -->")
    for i in range(1, N):
        tmp.append(proc(i, N))
    res *= sum(tmp)
    print(f'Результат: ( 4/{N} ) * Σ{sum(tmp)} ≈ {round(res, 5)}')
    print(datetime.now() - start_time)
