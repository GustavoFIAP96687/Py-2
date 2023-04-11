
baseDados = 'CJose dos Santos,42,Sao Paulo;CSandra Silva,36,Sao Jose do Rio Preto;CAugusto Soares,22,Sao Paulo;CVanderlei Azevedo,45,Santos;CVanessa Ferreira,27,Sao Paulo;PMouse,1,9.90;PTeclado,3,19.90;PMonitor,2,349.90;PHD SSD,2,199.90;PProcessador,1,350.00'


dados_individuais = baseDados.split(';')


clientes = {}
produtos = {}


for dado in dados_individuais:
    tipo = dado[0] # 
    info = dado[1:].split(',') # 
    if tipo == 'C':
        clientes[info[0]] = {'idade': info[1], 'cidade': info[2]}
    elif tipo == 'P':
        produtos[info[0]] = {'quantidade': info[1], 'preco': info[2]}

# Exibe as informações de clientes
print('Clientes:')
for nome, info in clientes.items():
    print('Nome:', nome)
    print('Idade:', info['idade'])
    print('Cidade:', info['cidade'])
    print()

# Exibe as informações de produtos
print('Produtos:')
for nome, info in produtos.items():
    print('Nome:', nome)
    print('Qtd em estoque:', info['quantidade'])
    print('Preço:', info['preco'])
    print()
