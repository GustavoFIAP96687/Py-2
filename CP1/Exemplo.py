print('Tabuada com WHILE')
 
num = int(input("Digite um numero para obter a tabuada: "))
 
while(num <= 0):
    print("Não pode numero negativo!")
    num = int(input("Digite um outro numero para obter a tabuada: "))
 
i = 1
 
while(i < 11):
    r = num * i
    print(f'{num} X {i} = {r}')
    i = i + 1










#p1 = float(input("Digite a nota da P1: "))
#p2 = float(input("Digite a nota da P2: "))
 
#m = (p1 + p2) / 2
 
#if (m >= 5):
    #print(f"Sua média foi {m:.2f} e você está aprovado!")
#else:
    #print("Reprovado!")
