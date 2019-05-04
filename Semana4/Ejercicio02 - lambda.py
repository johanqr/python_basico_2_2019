import math
resta = lambda x,y : x-y
multiple = lambda x,y : x*y
divide = lambda x,y : x/y
potencia = lambda x,y : math.pow(x,y)
raiz = lambda x,y : math.pow(x, 1/y)
x=3
y=2

diccionario_funciones = {
    'suma' : lambda x,y : x+y,
    'resta' : resta,
    'multiplica' : multiple,
    'divide' : divide,
    'potencia' : potencia,
    'raiz' : raiz
}


for mi_funcion in diccionario_funciones.values():
    print('resultado=',mi_funcion(x,y))