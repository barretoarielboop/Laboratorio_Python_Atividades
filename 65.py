def calcularCubo(a):
    raiz = a**(1/3)
    return raiz

def calcularDivisaoCubo(a):
    if a % 3 == 0:
        calcularCubo(a)
        return a

print(calcularDivisaoCubo(9))