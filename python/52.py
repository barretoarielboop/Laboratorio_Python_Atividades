medicamentos = {}

for i in range(0,5):
    entrada_med = input("Insira o nome do medicamento")
    quantidade_med = int(input("Insira a quantidade restante do medicamento em estoque:"))
    medicamentos[entrada_med] = quantidade_med

consulta = input("Qual medicamento você deseja consultar?:")

if consulta in medicamentos:
    print("Há",medicamentos[consulta],"unidades restantes do medicamento desejado.")
else:
    print("Medicamento não encontrado.")