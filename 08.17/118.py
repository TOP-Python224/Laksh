punctuation = r'''!()-[]{};?@#$%:'"\,./^&;*_ '''

# ИСПОЛЬЗОВАТЬ: зачем вызывать метод lower() в цикле неизвестно сколько раз, когда можно сделать это единожды?
text = input().lower()
for i in text:
    if i in punctuation:
        text = text.replace(i, '')

# ИСПРАВИТЬ: вы не поняли, что такое словесный палиндром — здесь не нужно все символы строки читать с конца к началу — речь о том, чтобы разбить строку на слова, а уже потом посмотреть совпадают ли прямой и обратный порядок самих слов
if text == text[::-1]:
    print('Является словесным палиндромом')
else:
    print('Не является словесным палиндромом')

# ДОБАВИТЬ: при наличии в коде работы с вводом и выводом в конце файла каждой задачи должны быть в виде комментария добавлены ввод и вывод из стандартных потоков — запустите код и добавьте свои варианты вывода под комментариями stdin и stdout

# stdin:


# stdout:



# ИТОГ: неверная интерпретация условия — 0/2.4