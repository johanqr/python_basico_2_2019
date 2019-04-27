verduras = ['tomates','papas','cebollas','ajos']
frutas = ['piña','naranja','sandia']
carnes = ['mortadela','pollo','costilla']
limpieza = ['jabon','cloro','shampoo']
compras = [verduras,frutas,carnes,limpieza]
mi_lista = []
cantidad = 0


for categoria in compras:
    mi_lista.extend(categoria)
    print(mi_lista)

print('El total: ',len(mi_lista))
pass