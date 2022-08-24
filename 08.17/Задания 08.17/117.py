text = input()
marks = '''!()-[]{};?@#$%:'"\,./^&;*_'''
for i in text:
    if i in marks:
        text = text.replace(i,'')
text = text.split()
print(text)