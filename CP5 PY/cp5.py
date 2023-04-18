def cadastrar_pedido():
    nome = input("Digite o seu nome: ")
    quantidade_produtos = int(input("Digite a quantidade de produtos que deseja comprar: "))

    with open("pedidos.txt", "a") as arquivo_pedidos:
        arquivo_pedidos.write(nome + "\n")
        total_pedido = 0

        for i in range(quantidade_produtos):
            nome_produto = input("Digite o nome do produto: ")
            quantidade = int(input("Digite a quantidade desejada: "))
            preco_unitario = float(input("Digite o preço unitário: "))
            preco_total = quantidade * preco_unitario
            total_pedido += preco_total
            arquivo_pedidos.write(nome_produto + "," + str(quantidade) + "," + str(preco_unitario) + "\n")

        arquivo_pedidos.write("\n")

    with open("total_pedidos.txt", "a") as arquivo_total:
        arquivo_total.write(nome + " - R$ " + "{:.2f}".format(total_pedido) + "\n")


while True:
    opcao = input("Deseja cadastrar um novo pedido? (s/n) ")
    if opcao.lower() == "s":
        cadastrar_pedido()
    else:
        print("Fim do programa")
