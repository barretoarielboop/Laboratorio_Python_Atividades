def realizar_saque(saldo,valor_saque):
    try:
        valor_saque = float(valor_saque)
        saldo = float(saldo)
    except:
        print('Valor incorreto')
    if  valor_saque > saldo:
        print('Saldo insuficiente')
    else:
        saldoAtualizado = saldo - valor_saque
        return saldoAtualizado
      #  print(saldoAtualizado)


if __name__ == '__main__':
    realizar_saque(1000,450)