agenda = {
    'Juan Perez' : {'telefono' : 83013040, 'correo' : 'jperez@gmail.com'},
    'Carlos Rojas' : {'telefono' : 87007070, 'correo' : 'crojas@hotmail.com'},
    'Ana Marin' : {'telefono' : 86006060, 'correo' : 'amarin@outlook.com'}
}

#Opcion 1: Crear diccionario para sofia

sofia = {
    'telefono' : 33333333,
    'correo' : 'sofia@gmail.com'
}
agenda['Sofia Castro'] = sofia
print(agenda)

#opcion2
agenda.update({'Sofia Castro' : sofia})

print(agenda)

