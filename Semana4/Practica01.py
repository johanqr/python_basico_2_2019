#personas = (dict(nombre = 'Juan Perez',telefono = 83013040,correo = 'jperez@gmail.com'),
#          dict(nombre='Carlos Rojas',telefono=81111111,correo='crojas@hotmail.com'),
#          dict(nombre='Ana Marin',telefono=8222222,correo='amarin@outlook.com'))

#agenda = (personas)

#for p in agenda:
#    print(p)

#pass

#Agenda contactos
agenda = {
    'Juan Perez' : {'telefono' : 83013040, 'correo' : 'jperez@gmail.com'},
    'Carlos Rojas' : {'telefono' : 87007070, 'correo' : 'crojas@hotmail.com'},
    'Ana Marin' : {'telefono' : 86006060, 'correo' : 'amarin@outlook.com'}
}

print(agenda)
print(agenda['Ana Marin'])
print(agenda['Ana Marin']['telefono'])


