#Escriba un programa que interprete el índice de masa corporal (IMC) en función del peso y la altura de un usuario.
#Debe decirles la interpretación de su IMC en función del valor de IMC:
#Menos de 18,5 tienen bajo peso
#Por encima de 18,5 pero por debajo de 25 tienen un peso normal
##Por encima de los 25 pero por debajo de los 30 tienen un ligero sobrepeso
#Mayores de 30 pero menores de 35 son obesos
##Por encima de 35 son clínicamente obesos.
altura =float(input("Ingresa tu altura m: "))
peso=float(input("Ingresa tu peso en kg :"))
imc=round((peso/altura**2),2)
print(imc)
if imc <18.5:
   print(f"Tu IMC es {imc}, tienes bajo peso.")
elif imc<25 :
    print(f"Tu IMC es {imc}, tienes un peso normal.")
elif imc<30 :
    print(f"Tu ICM es  {imc}, estas ligeramente en sobrepeso.")
elif imc<35 :
    print(f"Tu ICM es {imc}, estas obeso.")
else:
    print(f"Tu ICM es {imc}, tienes mucho sobrepeso..")
