import sys
produtos ={}
#=======================================================================================================================

def produtoInvalidoErro(x):
    if x in produtos.keys():
        print('========\nProduto já existente\n=========')
        return False
    else:
        return True
def valorInvalidoErro(x):
    if x <= 0:
        print('========\nValor do produto invalido\n=========')
        return False
    else:
        return True
def quantidadeInvalidoErro(x):
    if x <= 0:
        print('========\nQuantidade do produto invalido\n=========')
        return False
    else:
        return True
#=======================================================================================================================
def addProduto():
    global produtos
    while True:
        try:
            nome = str(input('Nome do produto: '))
            precoUni = float(input('Valor do produto: '))
            quantidade = int(input('Quantidade de entrada: '))
        except ValueError:
            print('Valores invalidos, repita !')
            continue
        if produtoInvalidoErro(nome) == False:
            continue
        if valorInvalidoErro(precoUni) == False:
            continue
        if quantidadeInvalidoErro(quantidade) == False:
            continue
        else:
            break

    produtos[nome] = {'Preço' : precoUni,'Estoque': quantidade ,'Vendas': 0}
    print('Tudo certo ! ')

def registrar_venda():
    global produtos
    for code, key in produtos.items():
        print(f'{code:<3} | R$ {key['Preço']:<3} reais | UNIDADES:{key["Estoque"]:>3}')
    print('\t\t°°°°°PRODUTO DE SAIDA°°°°°°')
    while True:
        try:
            nome = str(input('....SAIDA :  '))
            if nome not in produtos.keys():
                print('Digite um produto EXISTENTE !')
                continue
            quantidade = int(input('....QUANTIDADE: '))
            if quantidade < 1 or quantidade > produtos[nome]['Estoque']:
                print('Quantidade invalida')
                continue
            else:
                break
        except ValueError:
            print('Valores invalidos, repita !')
            continue
    produtos[nome]['Vendas'] += quantidade
    produtos[nome]['Estoque']-= quantidade
    print('======Venda Realizada com sucesso!=======')
    print(f'{produtos[nome]} |\nVendidos : {produtos[nome]['Vendas']} |\nRestam : {produtos[nome]['Estoque']} |')
    print('==========================================')
    main()

def gerar_relatorio():
    for code, key in produtos.items():
        vendas = [key['Vendas']]
        totalVendas = sum(vendas)
        faturamento = 0.0
        if produtos[code]['Vendas'] > 0:
            faturamento = key['Preço'] * totalVendas


    melhor = max(vendas)
    melhorProduto = produtos[code]['Vendas'] == melhor
    ticketMedio = totalVendas / faturamento
    print(f'O total de vendas foi : {totalVendas}\nO produto mais vendido foi :{melhorProduto}\nO faturamento foi : R${faturamento:.2f}\nTicket Medio de : R${ticketMedio:.2f}')


def main():
    print("ººººESCOLHAºººº")
    print("{Y} NOVO PRODUTO\n{N} REGISTRAR VENDA\n{R}Gerar Relatório\n{X} SAIR")
    usuar = str(input('.... :  ')) .upper()
    if usuar == 'Y':
        addProduto()
    if usuar == 'N':
        registrar_venda()
    if usuar == 'R':
        gerar_relatorio()
    elif usuar == 'X':
        sys.exit(0)
    else:
        print("Apenas Y | N | R | X ")
        main()





if __name__ == '__main__':
    main()