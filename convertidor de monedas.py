def conversor(tipo_pesos,valor_dolar):
    pesos=input ("Cuantos pesos "+tipo_pesos+" tienes ? : ")
    pesos= float(pesos)
    dolares=pesos/valor_dolar
    dolares=round(dolares,2)
    dolares=str(dolares)
    print("tienes $ "+dolares+" dolares")
    
menu="""
Bienvenido al conversor de Monedas 💵💰

1.-Pesos colombianos
2.-Pesos arrgentinos
3.-Pesos mexicanos

Elije una opcion :
"""
opcion =int(input (menu))
if opcion==1:
    conversor("Colombianos",3875)
elif opcion==2:
    conversor("Argentinos",65)
elif opcion==3:
    conversor("Mexicanos",24)
else :
    print("ingresa una opcion valida, porfavor") 
