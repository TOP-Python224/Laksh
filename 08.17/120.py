word = input().split()
print(*word[:-1], sep=", ", end=' и ')
print(word[-1])
