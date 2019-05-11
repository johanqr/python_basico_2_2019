class Duck:
    def __init__(self,nombre): # funcion para definir una variable interna nombre
        self.duck_nombre = nombre

    def quack(self): #self es requerido por que son metodos de si mismo
        print('Quaack!')

    def walk(self):
        print('Walk like a duck')

# Nace un pato llamado donald
#donald = Duck() # Sin atributo nombre solo definimos la clase
donald = Duck('donald') # Es obligatorio poner un nombre

# Donald dice Quack y camina
donald.quack()
donald.walk()

print("Cual es tu nombre?: ",donald.duck_nombre)