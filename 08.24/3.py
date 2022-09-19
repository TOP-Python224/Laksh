from numbers import Real
from random import sample
# параметры строго ключевые, потому что более лучше становится понять код
def remove_numbers(lst: list[Real],
                                   *,
                                   a:  int,
                                   boolean: bool) -> list | None:
                                   """Редактирует переданный список (True) и возвращает None, либо возвращает отредактированную копию списка (False) """
                                   
                                   if boolean:
                                       for i in range(a):
                                           lst.remove(min(lst))
                                           lst.remove(max(lst))
                                       return None
                                       
                                   else:
                                       new_lst = lst.copy()
                                       for i in range(a):
                                           new_lst.remove(min(new_lst))
                                           new_lst.remove(max(new_lst))
                                       return new_lst
                                   
# stdin:
# print(remove_numbers(
    # sample(range(-120, 222), 15),
    # a = 3,
    # boolean=True
# ))
# stdout:
#None



# stdin:
# print(remove_numbers(
    # sample(range(-125, 1001), 14),
    # a = 4,
    # boolean=False
# ))


#stdout:
#[386, 286, 249, 509, 274, 240]
