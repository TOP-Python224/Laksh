n = input()
sum = 0
for i in n:
    if i != " ":
        sum += 80

print(f'{sum//100} руб . {sum%1000} коп.')
