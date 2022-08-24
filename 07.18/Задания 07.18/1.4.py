number = input()
number1 = sum(list(map(int,list(number[:3]))))
number2 = sum(list(map(int,list(number[3:]))))
if number1 == number2: print('ДА')
else: print('НЕТ')

