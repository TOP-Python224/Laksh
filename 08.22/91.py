
# ДОБАВИТЬ: аннотации типов для параметров и возвращаемого значения функции
# ДОБАВИТЬ: строку документации для функции — начинается с глагола и отвечает на вопрос "что делает?"


def ordinalDate( day: int, month: int, year: int ) -> int:
    
    """Возвращает порядковый номер заданного дня в указанном году."""
    year_is_leap  = year % 400 == 0 or year % 4 == 0 and year % 100 != 0
    month_days = [31,28+year_is_leap,31, 30,31,30, 31,31,30, 31,30,31]

    md = 0
    for i in range(month-1):
        md += month_days[i]
    return md + day



# ИСПОЛЬЗОВАТЬ: для распаковки map объекта в несколько переменных нет необходимости сначала преобразовывать в список
day, month, year = map(int, input('день, месяц, год: ').split())
print(f'Порядковый номер: {ordinalDate(day, month, year)}\n')

day, month, year = list( map( int, input( 'день, месяц, год: ' ).split() ) )
print( f'Порядковый номер: { ordinalDate(day,month,year) }\n' )



# stdin:
# 10 10 2020

# stdout:

# 284


# ИТОГ: хорошо — 4/4

# 284

