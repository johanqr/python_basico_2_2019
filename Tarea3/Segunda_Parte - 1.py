palabras=[]
cantidad = int(input('Dígame cuántas palabras tiene la lista: '))

if cantidad <= 0:
    print('¡Imposible!')
else:
    for x in range(0,cantidad):
        print('Dígame la palabra',x+1)
        palabra=input()
        palabras.append(palabra)
    print('La lista creada es: ',palabras)
