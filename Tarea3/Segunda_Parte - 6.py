palabras1=[]
palabras2=[]
cantidad = int(input('Dígame cuántas palabras tiene la lista: '))

if cantidad <= 0:
    print('¡Imposible!')
else:
    for x in range(0,cantidad):
        print('Dígame la palabra',x+1)
        palabra=input()
        palabras1.append(palabra)
    print('La lista creada es: ',palabras1)


    for i in reversed(palabras1):
        palabras2.append(i)

print('La lista inversa es: ',palabras2)