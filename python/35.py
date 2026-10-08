produto_a = input("Insira o nome do produto:")
produto_b = input("Insira o nome do produto:")
produto_c = input("Insira o nome do produto:")

Estoque = {produto_a: 0, produto_b: 0, produto_c: 0}

quant_a = int(input("Insira a quantidade do produto", produto_a, ":"))
quant_b = int(input("Insira a quantidade do produto", produto_b, ":"))
quant_c = int(input("Insira a quantidade do produto", produto_c, ":"))

Estoque[produto_a]=quant_a
Estoque[produto_b]=quant_b
Estoque[produto_c]=quant_c

print(Estoque)