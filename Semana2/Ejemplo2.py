import math

a = float(input('Favor ingresar a:'))
b = float(input('Favor ingresar b:'))
c = float(input('Favor ingresar c:'))

discriminante = b ** 2 - 4*a*c

if discriminante < 0:
    raiz = math.sqrt(-discriminante) * complex(0,1) # Por ser negativo se mete al numero complejo i
else:
    raiz = math.sqrt(discriminante)


x1 = (-b + raiz) / (2*a)
x2 = (-b - raiz) / (2*a)

print(x1,x2)