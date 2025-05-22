print("informe os coeficiente " )
a = float (input(" A "))
b = float (input(" b "))
c = float (input(" c "))

delta = b**2 - 4*a*c
if delta > 0 :
    raizd = delta ** 0.5
    x1 = (-b + raizd) / (2*a)
    x2 = (-b - raizd) / (2*a)
    print ("duas raizes reais ")
    print("x1",x1)
    print("x2",x2)

elif delta == 0 :
    x = -b / (2*a)  
    print("uma raiz real ")
    print("x",x)

else:
    print("não tem raiz real ")