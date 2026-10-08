def numero(a):
    divisores = []
    for i in range(1, a):
        if a % i == 0:
            divisores.append(i)
 
    if sum(divisores) == a:
        return "número perfeito"
    else:
        return "numero imperfeito"


print(numero(7))