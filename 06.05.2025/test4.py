import sys

v0 = int (input('digite a velocidade inicial'))

if v0 <=0:
    sys.exit('informe valor positivo')

t = int (input('digite a distancia entre lajes e natal'))

if t <=0:
    sys.exit('informe valor positivo')

a = int (input('digite a aceleração '))

if a <=0:
    sys.exit('informe valor positivo')

d = (v0 * t + (a * t **2)/2)

print (d)
