from random import uniform, randint
from typing import SupportsFloat

r_lst, r_str, r_tpl,  = [], '', ()
result = {}

for _ in range(randint(1, 10)):
    r_str += str(uniform(0.0, 100.0)) + ' '
    
for _ in range(randint(1, 10)):
    r_lst.append(randint(10,1000))
    
for _ in range(randint(1, 10)):
    r_tpl += (uniform(0.0, 100.0),)


NumType = r_lst or r_str or r_str
def average(seq: NumType) -> dict[float] | None:
    """Функция принимает на вход один аргумент: список, кортеж или строку, содержащий только целые или вещественные числа. Функция возвращает словарь"""
    arith, qua, harm = 0, 0, 0
    geo = 1

    if not isinstance(seq, (list, tuple, str)):
        raise TypeError('сообщение об ошибке типа')

    try:
        if type(seq) == str:
            tmp_seq = []
            for num in seq.rstrip().split(' '):
                tmp_seq.append(float(num))
            seq = tmp_seq
    except ValueError:
        return None

    seqlen = len(seq)
    for number in seq:
        if not isinstance(number, (int, float)):
            raise TypeError('сообщение об ошибке типа')
        else:
            arith += number
            geo *= number
            qua += number*number
            harm += 1/number
    result['arith'] = arith / seqlen
    result['geo'] = pow(geo, 1/seqlen)
    result['qua'] = pow(qua/seqlen, 1/2)
    result['harm'] = seqlen / harm

    sorted_result = sorted(result.items(), key=lambda i: i[1])
    sorted_result = dict(sorted_result)
    return sorted_result


print(*(num for num in r_lst), sep='  ', end='\n\n')
print(average(r_lst), end='\n\n')

print(*(num for num in r_tpl), sep='  ',  end='\n\n')
print(average(r_tpl), end='\n\n')

print(*(float(num) for num in r_str.split()), sep='  ',  end='\n\n')
print(average(r_str), end='\n\n')


# stdout:
# 591  585  337  564

# {'harm': 491.2883652385054, 'geo': 506.30601621953065, 'arith': 519.25, 'qua': 529.8988110950995}

# 56.22045371075141  44.522689465033814  95.98993686257256  20.672812490420323

# {'harm': 40.388517623122645, 'geo': 47.20904901956773, 'arith': 54.35147313219453, 'qua': 60.79564632395012}

# 48.00003306908048  79.90576362160346  5.712424467353461  34.43941900909597  17.457775718206705  51.61033581396756

# {'harm': 19.102281641210276, 'geo': 29.653110371740873, 'arith': 39.52095861655127, 'qua': 46.3250117924457}
