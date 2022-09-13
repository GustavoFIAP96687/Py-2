n = int(input("Digite o valor de n: "))
while (n <= 0): n = int(input("Informe somente valores positivos: "))

fatorial = 1
multiplica = 2
while (multiplica <= n):
    fatorial = fatorial*multiplica

    multiplica = multiplica + 1

    if (multiplica - 1 == n):
        print(f"O valor de {n}! é = {fatorial}")

        pergunta = input("\nDeseja executar o programa novamente? 'SIM' ou 'NAO': ")
        while (pergunta != 'SIM' and pergunta != 'NAO'): 
            pergunta = input("Deseja executar o programa novamente? 'SIM' ou 'NAO': ")
        if (pergunta == 'SIM'): 
            multiplica = 2
            fatorial = 1

            n = int(input("Digite o valor de n: "))
            while (n <= 0): n = int(input("Informe somente valores positivos: "))