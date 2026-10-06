def arquivo():
        while True:
                try:
                        relatorio_vendas = input("Insira o nome do arquivo desejado:")
                except FileNotFoundError:
                        print("Arquivo não encontrado.")
                else:
                        print("Arquivo existente.")
                        print("Requerimento encerrado.")
                        break

        return relatorio_vendas

relatorio_vendas = arquivo()
print(relatorio_vendas)
