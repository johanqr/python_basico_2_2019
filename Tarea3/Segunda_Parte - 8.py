palabras1=[]
palabras2=[]
cantidad1 = int(input('Dígame cuántas palabras tiene la primera lista: '))
palabras3=[]
palabras4=[]
palabras5=[]
palabras6=[]

if cantidad1 <= 0:
    print('¡Imposible!')
else:
    for x in range(0,cantidad1):
        print('Dígame la palabra',x+1)
        palabra=input()
        palabras1.append(palabra)
    print('La primera lista es: ',palabras1)

cantidad2 = int(input('Dígame cuántas palabras tiene la segunda lista: '))

if cantidad2 <= 0:
    print('¡Imposible!')
else:
    for x in range(0,cantidad2):
        print('Dígame la palabra',x+1)
        palabra=input()
        palabras2.append(palabra)
    print('La segunda lista es: ',palabras2)


palabras1 = list(dict.fromkeys(palabras1))
palabras2 = list(dict.fromkeys(palabras2))

for i in palabras1:
    for j in palabras2:
        if i == j:
            palabras3.append(i)
            palabras6.append(i)

for a in palabras1:
    if a not in palabras2:
        palabras4.append(a)
        palabras6.append(a)

for b in palabras2:
    if b not in palabras1:
        palabras5.append(b)
        palabras6.append(b)


print('Palabras que aparecen en las dos listas:',palabras3)
print('Palabras que sólo aparecen en la primera lista:',palabras4)
print('Palabras que sólo aparecen en la segunda lista:',palabras5)
print('Todas las palabras:',palabras6)
