
# Creacion de una clase
class Persona:
    #Metodo inicializador
    def __init__(self, nombre, apellido, edad):
        #Atributos
        self.__nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self.__nombre} {self.apellido} {self.edad}')


#Creacion de un objeto de esta clase
persona1 = Persona('Juan','Carmona',28)

#Con doble guion bajo no podemos modificar el valor del parametro
persona1.__nombre ="Felix"
persona1.mostrar_detalle()