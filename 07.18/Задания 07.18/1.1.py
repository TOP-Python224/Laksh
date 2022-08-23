n = input()

if "@" in n:
    if "." in n[n.find('@'):]:
        print("Верно")
    else:
        print("Неверно")
else:
    print("Неверно")