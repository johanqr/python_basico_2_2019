palabras1=[]
palabras2=[]
cantidad1 = int(input('Dígame cuántas palabras tiene la lista: '))

if cantidad1 <= 0:
    print('¡Imposible!')
else:
    for x in range(0,cantidad1):
        print('Dígame la palabra',x+1)
        palabra=input()
        palabras1.append(palabra)
    print('La lista creada es: ',palabras1)

cantidad2 = int(input('Dígame cuántas palabras tiene la lista de palabras a eliminar: '))

if cantidad2 <= 0:
    print('¡Imposible!')
else:
    for y in range(0,cantidad2):
        print('Dígame la palabra',y+1)
        palabra=input()
        palabras2.append(palabra)
    print('La lista de palabras a eliminar es:  ',palabras2)


for i in range(0,cantidad1-1):
    for j in range(0,cantidad2-1):
        if palabras1[i] == palabras2[j]:
            palabras1.remove(palabras2[j])

print('La lista es ahora: ',palabras1)