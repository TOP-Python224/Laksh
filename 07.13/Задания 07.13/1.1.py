
name = [("К",2,6), ("У",5,1), ("З",3,3), ("Ь",1,1), ("М",4,7), ("А",7,1)]

for i in name:
    text,amount,le = i
    for j in range(le):
        for k in range(amount):
            print(text, end = "")
        print()
            