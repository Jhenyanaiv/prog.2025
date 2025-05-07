import sys

# x = -b + raiz de delta / 2 * a 

# b velocidade inicial v0 
# a aceleração a 
# 

d = int (input('digite a distancia entre lajes e natal :'))

if d <=0:
    sys.exit('informe valor positivo :')

v0 = int (input('digite a velocidade inicial:'))

if v0 <=0:
    sys.exit('informe valor positivo:')

a = int (input('digite a aceleração : '))

if a <=0:
    sys.exit('informe valor positivo :')

d *= 1000 

v0 /= 3.6 

delta = v0**2-4*a*d 
if a <=0:
    sys.exit('não é possivel calcular o tempo ')

t = (-v0+delta**0.5)/(2*a) 

hora = t//3600

t = t%3600

minuto = t//60 

segundo = t%60

print (f'tempo = {hora}:{minuto}:{segundo}')
