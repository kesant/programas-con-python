# TEMA1 2016 2T

# vocales =["A", "E", "I", "O", "U"]
# consonantes = ["B", "C", "D", "F" ,"G", "H", "J", "K", "L", "M", "N", "P" ,"Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
# usuario=input("Ingrese el texto separado por espacios en blanco o un punto : ").upper()
# usuario=usuario.replace("."," ")
# list_palabras=usuario.split(" ")
# vocales_count=0
# consonantes_count=0
# iguales=0
# for palabra in list_palabras:
#     if palabra.isalpha():
#         for letra in palabra:
#             if letra in vocales:
#                 vocales_count+=1
#             elif letra in consonantes:
#                 consonantes_count+=1
#         if vocales_count==consonantes_count:
#             iguales+=1
# print(f"La cantidad de paalabras con la misma cantidad de vocales y consonantes es {iguales}")

##############################################################

#TEMA 2 2016 1T
# visitados = ['maria2|www.facebook.com|160', 'xavi7|www.eluniverso.com|50','jose15|www.sri.gob.ec|30', 'maria2|www.twitter.com|30','xavi7|www.inec.gob.ec|10', 'maria2|www.espol.edu.ec|50',
# 'jose15|www.sri.gob.ec|120', 'xavi7|www.sri.gob.ec|20','maria2|www.twitter.com|20' ]
# empleados = ['maria2', 'jose15', 'xavi7']
# trabajo = ['www.espol.edu.ec', 'www.inec.gob.ec', 'www.sri.gob.ec']
# notrabajo_visitado=[]
# for visita in visitados:
#     visita=visita.split("|")
#     if (visita[1] not in trabajo) and (visita[1] not in notrabajo_visitado):
#         notrabajo_visitado.append(visita[1])
# print(notrabajo_visitado)

###########################################################################

#TEMA4 2016 1T
# mensaje = "No basta saber, se debe también aplicar. No es suficiente querer, se debe también hacer. Goethe (1749-1832)"
# largo=len(mensaje)
# cual='be' 
# cuantos=0 
# lista=[]
# donde=-1 
# i=0
# while (i<largo): 
#     donde=mensaje[i:].find(cual) 
#     if (donde>0):
#         cuantos=cuantos+1 
#         i=i+donde+1 
#         lista.append(donde)
#     else:
#         i=i+1
# print (cuantos)
# print (lista)
# temab
# lista = [5,3,2,6,7,34,1,23,5,6]
# lista2 = []
# for i in range(1,len(lista)):
#     if (lista[i-1] <= lista[i]) and (lista[i] >= lista[i+1]):
#         lista2.append(lista[i])
# print(lista2)

###################################################3############################
# TEMA1 2017 1t
# abecedario = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# equivale = [1,3,3,2,1,4,2,4,1,9,5,1,3,1,1,3,10,1,1,1,1,4,4,9,4,10]
# palabras= "CAS*A*,S*ASTR*E*,R*EY*,A*ZOTE*"
# list_palabras=palabras.split(",")
# lista_cuenta=[]
# lista_normal=[]
# print("Las calificaciones de las palabras son: ")
# for  palabra in list_palabras:
#     if palabra.isupper():
#         cuenta=0
#         palabra_normal=palabra.replace("*","").lower()
#         for indice in range(len(palabra)):
#             if palabra[indice]=="*":
#                 indice_letra=abecedario.find(palabra[indice-1])
#                 cuenta+=equivale[indice_letra]
#             else :
#                 indice_letra=abecedario.find(palabra[indice])
#                 cuenta+=equivale[indice_letra]
#         lista_cuenta.append(cuenta)
#         lista_normal.append(palabra_normal.upper())
#         print(f"{palabra_normal} :       {cuenta}")
#     else:
#         cuenta=0
#         palabra_normal=palabra.replace("*","").lower()
#         print(f"{palabra_normal} :       {cuenta}")
# ind_max=lista_cuenta.index(max(lista_cuenta))
# print(f"La palabra con mayor puntaje es {lista_normal[ind_max]} ({max(lista_cuenta)} puntos)")

