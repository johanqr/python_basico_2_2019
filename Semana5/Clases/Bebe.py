class Bebe:

    def __init__(self,nombre,edad):
        self.bebe_nombre = nombre
        self.bebe_edad = edad

    def respira(self):
        print("El bebé está respirando")

    def comer(self):
        print("El bebé está comiendo")

    def llorar(self):
        print("El bebé está llorando")

    def dormir(self):
        print("El bebé está durmiendo")

    def crecer(self,edad=1):
            self.bebe_edad += edad

#Nace un bebé
#mocoso = Bebe() # Bebe sin parametro nombre
mocoso = Bebe('Jon Snow',0)
print("Hola mi nombres es {} y tengo {} años".format(mocoso.bebe_nombre,mocoso.bebe_edad))

'''#El bebe despierta
print("-- El bebé despierta --")
mocoso.respira()

mocoso.llorar()
print("-- ¿Tiene hambre? --")
mocoso.comer()

mocoso.llorar()

print("-- ¿Tiene sueño? --")

mocoso.dormir()'''

#crecer bebe

mocoso.crecer()
print("Hola mi nombres es {} y tengo {} años".format(mocoso.bebe_nombre,mocoso.bebe_edad))