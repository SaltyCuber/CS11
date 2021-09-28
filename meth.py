def multiply(b, c):
    a = 0
    while c != 0:
        if modulo(c, 2) == 1:
            a = add(a, b)
        b = b << 1
        c = c >> 1
    return a

def divide(b, c):
    a = 0
    while b >= c:
        b = subtract(b, c)
        a = add(a, 1)
    return a

def modulo(b, c):
    while b >= c:
        b = subtract(b, c)
    return b

def add(b, c):
    a = nor(nor(b, c), nor(nor(b, b), nor(c, c)))
    d = (nor(nor(b, b), nor(c, c))) << 1
    while d != 0:
      temp = (nor(nor(b, b), nor(c, c))) << 1  
      a = nor(nor(a, d), nor(nor(a, a), nor(d, d)))
      d = temp
    return a

def subtract(b, c):
    a = add(add(b, nor(c, c)), 1)
    return a

def nor(b, c):
    a = ~(b | c)
    return a



def div(b, c):
    # this is gonna be shift and subtract division because repeated subtraction is slow lol
    a = 0
