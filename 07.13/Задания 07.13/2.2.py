
sum = 0
ch = 1234
# число например 125
ch1 = ch % 10 #  (4) 
ch2 = ch % 100 // 10 #  (3)
ch3 = ch // 100 % 10 #  (2)
ch4 = ch // 100 // 10 # (1)
print(ch1,ch2,ch3,ch4, sep = ('\n'))
for i in range(100, 1000):
    if (i % 10) == (i % 100 //10) or ( i % 10) == ( i // 100) or ( i % 100 // 10) == ( i // 100):
        sum += 1
print(sum)

    