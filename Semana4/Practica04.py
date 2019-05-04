agenda = {
    'Juan Perez' : {'telefono' : 83013040, 'correo' : 'jperez@gmail.com'},
    'Carlos Rojas' : {'telefono' : 87007070, 'correo' : 'crojas@hotmail.com'},
    'Ana Marin' : {'telefono' : 86006060, 'correo' : 'amarin@outlook.com'}
}

#print(agenda.items())
#print(agenda.values())

#for contactos in agenda.items():

#Johan
#for persona, datos in agenda.items():
#    print('Nombre: ',persona,datos)


#Keys()
print('Usando keys')
for persona in agenda.keys():
    print('nombre: ',persona,
           'telefono:',agenda[persona]['telefono'],
           'correo:', agenda[persona]['correo'])

#Items()
print('Usando items')
for persona, info in agenda.items():
    print('nombre: ',persona,
           'telefono: ',info['telefono'],
           'correo: ',info['correo'])