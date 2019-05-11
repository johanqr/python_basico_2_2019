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
    print('El promedio de la cantidad miles de colones en débito:: ')
    return (reduce(lambda x, y: (x+y), b[i]))/3

def suma(i):
    print('La suma de todas las deudas: ')
    return reduce(lambda x, y: x +y, b[i])

def multiplicacion(i):
    print('la multiplicación de todos los crédito entre si: ')
    return reduce(lambda x, y: x * y, b[i])


diccionario_funciones = {
    'elpromedio' : promedio,
    'lasuma' : suma,
    'lamultiplicacion' : multiplicacion
}

'''for i in range(3):
    i += 1
    if i == 1:
        print("El promedio de la cantidad miles de colones en débito: ",promedio(i))
    elif i == 2:
        print("la multiplicación de todos los crédito entre si: ", multiplicacion(i))
    else:
        print("La suma de todas las deudas: ",suma(i))'''

for i in range(3):
    i+=1
    print('=========================================================')
    for mi_funcion in diccionario_funciones.values():
        print(mi_funcion(i))







