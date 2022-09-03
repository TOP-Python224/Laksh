# ИСПОЛЬЗОВАТЬ: в стандартной библиотеке есть модуль с несколькими строковыми константами, например со знаками препинания
puncts = r'''?!,.:" '''
vowels = 'aeiouAEIOU'
consonants = 'bcdfghjklmnpqrstvwxyz'


text = input().split()

for word in text:
    
    word_left = ''
    word_right = ''
    word_t = ''
    word_left = word[:len(word) - len(word.lstrip(puncts))]
    word_right = word[len(word.rstrip(puncts)):]
    word_t = word.strip(puncts)
    word_t1 = word.strip(puncts)
    
    if word_t[0] in vowels:
         word_t = word_t + 'way'
    else:
        for char in word_t:
            if char in vowels:
                i = word_t.find(char)
                break
        word_t = word_t[i:] + word_t[:i] + 'ay'
    if word_t1.istitle():
        word_t = word_t.title()
    print(word_left + word_t + word_right, end = ' ')
    
    



# stdin:
# He said: "Will you help me?"

# stdout:
# Ehay aidsay: "Illway ouyay elphay emay?"

# ДОБАВИТЬ: при наличии в коде работы с вводом и выводом в конце файла каждой задачи должны быть в виде комментария добавлены ввод и вывод из стандартных потоков — запустите код и добавьте свои варианты вывода под комментариями stdin и stdout

# stdin 2:
# Vova, why are you doing this?!

# stdout 2:
#Ovavay, hyway areway ouyay oingday isthay?!


# ИТОГ: многочисленные логические ошибки — 0.8/2.4
