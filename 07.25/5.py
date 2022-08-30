word = input()
d = {}
marks = '''!()-[]{};?@#$%:'"\,./^&amp;*_'''
for i in word:
    if i in marks:
        word = word.replace(i, '')
word =word.split()

for i in word:
    d[i.lower()] = d.get(i.lower(), 0) + 1
    
sorted_dict = {}
sorted_keys = sorted(d, key = d.get)

for i in sorted_keys:
    sorted_dict[i] = d[i]
    
for key,values in sorted_dict.items():
    if values == min(sorted_dict.values()):
        print(key)
        break



