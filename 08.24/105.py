digits = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
digits_inv = {k: v for v, k in digits.items()}


def from_decimal(num: int,
                 *,
                 base: int = 16) -> str:
    """Преобразует десятичное число в 16-ную систему исчисления """
    quotient = num // base
    remainder = num % base
    num = digits.get(remainder, remainder)

    while quotient > 0:
        remainder = quotient % base
        quotient = quotient // base
        num = digits.get(remainder, str(remainder)) + str(num)
    return num


def to_decimal(num: str,
               *,
               base: int = 16) -> int:
    """Преобразует обратно в десятичную систему исчисления """
    num_reversed = str(num)[::-1]
    # КОММЕНТАРИЙ: sum — это имя встроенной функции, использовав его для своей переменной, вы лишились возможности использовать встроенную функцию
    result = 0
    for i in range(len(num_reversed)):
        if num_reversed[i].title() in digits_inv:
            if 0 <= digits_inv[num_reversed[i].title()] <= base:
                result += digits_inv[num_reversed[i].title()] * base**i
            else:
                raise ValueError('Число не принадлежит системе счисления')
        elif num_reversed[i].isdecimal():
            if 0 <= int(num_reversed[i]) <= 16:
                result += int(num_reversed[i]) * base**i
            else:
                raise ValueError('Число не принадлежит системе счисления')
        else:
            raise ValueError('Символ не принадлежит системе счисления')
    return result


def result_invent(num: int,
                  base_from: int,
                  base_to: int) -> int | str:
    return from_decimal(
        to_decimal(num=num, base=base_from),
        base=base_to
    )


number = input('Введите число в исходной системе счисления: ')
base_source = int(input('Введите исходную систему счисления (2-16): '))
base_destination = int(input('Введите целевую систему счисления (2-16): '))

if 2 <= base_source <= 16 and 2 <= base_destination <= 16:
    print(result_invent(number, base_source, base_destination))
else:
    raise ValueError('Неправильная система счисления!')


# stdin:
# Введите число в исходной системе счисления: 5a698d
# Введите исходную систему счисления (2-16): 2
# Введите целевую систему счисления (2-16): 16
# ValueError: Число не принадлежит системе исчисления

# Введите число в исходной системе счисления: 1a45a
# Введите исходную систему счисления (2-16): 14
# Введите целевую систему счисления (2-16): 15
# 14B80
