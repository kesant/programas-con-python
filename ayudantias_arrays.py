# crear una funcion que dada un array de una dimension ,hacer un resumen estadistico de las edades ,verificar que el array sea de una dimension caso contrario entregar error.
import numpy as np
# def get_array_info(input_array):
#     if input_array.ndim > 1:
#         print("ERROR, EL ARRAY NO DEBE TENER MAS DE UNA DIMENSION ")
#     else :
#         print(f"cantidad de elementos del array {input_array.shape[0]}")
#         print(f"tipo de dato de los elementos del array {input_array.dtype}")
#         print(f"Valor minimo: {input_array.min()}")
#         print(f"Valor maximo: {input_array.max()}")
#         print(f"valor promedio : {input_array.mean()}")
#         print(f"suma de los  valores : {input_array.sum()}")


# new_array= np.array([16,25,19,58,22])
# get_array_info(new_array)
#debemos crear una matrix nxn , de numeros aleatorios entre 0 al 100
# def get_random_array(regs, values):
#     if type(regs) != int or type(values) != int:
#         print("ERROR: Los parámetros de la función deben ser números enteros.")
#     else:
#         return np.random.randint(100, size=(regs, values))

# print(get_random_array(5,5))
# dado un array de dos dimensiones, el valor total de las filas o valor total de las columnas 
# def array_sum(input_array):
#     if input_array.ndim != 2:
#         print("ERROR: El Array debe tener 2 Dimensiones.")
#     else:
#         # Variables para almacenar los índices:
#         row_index = 0
#         col_index = 0
#         # Arrays con las sumas de las filas y las columnas:
#         row_sum = input_array.sum(axis=1)
#         col_sum = input_array.sum(axis=0)
#         # Itero el array de suma de filas, para imprimir los valores:
        
#         for value in row_sum:
#             print(f"Total Fila {row_index}: {value}")
#             row_index += 1
#         # Itero el array de suma de columnas, para imprimir los valores:
#         for value in col_sum:
#             print(f"Total Columna {col_index}: {value}")
#             col_index += 1

# my_array_2D = np.array([[1, 2, 3],
#                            [4, 5, 6],
#                            [7, 8, 9]])
# array_sum(my_array_2D)

# np.all()
# Retorna True si todos los elementos del arreglo cumplen con la condición.
# np.any()
# Retorna True si almenos uno de los elementos del arreglo cumple con la condición.
# np.where()
# Retorna un arreglo con los índices de los elementos que cumplen con la condición.

# new_array=np.array([[12,56,15,45,56],[20,506,25,45,65]])
# print(new_array)
# print(np.all(new_array==12))
# print(np.any(new_array<20))
# fila,columna=np.where(new_array>50)
# print(fila,columna)
# dic_posiciones={}
# contador=0
# new_data=list(zip(fila,columna))
# for values in new_data:
#     dic_posiciones[f"posicion {contador}"]=new_array[values]
#     contador+=1
# print(dic_posiciones)
# def metricaPais(ddatos,dpaises):
#     d_PromediosMetricasPais = {}
#     for pais, ciudades in dpaises.items():

# 		for datos,valores in ddatos.items():						
# 			if datos[0] in ciudades :
# 				d_PromediosMetricasPais[(pais,datos[1])]+=valores 


#literal b de la leccion
dpaises = {"Ecuador": ["Guayaquil", "Cuenca"], "Colombia": ["Bogota"]}

ddatos={("Guayaquil","temperatura"): 29,("Guayaquil","precioCasas"): 130000, ("Cuenca","precioCasas"): 22,  ("Cuenca","temperatura"):120000,("Bogota","temperatura"): 20,  ("Bogota","precioCasas"):100000}
def metricaPais(ddatos,dpaises):
    d_PromediosMetricasPais = {}

    for pais, ciudades in dpaises.items():#separamos pais y ciudades del diccionario 
        for datos ,valores in ddatos.items():#por cada pais volvemos a recorrer ddatos y separamos por datos(la tupla con ciudad y metrica) y valores el valor de la metrica
            if datos[0] in ciudades:# verificamos que la ciudad pertenezca al pais
                if (pais,datos[1]) not in d_PromediosMetricasPais:#verificamos que la llave (pais,metrica) no este en el diccionario
                    d_PromediosMetricasPais[pais,datos[1]]=[valores]#creamos un nuevo valor en el diccionario con clave (pais ,metrica)y valor el valor de la metrica como lista
                else:
                    d_PromediosMetricasPais[pais,datos[1]]=d_PromediosMetricasPais[pais,datos[1]]+[valores]#en el caso de que (pais ,metrica) ya este en el diccionario agregamos el otro valor de la metrica a la lista

    for llave,valor in  d_PromediosMetricasPais.items():#recorremos el diccionario final 
        d_PromediosMetricasPais[llave]=sum(valor)/len(valor)#reemplazamos el valor de cada clave con su promedio 
    return d_PromediosMetricasPais

metricaPais(ddatos,dpaises)

