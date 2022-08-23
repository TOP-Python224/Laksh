a = 0
z = 999999
cnt = 0
for i in range(a, z+1):
    i_str = str(i)
    while len(i_str) < 6:
        i_str = '0' + i_str
    i = list(i_str)
    f = i[0:3]
    s = i[3:]
    if sum(map(int, f)) == sum(map(int, s)):
        cnt += 1
print(cnt)