# Faça um programa que solicite ao usuário um número de até 4 dígitos inteiro positivo
# e exiba a soma dos seus algarismos.

import sys
try:
    numero = int (input('digite um número de 4 digitos'))

    if numero <=0:
        sys.exit('informe valor positivo')

    if numero > 9999:
        sys.exit("digite um número de apenas 4 digitos")

    else:
        if numero < 10:
            soma = numero
        if numero >= 10 and numero < 100:
            soma = (numero // 10 ) + (numero % 10)
        if numero >=100 and numero < 1000:
            soma = numero // 100 + (numero % 100) // 10 + (numero % 10) 
        if numero >= 1000 and numero <=9999:
            soma = numero // 1000 + (numero % 1000) // 100 + (numero % 100) // 10 + (numero % 10)

except ValueError:
    sys.exit("digite apenas números inteiros positivos")
print ("soma dos algarismo é:",soma)
