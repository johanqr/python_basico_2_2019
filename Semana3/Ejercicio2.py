verduras = ['tomates','papas','cebollas','ajos']
frutas = ['piña','naranja','sandia']
carnes = ['mortadela','pollo','costilla']
limpieza = ['jabon','cloro','shampoo']
compras = [verduras,frutas,carnes,limpieza]
cantidad = 0


for categoria in compras:
    print (categoria,len(categoria))
    cantidad += len(categoria)

print('El total: ',cantidad)
pass