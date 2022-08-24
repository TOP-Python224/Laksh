text = "abcdefgh"
number = [1, 2, 3, 4, 5, 6, 7, 8]

x1,x2,y1,y2= text.index(input()) +1, int(input()), text.index(input()) + 1, int(input())

if -1 <=y1 - x1<= 1 and -1 <= y2 - y1 <= 1:
    print ('ДА')
else:
    print ('НЕТ')