text = "abcdefgh"
number = [1, 2, 3, 4, 5, 6, 7, 8]

x1,x2,y1,y2= text.index(input()) +1, int(input()), text.index(input()) + 1, int(input())

if (x1 + x2 + y1 + y2) % 2 == 0:
    print("ДА")
else:
    print("НЕТ")