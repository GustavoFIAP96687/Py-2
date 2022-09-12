soma = 0
i = 1

while(i <= 10):
    numero = int(input('digite um numero: '))

    if(i == 1):
        maior = numero
        i = i + 1
    elif(numero > maior):
        maior = numero
        i = i + 1

    # soma dos valores
    soma = soma + numero

    # media
media = soma / 10

print('o maior é: ', maior)
print('soma é: ', soma)
print('a media é: ', media)