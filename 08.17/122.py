vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'

text = input().split()
for word in text:
    if word[0] in vowels:
        print(word + 'way', end=' ')
    if word[0] in consonants:
        for i in word:
            if i in vowels:
                x = word.find(i)
                break
        print(word[x:] + word[:x] + 'ay')
