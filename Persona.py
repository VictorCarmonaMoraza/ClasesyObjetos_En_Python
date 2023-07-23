
# Creacion de una clase
class Persona:
    #Metodo inicializador
    def __init__(self, nombre, apellido, edad):
        #Atributos
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


#Creacion de un objeto de esta clase
persona1 = Persona('Juan','apellido',28)

#Imprimimos valores de la instancia persona1
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)