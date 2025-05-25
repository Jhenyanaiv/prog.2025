try:
    print("informe  tempo que um veículo permaneceu no estacionamento" )
    h = int (input("H: "))
    m = int (input("M: "))

except ValueError:
    print("digite apenas números inteiros para horas e minutos")
    exit()

totalm = h * 60 + m

if totalm % 60 ==0:
    hp = totalm // 60
else :
    hp = totalm // 60 + 1

if hp > 12 :
    valor = 30 
else :
    if hp <= 2 :
        valor = hp * 8 
    elif hp <= 4 :
        valor = 2 * 8 + (hp - 2) * 5
    else :
        valor = 2 * 8 + 2 * 5 + (hp - 4) * 3

        print("o valor a ser pago " ,valor ,",00")