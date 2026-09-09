Alunos = {}
Notas_boas = []

for i in range(5):
    nome = input("Insira o nome do aluno:")
    nota_final = float(input("Insira a nota de final do aluno:"))

    Alunos[nome] = nota_final

for nome, nota in Alunos.items():
    if nota_final >= 7:
        Notas_boas.append(nome)

soma = 0
for nota in Alunos.values():
    soma += nota

media_turma = soma/5
quant_aprovados = len(Notas_boas)

print("A média da turma é", media_turma)
print("A quantidade de alunos aprovados é", quant_aprovados)