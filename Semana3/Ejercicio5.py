verduras = ['tomates','papas','cebollas','ajos']
frutas = ['piña','naranja','sandia']
carnes = ['mortadela','pollo','costilla']
limpieza = ['jabon','cloro','shampoo']
compras = [verduras,frutas,carnes,limpieza]

verduras.append('chile')
frutas.append('mango')

#verduras.clear()
#del verduras #borra la variable pero los datos siguen en memoria
#del verduras = [] # recrea la variable pero los datos aun siguen en memoria
del verduras[:] # borra los datos de la lista

print(compras)
pass