import math

print("informe  o comprimento dos lados" )
a = float (input(" A: "))
b = float (input(" B: "))
c = float (input (" C: "))

#calcular se os lados formam um triangulo
if a + b > c and a + c > b and b + c > a :
   print("Os lados informados formam um triângulo.")
   
   #calcular os angulos do triangulo usando a biblioteca que trnsforma radianos em graus
   ang_a = math.degress(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
   ang_b = math.degress(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
   ang_c = math.degress(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))

   print(f" angulo A: {ang_a:.2f}")
   print(f" angulo B: {ang_b:.2f}")
   print(f" angulo C: {ang_c:.2f}")


    # agora para saber qual tipo de triangulo 
   if a == b and b == c: # todos os lados são iguais
    print("O triangulo é equilátero")
   else :
        if a == b or b == c or a == c: # dois lados são iguais
            print("O triangulo é isósceles")
        else: # e se não for nenhuma desses, so pode ser escaleno
            print("O triangulo é escaleno")

    #e agora pra saber qual tip de triangulo em relaçao aos angulos 
   if ang_a == 90 or ang_b == 90 or ang_c == 90:
        print("O triangulo é retângulo")    #quando um dos angulos é 90 
   else:
        if ang_a > 90 or ang_b > 90 or ang_c > 90:
            print("O triangulo é obtusângulo")    #quando um dos angulos é maior que 90 
        else:
            print("O triangulo é acutângulo")   #se nao for nenum so pode ser actangulo quando todos os angulos são menores que 90

else:
    print("Os lados informados não formam um triângulo.")
    
    
