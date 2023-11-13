import timeit
from functools import lru_cache

def fib(n):
    if n <= 1:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


@lru_cache
def fib2(n):
    if n <= 1:
        return 0
    if n == 1:
        return 1
    return fib2(n - 1) + fib2(n - 2)


time_1 = timeit.timeit(lambda: fib(30), number=1)
print("Czas dla funkcji rekurencyjnej:", time_1, "sekundy")

time_2 = timeit.timeit(lambda: fib2(30), number=1)
print("Czas dla funkcji z pamięcią podręczną:", time_2, "sekundy")
