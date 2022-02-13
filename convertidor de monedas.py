
def conversor(tipo_pesos,valor_dolar):
    pesos=input ("Cuantos pesos "+tipo_pesos+" tienes ? : ")
    if pesos.isnumeric():
        pesos= float(pesos)
        dolares=pesos/valor_dolar
        dolares=round(dolares,2)
        dolares=str(dolares)
        print("tienes $ "+dolares+" dolares")        
    else :
        print("ingresa una opcion valida, porfavor")
    
menu="""
Bienvenido al conversor de Monedas 💵💰

1.-Pesos colombianos
2.-Pesos arrgentinos
3.-Pesos mexicanos

Elije una opcion :
"""
opcion =input (menu)
if opcion.isnumeric():
    if int(opcion)==1:
        conversor("Colombianos",3875)
    elif int(opcion)==2:
        conversor("Argentinos",65)
    elif int(opcion)==3:
        conversor("Mexicanos",24)
    else :
        print("ingresa una opcion valida, porfavor") 
else :
    print("ingresa una opcion valida, porfavor")