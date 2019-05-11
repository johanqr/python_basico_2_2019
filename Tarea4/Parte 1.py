import math
from functools import reduce

hoja_calculo = [
    ['carlos', 54.54,6.57,3.64],
    ['juan', 5.54,9.57,4.64],
    ['luis', 9.54,7.57,1.64] ,
]

#print (hoja_calculo)

def transpuesta(hoja_calculo):
    return [list(i) for i in zip(*hoja_calculo)]

b = transpuesta(hoja_calculo)
b #sea b la tabla resultante luego de aplicar transpuesta

print (b)

#b[1] = list(map(lambda x: x/10, b[2]))
#print (b)




def promedio (i):
    return (reduce(lambda x, y: (x+y), b[i]))/3

def suma(i):
    return reduce(lambda x, y: x +y, b[i])

def multiplicacion(i):
    return reduce(lambda x, y: x * y, b[i])

diccionario_funciones = {
    'elpromedio' : promedio,
    'lasuma': suma,
    'lamultiplicacion': multiplicacion
}
'''for i in range(3):
    i += 1
    print("Lista: ",i)
    print("Promedio: ",promedio(i))
    print("Suma:",suma(i))
    print("Multiplicacion:",multiplicacion(i))'''

for mi_funcion in diccionario_funciones.values():

        print(mi_funcion(i))




