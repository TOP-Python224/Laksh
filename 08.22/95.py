# ИСПРАВИТЬ: имена функциям и методам мы даём в змеином_нижнем_регистре
# ДОБАВИТЬ: аннотации типов для параметров и возвращаемого значения функции
# ДОБАВИТЬ: строку документации для функции — начинается с глагола и отвечает на вопрос "что делает?"
def Capitalize(text):
    # изменяем первую букву, исключая пробелы
    pos = 0
    # ОТВЕТИТЬ: так вы находите не букву, а первый символ не являющийся пробелом — это может быть перевод строки, цифра или знак препинания — имеет ли смысл какой либо из таких символов переводить в верхний регистр?
    while pos < len(text) and text[pos] == ' ':
        pos += 1
    if pos < len(text):
        text = text[0:pos] + text[pos].upper() + text[pos+1 : len(text)]

    # изменяем первую букву, которая следует за точкой и восклицательным или вопросительным знаком
    pos = 0
    while pos < len(text):
        if text[pos] == "." or text[pos] == "!" or text[pos] == "?":
            pos = pos + 1
            while pos < len(text) and text[pos] == " ":
                pos = pos + 1
            if pos < len(text):
                text = text[0:pos] + text[pos].upper() + text[pos+1 : len(text)]
        pos = pos + 1
 
    pos = 1
    while pos < len(text) - 1:
        # ИСПРАВИТЬ: эти два условия можно заменить на одну проверку среза
        if (text[pos-1] == " "
            and text[pos] == "i"
            # ИСПРАВИТЬ: все эти условия прекрасно заменяются одним оператором in
            and (text[pos+1] == " "
                 or text[pos+1] == "."
                 or text[pos+1] == "!"
                 or text[pos+1] == "?"
                 # ИСПОЛЬЗОВАТЬ: это не все возможные символы после i (см. тесты) — рекомендую строковую константу punctuation в модуле стандартной библиотеки string (там, впрочем, тоже не все)
                 or text[pos+1] == "’")):
            text = text[0:pos] + "I" + text[pos+1 : len(text)]
        pos = pos + 1
    return text


text = input('Введите текст = ')
print(Capitalize(text))


# stdin:
# what time do i have to be there? what’s the address? this time i’ll try to be on time!

# stdout:
# What time do I have to be there? What’s the address? This time I’ll try to be on time!


# СДЕЛАТЬ: тесты, ещё раз тесты, и снова тесты — с разными входными данными — и вы увидите много удивительного
# Введите текст = он сказал: "i'll be back". и ушёл
# Он сказал: "i'll be back". И ушёл

# Введите текст = what i'm going to do?
# What i'm going to do?


# СДЕЛАТЬ: хорошо, с посимвольным перебором вы более-менее справились — а теперь открывайте документацию/литературу и читайте о строковых методах


# ИТОГ: неплохо — 4/6
