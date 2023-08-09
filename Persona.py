
class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad

    @property
    def nombre(self):
        print('Lllamndo getter nombre')
        return self._nombre

    @nombre.setter
    def nombre(self,nombre):
        print('Lllamndo setter nombre')
        self._nombre = nombre



persona1 = Persona('Juan','Carmona',28)
persona1.nombre ='Lucia'
print(persona1.nombre)
