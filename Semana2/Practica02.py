import math

a = float(input('Favor ingresar a:'))
b = float(input('Favor ingresar b:'))
c = float(input('Favor ingresar c:'))

x1 = ((b * -1) + (math.sqrt((b**2)-(4*a*c))))/(2*a)
print('Valor de x1 ',x1)

x2 = ((b * -1) - (math.sqrt((b**2)-(4*a*c))))/(2*a)
print('Valor de x1 ',x2)

