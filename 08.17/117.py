punctuation = r'''!()-[]{};?@#$%:'"\,./^&;*_'''

text = input()
for i in text:
    if i in punctuation:
        text = text.replace(i, '')
text = text.split()
print(text)