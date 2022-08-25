punctuation = r'''!()-[]{};?@#$%:'"\,./^&;*_ '''

text = input()
for i in text:
    if i in punctuation:
        text = text.replace(i, '').lower()
if text == text[::-1]:
    print('Является словесным палиндромом')
else:
    print('Не является словесным палиндромом')