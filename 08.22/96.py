def isInteger(text):
    num = 0
    if text[0] == '+' or text[0] == '-' or text[0] == int(text[0]):
        num += 1
        for number in range(1,len(text)+1):  
            if number == int(number):
                num += 1
    if num == len(text):
        return 'Является числом'
    else:
        return 'Неявляется числом'
        
text = input('Введите текст = ')

print(isInteger(text))
       