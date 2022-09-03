vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'

# ИСПОЛЬЗОВАТЬ: обязательно приводите сравниваемые строки к одному регистру, иначе рискуете потерять данные (см. stdout)
# В задаче написанно что все слова будут вводится в нижнем регистре и разделены пробелами) поэтому метод lower не использовал
text = input().lower().split()
for word in text:
    if word[0] in vowels:
        print(word + 'way', end=' ')
    # ОТВЕТИТЬ: зачем две независимые проверки?
    else:
        # КОММЕНТАРИЙ: здесь вы перебираете символы в строке — именуйте переменные соответственно
        for char in word:
            if char in vowels:
                # КОММЕНТАРИЙ: а здесь вы получаете индекс символа — именуйте переменные соответственно
                i = word.find(char)
                break
        print(word[i:] + word[:i] + 'ay', end=' ')



# stdin:
# What do you think about this new language

# stdout:
# oday ouyay inkthay aboutway isthay ewnay anguagelay

# ДОБАВИТЬ: при наличии в коде работы с вводом и выводом в конце файла каждой задачи должны быть в виде комментария добавлены ввод и вывод из стандартных потоков — запустите код и добавьте свои варианты вывода под комментариями stdin и stdout

# stdin 2:
# it is a hard language
# stdout 2:
# itway isway away ardhay anguagelay

# ИТОГ: верно, с небольшими упущениями — 1.8/2.4
