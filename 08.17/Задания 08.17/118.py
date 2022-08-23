text = input()
marks = '''!()-[]{};?@#$%:'"\,./^&;*_ '''
for i in text:
    if i in marks:
        text = text.replace(i,'').lower()
if text == text[::-1]:
    print('Словесные палиндромы')
else:
    print('Не явялются словесными палиндромами')