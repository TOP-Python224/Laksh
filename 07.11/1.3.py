one, two = int(input()), int(input())

if one % two == 0:
    print( f"Частное:{one // two}")
else:
    print( f"Частное:{one // two}",f"Остаток:{one % two}", sep = '\n')