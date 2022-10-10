from random import uniform, randint
from numbers import Real

r_lst, r_str, r_tpl,  = [], '', ()
result = {}

for _ in range(randint(1, 10)):
    r_str += str(uniform(0.0, 100.0)) + ' '

for _ in range(randint(1, 10)):
    r_lst.append(randint(10,1000))
    
for _ in range(randint(1, 10)):
    r_tpl += (uniform(0.0, 100.0),)


# ИСПРАВИТЬ: аннотацию типа параметра seq — согласно условию сюда может быть передан итерируемый объект или числовой объект
SeqType = list[Real] | tuple[Real, ...] | str
def average(*seq: SeqType) -> dict[str, float] | None:
    # ИСПРАВИТЬ: что именно делает функция с переданными ей данными?
    """Принимает на вход один аргумент: список, кортеж или строку, содержащий только целые или вещественные числа. Функция возвращает словарь"""
    arith, qua, harm, geo = 0, 0, 0, 1
    # ИСПРАВИТЬ: здесь и далее: seq — это всегда кортеж, в котором находятся ваши аргументы — а проверять вам нужно содержимое этого кортежа
    if not isinstance(seq, (list, tuple, str, float, int)):
        raise TypeError('сообщение об ошибке типа')
    
    try:
        # ИСПОЛЬЗОВАТЬ: при использовании функции type() используйте оператор is
        if type(seq) is str:
            tmp_seq = []
            for num in seq.rstrip().split(' '):
                tmp_seq.append(float(num))
            seq = tmp_seq
    except ValueError:
        return None

    for numbers in seq:
        if not isinstance(numbers, (int, float)):
            for number in numbers:
                arith += number
                geo *= number
                qua += number*number
                harm += 1/number
        else:
            arith += numbers
            geo *= numbers
            qua += numbers*numbers
            harm += 1/numbers

    seqlen = len(seq)
    result['arith'] = arith / seqlen
    result['geo'] = pow(geo, 1/seqlen)
    result['qua'] = pow(qua/seqlen, 1/2)
    result['harm'] = seqlen / harm

    sorted_result = sorted(result.items(), key=lambda i: i[1])
    sorted_result = dict(sorted_result)
    return sorted_result


print(*(num for num in r_lst), sep='  ')
print(average(r_lst), end='\n\n')

print(*(num for num in r_tpl), sep='  ')
print(average(r_tpl), end='\n\n')

# КОММЕНТАРИЙ: уже на этом тесте у вас ломается код
print(*(float(num) for num in r_str.split()), sep='  ')
print(average(r_str), end='\n\n')

# ДОБАВИТЬ: тесты с отдельными числами, а также с числами и итерируемыми объектами (см. условие задачи)


# 591  585  337  564
# {'harm': 491.2883652385054, 'geo': 506.30601621953065, 'arith': 519.25, 'qua': 529.8988110950995}

# 56.22045371075141  44.522689465033814  95.98993686257256  20.672812490420323
# {'harm': 40.388517623122645, 'geo': 47.20904901956773, 'arith': 54.35147313219453, 'qua': 60.79564632395012}

# -1, 1.5, -2, 2.5
# {'harm': -9.23076923076923, 'arith': 0.25, 'geo': 1.6548754598234365, 'qua': 1.8371173070873836}

# 48.00003306908048  79.90576362160346  5.712424467353461  34.43941900909597  17.457775718206705  51.61033581396756
# {'harm': 19.102281641210276, 'geo': 29.653110371740873, 'arith': 39.52095861655127, 'qua': 46.3250117924457}


# ИТОГ: необходимо перепроектировать сигнатуру функции и доработать код — 1/5
