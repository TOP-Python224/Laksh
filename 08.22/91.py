def ordinalDate(day, month, year):
    year_is_leap = year % 400 == 0 or year % 4 == 0 and year % 100 != 0
    month_days = [31, 28+year_is_leap, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    md = 0
    for i in range(month-1):
        md += month_days[i]
    return md + day

day, month, year = list(map(int, input('день, месяц, год: ').split()))
print(f'Порядковый номер: { ordinalDate(day,month,year) }\n')


# stdin:
# 10 10 2020

# stdout:
# 284
