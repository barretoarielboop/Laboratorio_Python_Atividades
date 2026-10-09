def cadastra_produto(nome,preco,quantidade):
    try:
        nome = str(nome)
        preco = float(preco)
        quantidade = int(quantidade)
    except:
        print('Valores invalidos')
    if preco < 0 :
        print('Preço invalido')
    elif quantidade < 0 :
        print('Quantidade invalida')
    else:
        print('SUCESSO')

if __name__=='__main__':
    cadastra_produto('Pipoca', 5.50, 78)