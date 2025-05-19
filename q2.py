import sys

v = float (input("digite o valor que voce deseja sacar"))
if v <=0:
    sys.exit('informe valor positivo :')

# converter em centavos para conseguir dividir em todas as cedulas 
# 1 real = 100 centavos 

centavos = v * 100

# como a maiot nota é a de cem, preciso ver quanttas notas podem ser usadas. 100 reais = 10000 centvos 

# se centavos for maior igual a 10000, eu posso usar uma ou mais notas de 100
if centavos >= 10000:
    # q vai ser de quantidade de notas 
    q = centavos // 10000
    # imprimir quantidade 
    print (f"{q} notas de 100 R$")
    #agora preciso ver o que sobrou 
    centavos = centavos % 10000

#agora com 50 R$ = 5000 centavos
if centavos >= 5000:
    q = centavos // 5000
    print (f"{q} notas de 50 R$") 
    centavos = centavos % 5000

# agora repete ate o utimo centasvo 

if centavos >= 2000:
    q = centavos // 2000
    print (f"{q} notas de 20 R$") 
    centavos = centavos % 2000

if centavos >= 1000:
    q = centavos // 1000
    print (f"{q} notas de 10 R$") 
    centavos = centavos % 1000

if centavos >= 500:
    q = centavos // 500
    print (f"{q} notas de 05 R$") 
    centavos = centavos % 500

if centavos >= 200:
    q = centavos // 200
    print (f"{q} notas de 2 R$") 
    centavos = centavos % 200

if centavos >= 100:
    q = centavos // 100
    print (f"{q} moedas de 1 R$") 
    centavos = centavos % 100

if centavos >= 50:
    q = centavos // 50
    print (f"{q} moedas de 0,50 centavos") 
    centavos = centavos % 50

if centavos >= 25:
    q = centavos // 25
    print (f"{q} moedas de 0,25 centavos") 
    centavos = centavos % 25

if centavos >= 10:
    q = centavos // 10
    print (f"{q} moedas de 0,10 centavos") 
    centavos = centavos % 10

if centavos >= 5:
    q = centavos // 5
    print (f"{q} moedas de 0,05 centavos") 
    centavos = centavos % 5





