
# def imprimir_nombre(nombre,apellidos,paralelo=10):
    
#     print(f"tu nombre es {nombre} y tu apellido es {apellidos},tu paralelo {paralelo}")

# #**************************************
# usuario=input("ingresa tu nombre: ")
# apellido=input("ingresa tu apellido :")
# curso=54
# imprimir_nombre(apellidos=apellido, nombre=usuario,paralelo=curso)
# def operacion_matematica(valor_1,valor_2):
#     resultado =valor_1+valor_2
#     print(resultado)
#******************************************************
# def conversacion(mensaje):
#     print("Hola")
#     print("Cómo estás")
#     print(mensaje)
#     print("Adios")
# #************************
""""5.  Como asistente de médico, usted tiene la tarea de generar un informe de indicadores a partir de un examen de sangre. El resultado del examen se lo entregan como una cadena de texto. Los indicadores los puede identificar porque estos siempre estarán en mayúsculas, por ejemplo, INR, WBC, RBC, TA, etc. Todo indicador va seguido de un espacio, luego un número con decimales, seguido de otro espacio en blanco y finalmente las unidades. Al final del resultado se encuentra el nombre del médico. Ejemplos de resultados:

resultado = “Resultado de Laboratorio ‘Su Salud’ Nombre del paciente: Jose Aimas E-mail del paciente: jose.aimas@gmail.com Resultados del laboratorio: INR 1.25 segundos BGT 180.12 mmol/dL HGB 13 g/dL ESR 3.2 mm/hora RBC 4000024.2 cel/uL TA 1.5 ng/dL WBC 123233.23 cel/uL. Los valores de este informe no representan un diagnóstico. Firmamédico responsable Dr. Juan Pozo”

resultado = “Resultado de Laboratorio ‘Sana’ Nombre del paciente: Ginger Irene Cruz Jurado Edad: 25 años E-mail: giircrju@espol.edu.ec Resultados: Azúcar BGT 180.12 mmol/dL Hemoglobina HGB 13 g/dL Hormonal TA 1.5 ng/dL. Médico responsable Dra. Karina Elizabeth Plaza”

La cantidad de indicadores puede variar. Los puntos no solo aparecen en los decimales, sino también para separar párrafos o en otras ocasiones como las direcciones de e-mail.

Escriba un programa que nos muestre la información desglosada, el nombre del médico 

INFORME DE LABORATORIO
**********************
INR  1.25    segundos
BGT  180.12    mmol/dL
HGB  13    g/dL
ESR  3.2    mm/hora
RBC  4000024.2  cel/uL
TA  1.5    ng/dL
WBC  123233.23  cel/uL
Médico: Juan Pozo    """


resultado = "Resultado de Laboratorio ‘Sana’ Nombre del paciente: Ginger Irene Cruz Jurado Edad: 25 años E-mail: giircrju@espol.edu.ec Resultados: Azúcar BGT 180.12 mmol/dL Hemoglobina HGB 13 g/dL Hormonal TA 1.5 ng/dL. Médico responsable Dra. Karina Elizabeth Plaza"
lista_palabras=resultado.split(" ")
print(lista_palabras)
lista_final=[]
for i in lista_palabras:
    if i.isupper():
        posicion=lista_palabras.index(i)
        lista_final.append([lista_palabras[posicion],lista_palabras[posicion+1],lista_palabras[posicion+2]])
print(lista_final)
print("INFORME DE LABORATORIO")
print("********************")
for posiciones in range(len(lista_final)-1):
    print("{0:10} {1:10} {2:10}".format(lista_final[posicion][0],lista_final[posicion][1],lista_final[posicion][2]))