word = input()
sum = 0
number = { 
1 : ['A','E','I','L','N','O','R','S','T','U'],
2 : ['D','G'],
3 : ['B', 'C', 'M', 'P'],
4 : ['F', 'H', 'V', 'W', 'Y'],
5 : ['K'],
8 : ['J', 'X'],
10 : ['Q', 'Z']
}
for i in word:
    for key,value in number.items():
        if i.upper() in value:
            sum += key
print(sum)