from typing import *
from time import * 

def time_decorator(func: Callable) -> Callable:
    """Выводит время использования функции """
    def time(*args, **kwargs):
        time_d = perf_counter()
        result = func()
        time_p = perf_counter()
        total_time = time_p - time_d / 10**9
        print(f"Время выполнения функции {total_time:.3f} секунд.\n")
        return result
    return time
 
@time_decorator
def say_whee():
    print('Ура')
 
 
say_whee()
    
    
# stdout:
# Ура
# Время выполнения функции 12546.409 секунд.
