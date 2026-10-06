def vinteum(a, b, c):
    conjunto = []
    conjunto.append(a)
    conjunto.append(b)
    conjunto.append(c)

    soma = sum(conjunto)
    if soma >= 21 and 11 in conjunto:
        soma_diminuida = soma-10
        if soma_diminuida > 21:
            print(-1)
    else:
        soma_diminuida = soma
        print(soma_diminuida)
    

    return soma_diminuida
    


print(vinteum(11,11,11))


