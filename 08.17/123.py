vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
punctuation = '?!,.'

y = ''
upper = 0

text = input().split()
for word in text:
    if word[-1] in punctuation:
        y = word[-1]
        word = word[:-1]

    if word[0] == word[0].upper():
        word = word.lower()
        upper += 1

    if word[0] in vowels:
        if upper == 1:
            print(word[0].upper() + word[1:] + 'way', end=' ')
        else:
            print(word + 'way', end=' ')

    if word[0] in consonants:
        for i in word:
            if i in vowels:
                x = word.find(i)
                break
        if upper == 1:
            print(word[x].upper() + word[x+1:] + word[:x] + 'ay' + y)
        else:
            print(word[x:] + word[:x] + 'ay' + y)