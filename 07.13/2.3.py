num = 0

for i in range(100, 10000):
    if i > 99:
        x, y, z = i // 100, i // 10 % 10, i % 10
        if x != y or y != z or x != z: num += 1
    if i > 1000:
        x, y, z, e = i // 100 // 10, i // 100 % 10, i % 100 // 10, i  % 10
        if x != y and y != z and x != z and x != e and e != y and e != z: num += 1
print(num)