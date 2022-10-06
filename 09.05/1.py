from random import randrange


one_set = {randrange(1,10) for _ in range(10)}

two_set = {randrange(1,10) for _ in range(10)}

one_set_r = one_set - two_set
two_set_r =two_set - one_set

print(f'Первый список множества {one_set}\nВторой список множества {two_set}\nРезультат!\n{one_set_r}\n{two_set_r}')