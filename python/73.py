lista_preco = ['10.0','5.50','7.50','22.00','15.75']

try:
    lista_preco_numero = float(lista_preco)
except TypeError:
    print('ops')
else:
    print((lista_preco_numero + 100)/ 10 )