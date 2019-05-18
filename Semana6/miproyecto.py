# esto es un proyecto que usa otro modulo

from archivo1 import suma_resta

resultado = suma_resta(a=10,b=3,c=2)

print(resultado)

from archivo2 import mi_lista,mi_diccionario

print('esto es un ejemplo')
from subfolder.archivo3 import Pato

donald = Pato()
p = donald.camina()

mi_lista.append(7)

pass