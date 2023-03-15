feriados = [
    {"date":"2023-01-01","name":"Confraternização mundial","type":"national"},
    {"date":"2023-02-21","name":"Carnaval","type":"national"},
    {"date":"2023-04-07","name":"Sexta-feira Santa","type":"national"},
    {"date":"2023-04-09","name":"Páscoa","type":"national"},
    {"date":"2023-04-21","name":"Tiradentes","type":"national"},
    {"date":"2023-05-01","name":"Dia do trabalho","type":"national"},
    {"date":"2023-06-08","name":"Corpus Christi","type":"national"},
    {"date":"2023-09-07","name":"Independência do Brasil","type":"national"},
    {"date":"2023-10-12","name":"Nossa Senhora Aparecida","type":"national"},
    {"date":"2023-11-02","name":"Finados","type":"national"},
    {"date":"2023-11-15","name":"Proclamação da República","type":"national"},
    {"date":"2023-12-25","name":"Natal","type":"national"}
]


comentarios = {}
def listar_feriados():

    print("Lista dos Feriados:")
    for i, feriado in enumerate(feriados):
        data = feriado['date'].split('-')
        print(f"{i+1} - {data[2]}/{data[1]}/{data[0]} - {feriado['name']}")

def ver_detalhes():

    id_feriado = int(input("Digite o id do feriado: "))
    feriado = feriados[id_feriado-1]
    print(f"\nDescrição do feriado: {feriado['name']}\n")
    if id_feriado in comentarios:
        comentarios_feriado = comentarios[id_feriado]
        print("Comentários sobre o feriado:")
        for id_comentario, comentario in comentarios_feriado.items():
            print(f"\t{id_comentario}: {comentario}")
    else:
        print("Não há comentários sobre o feriado")

def fazer_comentario():

    id_feriado = int(input("Digite o id do feriado: "))
    comentario = input("Digite o seu nome e o comentário sobre o feriado: ")
    if id_feriado in comentarios:
        comentarios[id_feriado][len(comentarios[id_feriado])+1] = comentario
    else:
        comentarios[id_feriado] = {1: comentario}

def excluir_comentario():

    id_feriado = int(input("Digite o id do feriado: "))
    if id_feriado in comentarios:
        print("Comentários sobre o feriado:")
        for id_comentario, comentario in comentarios[id_feriado].items():
            print(f"\t{id_comentario}: {comentario}")
        id_comentario = int(input("Digite o id do comentário que deseja excluir: "))
        del comentarios[id_feriado][id_comentario]
        print("Comentário excluído com sucesso!")
    else:
        print("Não há comentários sobre o feriado")


# Menu


while True:
    listar_feriados()
    print("\nEscolha uma opção:")
    print("1 - Ver detalhes do feriado")
    print("2 - Fazer um comentário do feriado")
    print("3 - Excluir um Comentario")

    op = int(input("Digite a opção desejada: "))

    if op == 1:
        ver_detalhes()
    elif op == 2:
        fazer_comentario()
    elif op == 3:
        excluir_comentario()



