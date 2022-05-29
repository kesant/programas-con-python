#Escribe un programa que determine si un número dado es par o impar
number=int(input("ingresa un numero: "))
condicion=number%2
if condicion==0:
    print("es un numero par")
else :
    print("es un numero impar")
