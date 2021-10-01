def fib(n):
    i = 0
    a = 0
    b = 1
    while True:
        if i == n:
            out = b
            break
        else:
            a = a + b
            i += 1
        if i == n:
            out = a
            break
        else:
            b = a + b
            i += 1
    return out

x = int(input("How many generations back?\n"))
print("The number of bees in generation {} is {}.".format(x, fib(x)))