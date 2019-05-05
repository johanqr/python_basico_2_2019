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

print('Dígame la palabra a buscar:')
buscar = input()
busqueda = palabras.count(buscar)
if busqueda > 1:
    print ('La palabra ',buscar,' aparece',busqueda,' veces en la lista.')
elif busqueda == 0:
    print('La palabra ',buscar, ' no aparece en la lista.')
else:
    print('La palabra ', buscar, ' aparece una vez vez en la lista.')