mydict = dict()
leng = int(input('Введите длину словаря '))
while len(mydict) != leng:
    key = input('Введите ключ ')
    values = input('Введите значение ')
    mydict[key] = values
meaning = input('Введите искомое значение ')
print(*[ i for i in mydict if  mydict[i] == meaning])