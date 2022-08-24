text = input().split(' ')

dict1 = {}
text1 = []
for word in text:
    if word in dict1:
        word1 = word[:word.index('.')] + '_' + str(dict1[word]) + word[word.index('.'):]
        text1.append(word1)
        dict1[word] = dict1.get(word, 1) + 1
        
    else:
        dict1[word] = dict1.get(word, 1) + 1
        text1.append(word)
        
print(text1)


