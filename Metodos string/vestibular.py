alunosVestibular = "Jose dos Santos,7,Sao Paulo;Sandra Silva,6.5,Sao Jose do Rio Preto;Augusto Soares,8,Sao Paulo;Vanderlei Azevedo,5.65,Santos;Vanessa Ferreira,9,Sao Paulo;Natan Cruz,10,Sao Paulo"

candidatos_aprovados = {}


alunos = alunosVestibular.split(";")

for aluno in alunos:
    atributos = aluno.split(",")
    nome = atributos[0]
    nota = float(atributos[1])
    cidade = atributos[2]


    if nota >= 7:
        candidatos_aprovados[nome] = {"Nota": nota, "Cidade": cidade}


for nome, atributos in candidatos_aprovados.items():
    print("Nome: " + nome)
    print("Nota: " + str(atributos["Nota"]))
    print("Cidade: " + atributos["Cidade"])
    print()