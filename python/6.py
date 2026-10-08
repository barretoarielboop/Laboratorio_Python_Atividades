leitor = int(input("Codigo do equipamento :"))

vericar = leitor % 2

if vericar == 0 :
    print('O codigo é par')
else :
    print('O codigo é impar')