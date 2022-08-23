number = input()

sum = 0
sum1 = 1

for i in number:
    sum += int(i)
    sum1 *= int(i)
    
print( "Сумма цифр = ", sum)
print( "Произведение цифр = ", sum1)
    
