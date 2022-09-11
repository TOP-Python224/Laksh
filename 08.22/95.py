def Capitalize(text):
    #изменяем первую букву, исключая пробелы
    pos = 0 
    while pos < len(text) and text[pos] == ' ':
        pos += 1
    if pos < len(text) : 
        text = text[0 : pos] + text[pos].upper() + text[pos + 1 : len(text)]

        
     # Изменяем  первую букву, которая следует за точкой и  восклицательным или вопросительным знаком
    pos = 0
    while pos < len(text):
        if text[pos] == "." or text[pos] == "!" or text[pos] == "?" :
            pos = pos + 1
 
            while pos < len(text) and text[pos] == " ":
                pos = pos + 1

 
            if pos < len(text):
                text = text[0 : pos] + text[pos].upper() + text[pos + 1 : len(text)]
        
        pos = pos + 1
 
    pos = 1
    while pos < len(text) - 1:
        if text[pos - 1] == " " and text[pos] == "i" and (text[pos + 1] == " " or text[pos + 1] == "." or text[pos + 1] == "!" or text[pos + 1] == "?" or text[pos + 1] == "’"):
            text = text[0 : pos] + "I" + text[pos + 1 : len(text)]
        pos = pos + 1
    return text


text = input('Введите текст = ')

print(Capitalize(text))

# stdin:
# what time do i have to be there? what’s the address? this time i’ll try to be on time!

# stdout:
# What time do I have to be there? What’s the address? This time I’ll try to be on time!