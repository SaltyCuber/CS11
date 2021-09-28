def multiply(b, c):
    a = 0
    while c != 0:
        if c & 1 == 1:
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

def add(b, c, carryIn=0):
    a = 0
    for i in range((b.bit_length()+c.bit_length()) + 1):
        bitB = b & 1
        bitC = c & 1
        bitD = bitB ^ bitC
        carry = bitB & bitC
        bitA = carryIn ^ bitD
        carry = carry | (carryIn & bitD)
        carryIn = carry
        b = b >> 1
        c = c >> 1
        a = (a | (bitA << i))
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
