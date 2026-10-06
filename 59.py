def numero(a,b):
    if a % 2 == 0 and b % 2 ==0:
        if a>b:
            return a
        else:
            return b
    else:
        if a<b:
            return a
        else:
            return b

print(numero(6,7))