listaFeriados=[]

dataInformada = input("Digite uma data dd/mm/yyyy: ")

while True:
    dados = [
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
    for feriado in dados:
        dataFormatada = feriado['date'][8:10] + "/" + feriado['date'][5:7] + "/" + feriado['date'][0:4]
        feriado.update({'date': dataFormatada})

        if (dataInformada[3:5] == feriado['date'][3:5]):
            feriadoMes = {'data':feriado['date'], 'nome': feriado['name']}
            listaFeriados.append(feriadoMes)

    if ( (len(listaFeriados) == 1) and (listaFeriados[0]['data'] == dataInformada)):
        print(f"A data que você digitou {dataInformada} é feriado - {listaFeriados[0]['nome']}")
    else:
        print('A data que você digitou não é feriado, mas temos todos esses no mês:')
        for fer in listaFeriados:   
            print(f"{fer['data']} - {fer['nome']}")