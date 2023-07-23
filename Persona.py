
# Creacion de una clase
class Persona:
    #Metodo inicializador
    def __init__(self):
        #Atributos
        self.nombre = 'Juan'
        self.apellido = 'Perez'
        self.edad = 28


#Creacion de un objeto de esta clase
persona1 = Persona()

#Imprimimos valores de la instancia persona1
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)