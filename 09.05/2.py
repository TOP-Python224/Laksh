text = input('Введите двоичное число > ')
set_binary = {'0','1'}
if text[:2].count('b') == 1:
    text = text.replace('b', '')

print('Yes') if set(text) == set_binary else print('No')








#stdin:
# 1010010101

# stdout:
# Yes

# stin:
# 01101b

# stdout:
# No