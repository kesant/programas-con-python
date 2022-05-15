#Your task is to write a function which returns the sum of following series upto nth term(parameter).
def series_sum(n):
    divisor=1
    resultado=0
    for i in range(n) :
        operacion=1/divisor
        resultado+=operacion
        divisor+=3
    return str(format(resultado, '.2f')) 
