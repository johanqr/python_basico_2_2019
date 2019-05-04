agenda = {
    'Juan Perez' : {'telefono' : 83013040, 'correo' : 'jperez@gmail.com'},
    'Carlos Rojas' : {'telefono' : 87007070, 'correo' : 'crojas@hotmail.com'},
    'Ana Marin' : {'telefono' : 86006060, 'correo' : 'amarin@outlook.com'}
}


def agregar(phone,email,name):
    contacto = {
        'telefono': phone,
        'correo': email
    }
    agenda.update({name: contacto})

#opcion 2
def agregar_contacto(phone,email,name):
    agenda[name]={'telefono': phone,
                   'correo' : email}


agregar(55555555,'johanquesada@gmail.com','Johan Quesada')

for p in agenda.items():
    print(p)