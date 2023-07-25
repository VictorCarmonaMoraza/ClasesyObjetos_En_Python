
# Creacion de una clase
class Persona:
    #Metodo inicializador
    def __init__(self, nombre, apellido, edad):
        #Atributos
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')


#Creacion de un objeto de esta clase
persona1 = Persona('Juan','Carmona',28)

#Imprimimos valores de la instancia persona1
persona1.mostrar_detalle()
#Persona.mostrar_detalle(persona1)
persona1.telefono = '666 666 777'
print(persona1.telefono)


#Creacion de un segundo objeto de tipo Persona
persona2 = Persona('Karla','Gomez',45)

#Imprimimos valores de la instancia persona2
persona2.mostrar_detalle()
