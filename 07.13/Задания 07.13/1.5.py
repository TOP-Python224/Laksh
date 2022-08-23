n =  int(input())
sum = []
while n % 7 == 0:
    sum.append(n)
    n = int(input())
print(n)
print(*sum, n)
    
    