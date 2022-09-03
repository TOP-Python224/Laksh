n = int(input())

fib, fib1, fib2 = 0, 1, 1

for i in range(n):
    if i < 2:
        fib, fib1, fib2 = 1, 1, 1
    if i >= 2:
        fib = fib1 + fib2
        fib1 = fib2
        fib2 = fib
    print(fib, end = " ")

        