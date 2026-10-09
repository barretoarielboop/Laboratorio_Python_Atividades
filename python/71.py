class saldoInsulficiennteErro(Exception):
    pass
saldo = 2000.00
saque = float(input("Insira o valor do saque "))
if saque > saldo:
    raise saldoInsulficiennteErro('Saldo invalido')