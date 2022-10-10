from numbers import Real
from random import sample


# параметры строго ключевые, потому что более лучше становится понять код
def remove_numbers(numbers: list[Real],
                   *,
                   n: int,
                   modify_list: bool) -> list | None:
    """Редактирует переданный список (True) и возвращает None, либо возвращает отредактированную копию списка (False) """
    if modify_list:
        for i in range(n):
            numbers.remove(min(numbers))
            numbers.remove(max(numbers))
        return None
    else:
        new_lst = numbers.copy()
        for i in range(n):
            new_lst.remove(min(new_lst))
            new_lst.remove(max(new_lst))
        return new_lst


# stdin:
print(remove_numbers(
    sample(range(-120, 222), 15),
    n=3,
    modify_list=True
))
# stdout:
# None

# stdin:
print(remove_numbers(
    sample(range(-125, 1001), 14),
    n=4,
    modify_list=False
))
# stdout:
# [386, 286, 249, 509, 274, 240]
