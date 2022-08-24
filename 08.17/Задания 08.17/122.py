text = input().split()
word1 = 'aeiou'
word2 = 'bcdfghjklmnpqrstvwxyz'
for word in text:
    if word[0] in word1:
        print(word + 'way', end = ' ')
    if word[0] in word2:
        for i in word:
            
            if i in word1:
                x = word.find(i)
                break
        print(word[x:] + word[:x] + 'ay')
        
        
    