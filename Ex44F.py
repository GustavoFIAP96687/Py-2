for i in range(1, 10, 1):
    numero = int(input('digite um numero: '))

    if(i == 1):
        maior = numero
    elif(numero > maior):
        maior = numero

    # soma dos valores
    soma = soma + numero

    # media
media = soma / 10

print('o maior é: ', maior)
print('soma é: ', soma)
print('a media é: ', media)