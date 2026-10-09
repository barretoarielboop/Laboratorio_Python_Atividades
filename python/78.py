def calcular_media(n1,n2,n3):

    try:
        a = float(n1)
        b = float(n2)
        c = float(n3)


    except ValueError:
        print('valor invalido')

    if a < 0 or b < 0 or c < 0:
        print('valor invalido')

    if a > 10 or b > 10 or c > 10:
        print('valor invalido')
    x = ((a+b+c)/3)
    if x > 5 :
        print('Aprovado')
    else:
        print('Reprovado')
    print(x)
if __name__ == '__main__':
    calcular_media(6,5.5,6)
