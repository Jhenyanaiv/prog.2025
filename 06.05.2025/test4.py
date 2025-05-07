import sys

v0 = int (input('digite a velocidade inicial'))

if v0 <=0:
    sys.exit('informe valor positivo')

d = int (input('digite a distancia entre lajes e natal'))

if d <=0:
    sys.exit('informe valor positivo')

a = int (input('digite a aceleração '))

if a <=0:
    sys.exit('informe valor positivo')

d = int (v0 * d + (a * d **2)/2)

print (d)
