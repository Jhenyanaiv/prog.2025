#O momento inicial da partida (no formato HH:MM);
#O momento de chegada (no formato HH:MM);
#O tempo parado para descanso (no formato HH:MM);
#A quantidade de litros de combustível gasto;
#O preço do litro de combustível (em R$) e;
#A distância percorrida (em Km);

#pedir hora e minutos seprados 
import sys

try:
    print("informe a hora de saida" )
    hs = int (input("H: "))
    ms = int (input("M: "))

    print("informe a hora de chegada" )
    hc = int (input("h: "))
    mc = int (input("m: "))

    print("informe a hora da pausa " )
    hd = int (input("h: "))
    md = int (input("m: "))

    l = float (input("informe a quantidade de litros de combustivel gasto: "))
    if l <=0:
        sys.exit('informe valor positivo :')

    p = float (input("informe o preço do litro de combustivel: "))
    if p <=0:
        sys.exit('informe valor positivo :')

    d = float (input("informe a distancia percorrida: "))

except ValueError:
    sys.exit("digite apenas números inteiros para horas ")

# agora preciso tranformar o que ele me deu em horas, em minutos, presta atencao opara nao mutiplicar tudo 

min_s = hs*60 +ms
min_c = hc*60 +mc
min_p = hd*60 +md 

# agora preciso ver o tempo de vaigem 
# perguntar como faz se o tempo passar de meia noite 

if min_c < min_s:
    min_c = min_c + 24*60

t_total_m = min_c - min_s
# agora preciso ver o tempo que passoi em movimenro 

t_total_movimento = t_total_m - min_p

# agora preciso coverter de vokta ao formsato de horas 
# para isso vejo quantas horas (60 mintos) cabe 
#depois os minutos vão ser o resto da divisao por 60
# e os segundos vão ser o resto da divisao por 60
tt_h = t_total_m //60
tt_m = t_total_m % 60
tt_s = t_total_m % 60
print (f'tempo total de viagem {tt_h}:{tt_m}:{tt_s}')
# agora preciso ver o tempo que passoi em movimenro
tm_h = t_total_movimento //60
tm_m = t_total_movimento % 60
tm_s = t_total_movimento % 60
print (f'tempo total de movimento {tm_h}:{tm_m}:{tm_s}')

# agora meter a infeliz da matematica para calcular velocidade media 
# tem que dividir por 60 para dar em horas 

v_m_global = d / t_total_m # essa é a velocidade media global 


v_m_movimento = d / t_total_movimento # essa é a velocidade media em movimento
print (f'velocidade media global {v_m_global} km/h')
print (f'velocidade media em movimento {v_m_movimento} km/h')

# agora preciso ver o custo da gasosa 
custo = l * p
print (f'o custo da gasosa foi de {custo} R$')

# agora o desempenho do carro em Km/l, l/h e R$/Km).

km_l = d/l 
print (f'o desempenho do carro foi de {km_l} km/l')

l_h = l/t_total_m/60
print (f'o desempenho do carro foi de {l_h} l/h')

reais_l = custo/d 
print (f'o desempenho do carro foi de {reais_l} R$/l')





