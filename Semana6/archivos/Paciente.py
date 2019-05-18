class Paciente:
    def __init__(self,nombre,apellido,telefono,direccion,enfermedades,medicamentos):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono= telefono
        self.direccion = direccion
        self.enfermedades = [enfermedades]
        self.medicamentos = [medicamentos]

