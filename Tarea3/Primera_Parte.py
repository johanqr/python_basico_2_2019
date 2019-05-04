# Para definir la agenda del hospital
agenda_hospital = []

persona = ('Juan', 'Mora', 100103111, 65, 81118811, 'dolor')

# agregamos una persona
agenda_hospital.append(persona)

# podemos revisar cual es el estatus de la agenda
# print(agenda_hospital)

# viene otra persona
persona = ('Ana', 'Jimenez', 32415116, 50, 46261266, 'consulta')
# agregamos otra persona
agenda_hospital.append(persona)

# podemos revisar cual es el estatus de la agenda
# print(agenda_hospital)

# suponga que vienen 5 personas mas
persona = [('Sofia', 'Alfaro', 32415116, 36, 51161161, 'consulta'),
           ('Carlos', 'Sanchez', 33411151, 15, 41655161, 'dolor'),
           ('Felipe', 'Perez', 12243151, 42, 65151111, 'documento'),
           ('Melissa', 'Alvarado', 734114144, 10, 87421312, 'dolor'),
           ('Pedro', 'Castro', 4372124141, 2, 99313131, 'dolor'), ]

# Podemos agregar esas personas que vienen todos de una sola vez
agenda_hospital.extend(persona)

# print(agenda_hospital)

# notemos que la impresión en pantalla está un poco sucia... lo arreglamos

# for paciente in agenda_hospital:
#    print(paciente)

print("Primera Parte")

# Primera Pregunta
print("Pregunta 1")
num1 = len(agenda_hospital)
print(num1)

# Segunda Pregunta
print("Pregunta 2")
padecimiento = [s for s in agenda_hospital if "dolor" in s]
num2 = len(padecimiento)
print(num2)

# Tercera pregunta
print("Pregunta 3")
for p in agenda_hospital:
    num3 = sorted(agenda_hospital,key=lambda x: x[3],reverse=True)
for n3 in num3:
    print(n3)

#Cuarta Pregunta
print("Pregunta 4")
mayor = [e for e in agenda_hospital if e[3] < 18]
num4 = len(mayor)
print("Mayor edad: ",num4)
menor = [e for e in agenda_hospital if e[3] >= 18]
num4 = len(menor)
print("Menor edad: ",num4)

# Quinta pregunta
print("Pregunta 5")
for p in agenda_hospital:
    num5 = sorted(sorted(agenda_hospital,key=lambda x: x[3],reverse=True), key=lambda y: y[5] == 'dolor',reverse=True)
for n5 in num5:
    print(n5)

#Sexta pregunta
print("Pregunta 6")
muertos = sorted([s for s in agenda_hospital if not "dolor" in s],key=lambda edad: edad[3])
num6 = (muertos)
for vivos in num6:
    print(vivos)