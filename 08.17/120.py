word = input().split()
print(*word[:-1], sep=", ", end=' и ')
print(word[-1])

# ИСПРАВИТЬ: это был бы очень хороший код, если бы не одна такая маленькая проблемка, возникающая при вводе одного слова (см. stdout)

# stdin:
# аб

# stdout:
#  и аб

# ДОБАВИТЬ: при наличии в коде работы с вводом и выводом в конце файла каждой задачи должны быть в виде комментария добавлены ввод и вывод из стандартных потоков — запустите код и добавьте свои варианты вывода под комментариями stdin 2 и stdout 2

# stdin 2:


# stdout 2:



# ИТОГ: логические ошибки в коде — 1.2/2.4