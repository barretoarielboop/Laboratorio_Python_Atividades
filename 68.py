lucro = float(input("Insira o lucro do trimeste: R$"))

try:
    acionistas = int(input("Insira o número de acionistas: "))
    divisao = lucro/acionistas
except ZeroDivisionError:
    print("A quantidade de acionistas não pode ser 0.")
except ValueError:
    print("Quantidade inválida.")
else:
    print("O valor recebido por cada acionista será de R$", divisao)