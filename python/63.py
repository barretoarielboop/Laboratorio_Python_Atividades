

def juntar(a, b, c, d, e):
    numeros = []
    numeros.append(a)
    numeros.append(b)
    numeros.append(c)
    numeros.append(d)
    numeros.append(e)

    def maior(numeros):
        maior_numero = max(numeros)
        return maior_numero
    
    def menor(numeros):
        menor_numero = min(numeros)
        return menor_numero
    return numeros, maior(numeros), menor(numeros)



print(juntar(1, 2, 3, 4, 5))