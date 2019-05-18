from archivos.Paciente import *


el_paciente = Paciente('Tyrion','Lannister',22222222,'Castlely Rock','fiebre,migraña,mareos','paracetamol,alcohol')


agenda_pacientes  = {'nombre' : el_paciente.nombre,'apellido' : el_paciente.apellido,'telefono' : el_paciente.telefono,'direccion' : el_paciente.direccion,'enfermedades' : el_paciente.enfermedades,'medicamentos' : el_paciente.medicamentos}

pacientes = [agenda_pacientes]
print(pacientes)

nuevo_paciente = Paciente('nombre': nuevo_paciente.nombre, 'apellido': 'nuevo_paciente.apellido', 'telefono': nuevo_paciente.telefono,'Winterfell',',know_nothing,gripe','sopa,acetaminofen')

pacientes.append(nuevo_paciente)
print(pacientes)

