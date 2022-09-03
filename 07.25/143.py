word1, word2 = input(), input()
word1 = list(word1)
word2 = list(word2)
sum = 0
word1.sort()
word2.sort()
for i in range(len(word1)):
    if word1[i] == word2[i]:
        sum += 1
    else:
        print('NO')
if sum == len(word1):
    print('YES')
    
