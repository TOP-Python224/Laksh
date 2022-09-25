from typing import Callable
from math import *

def fvp( fun: Callable,
               *args: int| float,
               key: bool = True) -> str| float:
               """ принимает математическую функцию ввиде lambda и выводит результат  """
               result = fun(*args)
               
               return f'{result:.2f}' if key else float(f'{result:.2f}')





print(fvp(
    lambda a, b, c, x: a * x**2 + b * x + c,
    10, 11, 12, 13
))

print(fvp(
    lambda a, b, c: sqrt((a + b + c)**2),
    1, 2, 3,
    key=False
))


print(fvp(
    lambda k, x, b: k * x + b,
    11, 12, 13
))
