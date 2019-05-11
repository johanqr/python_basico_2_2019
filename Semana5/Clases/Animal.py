class Animal:
    def __init__(self,e,a):
        self.especie = e
        self.edad = a

    def crecer(self,edad=0):
        if(self.edad + edad) > 14:
            self.vivo = False
        else:
            self.edad += edad
            self.vivo = True

    def correr(self):
        print('Soy un {}. '
          'Estoy corriendo'.format(self.especie)) # format me permite sustituir lo que esta en llaves



#Se instancia un perro
perro = Animal('perro',3)
perro.crecer(3)

print("hola soy un {} "
      "tengo {} años".format(perro.especie,perro.edad))

if perro.vivo:
    print("hola soy un {} "
          "tengo {} años".format(perro.especie, perro.edad))
else:
    print("Me morí ... RIP")
