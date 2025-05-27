import sys

try:

    multiplicador = int (input("informe o multiplicador"))
except ValueError:
    sys.exit("digite apenas números inteiros positivos")

else:
    if multiplicador < 0 :
        sys.exit("digite um valor valido")

multiplicando = 1 
while multiplicando <= 10:
    print (f"{multiplicador} X {multiplicando} = {multiplicador * multiplicando}")
    multiplicando += 1

print("fim da tabuada")

