def ordinalDate2(day, year):
    year_is_leap = year % 400 == 0 or year % 4 == 0 and year % 100 != 0
    month_days = [31, 28+year_is_leap, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month = 1
    for i in month_days:
        if i < day:
            day = day - i
            month += 1
    return day, month, year
    
    
day, year = list(map(int, input('день, год: ').split()))
print(*ordinalDate2(day, year))

day_len = int(input('Введите количество дней до второй даты'))

year_is_leap = year % 400 == 0 or year % 4 == 0 and year % 100 != 0
if year_is_leap:
    if day_len + day < 366:
        print(*ordinalDate2(day+day_len, year))
    else:
        print(*ordinalDate2(day+day_len - 366, year + 1))


# stdin:
# 10 2020
# 285 

# stdout:
# 10 01 2020
# 21 10 2020
