
# Creacion de una clase
class Persona:
    #Metodo inicializador
    def __init__(self, nombre, apellido, edad):
        #Atributos
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

    def mostrar_detalle(self):
        print(f'Persona: {self.__nombre} {self.apellido} {self.edad}')


#Creacion de un objeto de esta clase
persona1 = Persona('Juan','Carmona',28)
#print(persona1.nombre)
persona1.nombre ='Lucia'
print(persona1.nombre)
