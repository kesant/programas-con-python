menu="""
Bienvenido al conversor de Monedas 💵💰

1.-Pesos colombianos
2.-Pesos arrgentinos
3.-Pesos mexicanos

Elije una opcion :
"""
opcion =int(input (menu))
if opcion==1:
    pesos=input ("Cuantos pesos colombianos tienes ? : ")
    pesos= float(pesos)
    valor_dolar =3875
    dolares=pesos/valor_dolar
    dolares=round(dolares,2)
    dolares=str(dolares)
    print("tienes $ "+dolares+" dolares")
elif opcion==2:
    pesos=input ("Cuantos pesos argentinos tienes ? : ")
    pesos= float(pesos)
    valor_dolar =65
    dolares=pesos/valor_dolar
    dolares=round(dolares,2)
    dolares=str(dolares)
    print("tienes $ "+dolares+" dolares")
elif opcion==3:
    pesos=input ("Cuantos pesos mexicanos tienes ? : ")
    pesos= float(pesos)
    valor_dolar =24
    dolares=pesos/valor_dolar
    dolares=round(dolares,2)
    dolares=str(dolares)
    print("tienes $ "+dolares+" dolares")
else :
    print("ingresa una opcion valida, porfavor") 
