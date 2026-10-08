materias = ("Português", "Matemática")

Alunos = []

for i in range(10):
    nome = input("Insira o nome do aluno:")
    nota_portugues = float(input("Insira a nota de português do aluno:"))
    nota_matematica = float(input("Insira a nota de matemática do aluno:"))

    Aluno = {"Nome": nome, "Matemática": nota_matematica, "Português": nota_portugues}

    Alunos.append(Aluno)

for Aluno in Alunos:
    media = (nota_portugues + nota_matematica)/2
    if media >= 7:
        print("Aluno(a) aprovado(a)")
    else:
        print("Aluno(a) reprovado(a)")